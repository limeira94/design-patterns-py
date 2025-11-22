from abc import abstractmethod, ABC

# PRODUTO é a classe complexa
class Robot:
    def __init__(self):
        self.bipedal = False
        self.wheeled = False
        self.traversal = []
        self.detection_systems = []
        
    def __str__(self):
        string = ""
        if self.bipedal: string += "ROBÔ BÍPEDE\n"
        if self.wheeled: string += "ROBÔ EM RODAS\n"
        if self.traversal: string += "Módulos de locomoção:\n"
        for module in self.traversal: string += f"- {module}\n"
        if self.detection_systems: string += "Sistemas de detecção:\n"
        for system in self.detection_systems: string += f"- {system}\n"
        return string
    

# Interface Builder
class RobotBuilder(ABC):
    @abstractmethod
    def reset(self):
        "Reinicia o builder, geralmente criando um objeto produto em branco"
        pass
    
    @abstractmethod
    def build_traversal(self):
        "implementa as etapas de construir o sistema de locomoção"
        pass
    
    @abstractmethod
    def build_detection_system(self):
        "implementa etapa de construir sistema de deteccao"
        pass

# Builder concretos
class AndroidBuilder(RobotBuilder):
    def __init__(self):
        self.product = Robot()

    def reset(self):
        self.product = Robot()

    def get_product(self) -> Robot:
        # Retorna o produto e, opcionalmente, o reseta para futuras construções
        return self.product

    def build_traversal(self):
        # Configurações específicas para um Android (Bípede + Braços)
        self.product.bipedal = True
        # As etapas de produção trabalham com a mesma instância de produto [7]
        self.product.traversal.append("duas pernas")
        self.product.traversal.append("dois braços")

    def build_detection_system(self):
        # Configurações específicas para um Android (Câmeras)
        self.product.detection_systems.append("câmeras")

class AutonomousCarBuilder(RobotBuilder):
    def __init__(self):
        self.product = Robot()

    def reset(self):
        self.product = Robot()

    def get_product(self) -> Robot:
        return self.product

    def build_traversal(self):
        # Configurações específicas para um Carro (Rodas)
        self.product.wheeled = True
        self.product.traversal.append("quatro rodas")

    def build_detection_system(self):
        # Configurações específicas para um Carro (Infravermelho)
        self.product.detection_systems.append("infravermelho")
       
# DIRECTOR 
class Director:
    def make_android(self, builder: RobotBuilder) -> Robot:
        builder.reset()
        builder.build_traversal()
        builder.build_detection_system()
        return builder.get_product()

    def make_autonomous_car(self, builder: RobotBuilder) -> Robot:
        builder.reset()
        builder.build_traversal()
        builder.build_detection_system()
        return builder.get_product()
    
    
if __name__ == '__main__':
    director = Director()
    android_builder = AndroidBuilder()

    # 1. Construção via Director (padrão)
    android = director.make_android(android_builder)
    print("--- Robô 1: Android (Via Director) ---")
    print(android)

    # 2. Construção customizada (sem Director, passo a passo)
    car_builder = AutonomousCarBuilder()
    car_builder.reset() # Começa do zero
    car_builder.build_traversal()
    # O cliente decide omitir o sistema de detecção, se quiser
    car = car_builder.get_product()
    print("--- Robô 2: Carro Autônomo (Customizado) ---")
    print(car)