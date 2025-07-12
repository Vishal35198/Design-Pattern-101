from abc import ABC, abstractmethod


# ! ABSTRACT PRODUCTS
class Button(ABC):

    @abstractmethod
    def render(self):
        raise NotImplementedError


class Slider(ABC):

    @abstractmethod
    def render(self):
        raise NotImplementedError


# ! CONCRETE PRODUCTS
class LightButton(Button):

    def render(self):
        print(f"Rendering the {self.__class__.__name__}")


class LightSlider(Button):
    def render(self):
        print(f"Rendering the {self.__class__.__name__}")
        

class DarkSlider(Button):

    def render(self):
        print(f"Rendering the {self.__class__.__name__}")


class DarkButton(Button):

    def render(self):
        print(f"Rendering the {self.__class__.__name__}")


# ! ABSTRACT FACTORY
class Themes(ABC):

    @abstractmethod
    def get_button(self) -> Button:
        raise NotImplementedError

    @abstractmethod
    def get_slider(self) -> Slider:
        raise NotImplementedError


class LightTheme(Themes):

    def get_button(self):
        return LightButton()

    def get_slider(self):
        return LightSlider()


class DarkTheme(Themes):

    def get_button(self):
        return DarkButton()

    def get_slider(self):
        return DarkSlider()


# ! CLIENT CODE


def client(theme: Themes):

    button = theme.get_button()
    button.render()

    slider = theme.get_slider()
    slider.render()


lighttheme = LightTheme()
darktheme = DarkTheme()
client(theme=lighttheme)
client(theme=darktheme)
