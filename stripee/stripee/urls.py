from django.contrib import admin
from django.urls import path
from app.views import (
    CreateCheckoutSessionView,
    SuccessView,
    CancelView,
    ProductLandingPageView,
)
from app.views import stripe_webhook

from app.views import StripeIntentView, CustomPaymentView
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('create-payment-intent/<pk>/', StripeIntentView.as_view(), name='create-payment-intent'),
    path('custom-payment/', CustomPaymentView.as_view(), name='custom-payment'),
    path('webhooks/stripe/', stripe_webhook, name='stripe-webhook'),
    path('', ProductLandingPageView.as_view(), name='landing'),
    path('admin/', admin.site.urls),
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('success/', SuccessView.as_view(), name='success'),
    path('create-checkout-session/<pk>/',
         CreateCheckoutSessionView.as_view(), name='create-checkout-session')
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
