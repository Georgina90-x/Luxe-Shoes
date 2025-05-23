from django.http import HttpResponse
from django.conf import settings
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

from checkout.webhook_handler import StripeWH_Handler

import stripe
import logging

logger = logging.getLogger(__name__)


@require_POST
@csrf_exempt
def webhook(request):
    """Listener of webhooks for Stripe"""
    # Setup
    wh_secret = settings.STRIPE_WH_SECRET
    stripe.api_key = settings.STRIPE_SECRET_KEY

    # get the webhook data and verify its signature
    payload = request.body
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE', None)
    if sig_header is None:
        return HttpResponse("Missing Stripe Signature", status=400)
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WH_SECRET
        )
    except ValueError as e:
        # Invalid payload
        logger.error(f"Invalid payload: {str(e)}")
        return HttpResponse(status=400)

    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        logger.error(f"Invalid payload: {str(e)}")
        return HttpResponse(status=400)

    except Exception as e:
        logger.error(f"Invalid payload: {str(e)}")
        return HttpResponse(content=e, status=400)

    # Set up a webhook handler
    handler = StripeWH_Handler(request)

    # Map webhook events to relevant handler functions
    event_map = {
        'payment_intent.succeeded': handler.handle_payment_intent_succeeded,
        'payment_intent.payment_failed': handler.handle_payment_intent_payment_failed,
    }

    # Get the webhook type from Stripe
    event_type = event['type']

    # If there's a handler for it, get it from the event map
    # Use the generic one by default
    event_handler = event_map.get(event_type, handler.handle_event)

    # Call the event handler with the event
    response = event_handler(event)
    return response
