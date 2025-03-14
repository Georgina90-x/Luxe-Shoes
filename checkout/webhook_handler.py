from django.http import HttpResponse


class StripeWH_Handler:
    """ Handles stripe webhooks """
    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """ Handles generic webhook events """
        return HttpResponse(
            content=f'Unhandled webhook received: {event['type']}',
            status=200
        )

    def handle_payment_intent_succeeded(self, event):
        """ Handles payment intent succeeded webhook for stripe """
        intent = event.data.object
        print(intent)
        return HttpResponse(
            content=f'Webhook received: {event['type']}',
            status=200
        )

    def handle_payment_intent_payment_failed(self, event):
        """ Handles payment intent failed webhook for stripe """
        return HttpResponse(
            content=f'Webhook received: {event['type']}',
            status=200
        )
