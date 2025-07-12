import numpy as np

class Context:
    """Stores tensors needed for backward pass"""
    def __init__(self):
        self.saved_tensors = []
    
    def save_for_backward(self, *args):
        self.saved_tensors.extend(args)

class Function:
    """Base class for all autograd operations"""
    @staticmethod
    def forward(ctx, *args, **kwargs):
        raise NotImplementedError
    
    @staticmethod
    def backward(ctx, grad_output):
        raise NotImplementedError
    
    @classmethod
    def apply(cls, *args, **kwargs):
        ctx = Context()
        output = cls.forward(ctx, *args, **kwargs)
        if any(isinstance(t, Tensor) and t.requires_grad for t in args):
            output._ctx = ctx
            output.grad_fn = cls
            output.requires_grad = True
        return output

class Tensor:
    """Main tensor class with autograd support"""
    def __init__(self, data, requires_grad=False):
        self.data = np.array(data)
        self.requires_grad = requires_grad
        self.grad = None
        self.grad_fn = None
        self._ctx = None
    
    def backward(self, grad_output=None):
        if not self.requires_grad:
            raise RuntimeError("Called backward on non-requires-grad tensor")
        
        if grad_output is None:
            grad_output = Tensor(1.0)
        self.grad = grad_output if isinstance(grad_output, Tensor) else Tensor(grad_output)
        
        # Topological sort
        visited = set()
        topo = []
        
        def build_topo(tensor):
            if tensor not in visited:
                visited.add(tensor)
                if tensor._ctx:
                    for t in tensor._ctx.saved_tensors:
                        if isinstance(t, Tensor):
                            build_topo(t)
                topo.append(tensor)
        
        build_topo(self)
        
        # Backward pass
        for tensor in reversed(topo):
            if tensor._ctx and tensor.grad_fn:
                grads = tensor.grad_fn.backward(tensor._ctx, tensor.grad)
                if not isinstance(grads, (list, tuple)):
                    grads = (grads,)
                
                for t, g in zip(tensor._ctx.saved_tensors, grads):
                    if isinstance(t, Tensor) and t.requires_grad:
                        if t.grad is None:
                            t.grad = Tensor(np.zeros_like(t.data))
                        t.grad.data += g.data
    
    def __add__(self, other):
        return Add.apply(self, other if isinstance(other, Tensor) else Tensor(other))
    
    def __mul__(self, other):
        return Mul.apply(self, other if isinstance(other, Tensor) else Tensor(other))
    
    def sin(self):
        return Sin.apply(self)
    
    def __repr__(self):
        return f"Tensor(data={self.data}, grad_fn={self.grad_fn.__name__ if self.grad_fn else None})"

# Operation Implementations
class Add(Function):
    @staticmethod
    def forward(ctx, a, b):
        ctx.save_for_backward(a, b)
        return Tensor(a.data + b.data)
    
    @staticmethod
    def backward(ctx, grad_output):
        return grad_output, grad_output

class Mul(Function):
    @staticmethod
    def forward(ctx, a, b):
        ctx.save_for_backward(a, b)
        return Tensor(a.data * b.data,requires_grad=True)
    
    @staticmethod
    def backward(ctx, grad_output):
        a, b = ctx.saved_tensors
        return grad_output * b.data, grad_output * a.data

class Sin(Function):
    @staticmethod
    def forward(ctx, x):
        ctx.save_for_backward(x)
        return Tensor(np.sin(x.data),requires_grad=True)
    
    @staticmethod
    def backward(ctx, grad_output):
        x = ctx.saved_tensors[0]
        return grad_output * np.cos(x.data)

# Example Usage
if __name__ == "__main__":
    print("=== Autograd System Demo ===")
    
    # Create tensors
    x = Tensor(2.0, requires_grad=True)
    y = Tensor(3.0, requires_grad=True)
    
    # Forward pass
    z = x * y  # z = x*y
    # out = z.sin() + 5  # out = sin(z) + 5
    
    print("\nForward Pass:")
    print(f"x: {x}")
    print(f"y: {y}")
    print(f"z = x*y: {z}")
    # print(f"out = sin(z)+5: {out}")
    
    # Backward pass
    z.backward()
    
    print("\nBackward Pass Results:")
    print(f"∂out/∂x: {x.grad}")  # Should be cos(x*y)*y
    print(f"∂out/∂y: {y.grad}")  # Should be cos(x*y)*x
    
    # Mathematical verification
    expected_grad_x = np.cos(2*3) * 3
    expected_grad_y = np.cos(2*3) * 2
    print("\nMathematical Verification:")
    print(f"Expected ∂out/∂x: {expected_grad_x:.4f}")
    print(f"Expected ∂out/∂y: {expected_grad_y:.4f}")
    
    print("\nGradients match expected values!" if np.allclose(x.grad.data, expected_grad_x) and 
          np.allclose(y.grad.data, expected_grad_y) else "\nGradient mismatch!")