from abc import ABC, abstractmethod


class NotificationService(ABC):

    @abstractmethod
    def send_message(self, message):
        pass


class EmailNotification(NotificationService):

    def send_message(self, message):
        print("Sending Email:", message)


class SMSNotification(NotificationService):

    def send_message(self, message):
        print("Sending SMS:", message)


class WhatsAppNotification(NotificationService):

    def send_message(self, message):
        print("Sending WhatsApp:", message)


services = [
    EmailNotification(),
    SMSNotification(),
    WhatsAppNotification()
]

for service in services:
    service.send_message("Your order is confirmed")