from abc import ABC, abstractmethod


class Notifier(ABC):
    @abstractmethod
    def send(self, message: str):
        pass


class EmailNotifier(Notifier):
    """
    Concrete Component
    """

    def send(self, message: str):
        print(f"Sending Email notification: {message}")


class NotifierDecorator(Notifier):
    def __init__(self, notifier: Notifier) -> None:
        self._notifier = notifier

    @property
    def notifier(self) -> Notifier:
        return self._notifier

    def send(self, message: str):
        return self._notifier.send(message)


class SMSDecorator(NotifierDecorator):
    """
    Concrete Decorator
    """

    def send(self, message: str):
        self.notifier.send(message)
        print(f"Sending SMS notification: {message}")


class SlackDecorator(NotifierDecorator):
    """
    Concrete Decorator
    """

    def send(self, message: str):
        modified_message = f"[SLACK ALERT] {message}"
        self.notifier.send(modified_message)
        print(f"Sending Slack notification: {modified_message}")


if __name__ == "__main__":
    message = "Alert! System is down."

    base_notifier = EmailNotifier()

    sms_wrapper = SMSDecorator(base_notifier)
    slack_wrapper = SlackDecorator(sms_wrapper)
    slack_wrapper.send(message)
