from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    def execute(self, notification: str):
        pass
    
    
class SMSStrategy(Strategy):
    def execute(self, notification: str):
        print(f"Sending SMS notification: {notification}")
    
        
class EmailStrategy(Strategy):
    def execute(self, notification: str):
        print(f"Sending Email notification: {notification}")
    
        
class PushStrategy(Strategy):
    def execute(self, notification: str):
        print(f"Sending Push notification: {notification}")
    
        
class CallStrategy(Strategy):
    def execute(self, notification: str):
        print(f"Making Call notification: {notification}")


class LetterStrategy(Strategy):
    def execute(self, notification: str):
        print(f"Sending Letter notification: {notification}")
        
        
class Context:
    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy
    
    def set_strategy(self, strategy: Strategy):
        self._strategy = strategy
    
    def execute_strategy(self, notification: str):
        return self._strategy.execute(notification)
    
        
if __name__ == '__main__':
    context = Context(SMSStrategy())
    print("Client: Strategy is set to SMSStrategy.")
    context.execute_strategy("This is a test notification SMS.")
    
    print()
    
    print("Client: Strategy is set to Email.")
    context.set_strategy(EmailStrategy())
    context.execute_strategy("This is a test notification email.")