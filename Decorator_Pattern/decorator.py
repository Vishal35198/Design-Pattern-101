# Component Interface 
from abc import ABC, abstractmethod

class TextComponent(ABC):
    @abstractmethod
    def render(self) -> str:
        pass
    
class PlainText(TextComponent):
    def __init__(self, content: str):
        self.content = content

    def render(self) -> str:
        return self.content
    
class TextDecorator(TextComponent):
    def __init__(self, component: TextComponent):
        self._component = component

    def render(self) -> str:
        return self._component.render()

# These are my decorators 
class BoldDecorator(TextDecorator):
    def render(self) -> str:
        return f"**{self._component.render()}**"

class ItalicDecorator(TextDecorator):
    def render(self) -> str:
        return f"_{self._component.render()}_"

class UnderlineDecorator(TextDecorator):
    def render(self) -> str:
        return f"<u>{self._component.render()}</u>"
    
if __name__ == "__main__":
    text = PlainText("Hello, Design Patterns!")

    # Apply decorators dynamically
    bold_italic_text = BoldDecorator(ItalicDecorator(text))
    underlined_text = UnderlineDecorator(text)
    full_formatted = UnderlineDecorator(BoldDecorator(ItalicDecorator(text)))

    print("Original:", text.render())
    print("Bold+Italic:", bold_italic_text.render())
    print("Underlined:", underlined_text.render())
    print("Full Formatting:", full_formatted.render())