from abc import ABC, abstractmethod

# Produtos 1
class AbstractDialog(ABC):
    @abstractmethod
    def render(self) -> None:
        pass

# Produtos 2
class AbstractButton(ABC):
    @abstractmethod
    def click(self, action: str) -> None:
        pass

# Implementações concretas dos produtos
class WindowsButton(AbstractButton):
    def click(self, action: str) -> None:
        print(f"Windows Button clicked! Performing action: {action}")
        

class WebButton(AbstractButton):
    def click(self, action: str) -> None:
        print(f"Web Button clicked! Performing action: {action}")


class WebDialog(AbstractDialog):
    def render(self) -> None:
        print("Rendering Web Dialog")
        

class WindowsDialog(AbstractDialog):
    def render(self) -> None:
        print("Rendering Windows Dialog")
        

# Fábricas abstratas
class AbstractGUIFactory(ABC):
    @abstractmethod
    def create_dialog(self) -> AbstractDialog:
        pass
    
    @abstractmethod
    def create_button(self) -> AbstractButton:
        pass

# Fábricas concretas
class WindowsFactory(AbstractGUIFactory):
    def create_dialog(self) -> AbstractDialog:
        return WindowsDialog()
    
    def create_button(self) -> AbstractButton:
        return WindowsButton()
    
    
class WebFactory(AbstractGUIFactory):
    def create_dialog(self) -> AbstractDialog:
        return WebDialog()
    
    def create_button(self) -> AbstractButton:
        return WebButton()


def client_code(factory: AbstractGUIFactory) -> None:
    dialog = factory.create_dialog()
    button = factory.create_button()
    
    dialog.render()
    button.click("Abrir...")


if __name__ == "__main__":
    print("Client: Testing client code with the Windows Factory:")
    client_code(WindowsFactory())
    
    print("\nClient: Testing the same client code with the Web Factory:")
    client_code(WebFactory())