from django.contrib import messages
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.context_processors import csrf
from django.conf import settings
import stripe
from .forms import PaymentForm
from .models import Merchandise


stripe.api_key = settings.STRIPE_SECRET


def place_order(request, product_id):
    product = get_object_or_404(Merchandise, pk=product_id)
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            try:
                customer = stripe.Charge.create(
                    amount=product.price * 100,
                    currency="GBP",
                    description=form.cleaned_data['email_address'],
                    card=form.cleaned_data['stripe_id'],
                )

                if customer.paid:
                    form.save()
                    messages.success(request, "Your purchase has been successful")
                    return redirect(reverse('merchandise'))

                else:
                    messages.error(request, "We were unable to take payment from the card provided. "
                                            "Please re-enter the details or use a different card.")

            except stripe.error.CardError, e:
                messages.error(request, "Your card was declined!")

        else:
            messages.error(request, "We were unable to submit the form. Please check your details and try again.")

    else:
        form = PaymentForm()

    args = {'form': form, 'publishable': settings.STRIPE_PUBLISHABLE, 'product': product}
    args.update(csrf(request))

    return render(request, 'payments\make_payment.html', args)
