from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt

from transaction.models import Transaction, TransactionSummary, Fund
from django.contrib.auth.models import User
from django.db.models import Sum

from django.http import JsonResponse
from instruments.models import Instrument

# import braintree
# from django.contrib.auth.decorators import login_required
# from django.core.urlresolvers import reverse
# from django.utils.decorators import method_decorator
# from django.views import generic
#
# from . import forms
#
# class CheckoutView(generic.FormView):
#     """This view lets the user initiate a payment."""
#     form_class = forms.CheckoutForm
#     template_name = 'payment.html'
#
#     @method_decorator(login_required)
#     def dispatch(self, request, *args, **kwargs):
#         # We need the user to assign the transaction
#         self.user = request.user
#
#         # Ha! There it is. This allows you to switch the
#         # Braintree environments by changing one setting
#         if settings.BRAINTREE_PRODUCTION:
#             braintree_env = braintree.Environment.Production
#         else:
#             braintree_env = braintree.Environment.Sandbox
#
#         # Configure Braintree
#         braintree.Configuration.configure(
#             braintree_env,
#             merchant_id=settings.BRAINTREE_MERCHANT_ID,
#             public_key=settings.BRAINTREE_PUBLIC_KEY,
#             private_key=settings.BRAINTREE_PRIVATE_KEY,
#         )
#
#         # Generate a client token. We'll send this to the form to
#         # finally generate the payment nonce
#         # You're able to add something like ``{"customer_id": 'foo'}``,
#         # if you've already saved the ID
#         self.braintree_client_token = braintree.ClientToken.generate({})
#         return super(CheckoutView, self).dispatch(request, *args, **kwargs)
#
#     def get_context_data(self, **kwargs):
#         ctx = super(CheckoutView, self).get_context_data(**kwargs)
#         ctx.update({
#             'braintree_client_token': self.braintree_client_token,
#         })
#         return ctx
#
#     def form_valid(self, form):
#         # Braintree customer info
#         # You can, for sure, use several approaches to gather customer infos
#         # For now, we'll simply use the given data of the user instance
#         customer_kwargs = {
#             "first_name": self.user.first_name,
#             "last_name": self.user.last_name,
#             "email": self.user.email,
#         }
#
#         # Create a new Braintree customer
#         # In this example we always create new Braintree users
#         # You can store and re-use Braintree's customer IDs, if you want to
#         result = braintree.Customer.create(customer_kwargs)
#         if not result.is_success:
#             # Ouch, something went wrong here
#             # I recommend to send an error report to all admins
#             # , including ``result.message`` and ``self.user.email``
#
#             context = self.get_context_data()
#             # We re-generate the form and display the relevant braintree error
#             context.update({
#                 'form': self.get_form(self.get_form_class()),
#                 'braintree_error': u'{} {}'.format(
#                     result.message, _('Please get in contact.'))
#             })
#             return self.render_to_response(context)
#
#         # If the customer creation was successful you might want to also
#         # add the customer id to your user profile
#         customer_id = result.customer.id
#
#         """
#         Create a new transaction and submit it.
#
#
#         """
#         address_dict = {
#             "first_name": self.user.first_name,
#             "last_name": self.user.last_name,
#             "street_address": 'street',
#             "extended_address": 'street_2',
#             "locality": 'city',
#             "region": 'state_or_region',
#             "postal_code": 'postal_code',
#             "country_code_alpha2": 'alpha2_country_code',
#             "country_code_alpha3": 'alpha3_country_code',
#             "country_name": 'country',
#             "country_code_numeric": 'numeric_country_code',
#         }
#
#         # You can use the form to calculate a total or add a static total amount
#         # I'll use a static amount in this example
#         result = braintree.Transaction.sale({
#             "customer_id": customer_id,
#             "amount": 100,
#             "payment_method_nonce": form.cleaned_data['payment_method_nonce'],
#             "descriptor": {
#                 # Definitely check out https://developers.braintreepayments.com/reference/general/validation-errors/all/python#descriptor
#                 "name": "COMPANY.*test",
#             },
#             "billing": address_dict,
#             "shipping": address_dict,
#             "options": {
#                 # Use this option to store the customer data, if successful
#                 'store_in_vault_on_success': True,
#                 # Use this option to directly settle the transaction
#                 # If you want to settle the transaction later, use ``False`` and later on
#                 # ``braintree.Transaction.submit_for_settlement("the_transaction_id")``
#                 'submit_for_settlement': True,
#             },
#         })
#         if not result.is_success:
#             # Card could've been declined or whatever
#             # I recommend to send an error report to all admins
#             # , including ``result.message`` and ``self.user.email``
#             context = self.get_context_data()
#             context.update({
#                 'form': self.get_form(self.get_form_class()),
#                 'braintree_error': _(
#                     'Your payment could not be processed. Please check your'
#                     ' input or use another payment method and try again.')
#             })
#             return self.render_to_response(context)
#
#         # Finally there's the transaction ID
#         # You definitely want to send it to your database
#         transaction_id = result.transaction.id
#         # Now you can send out confirmation emails or update your metrics
#         # or do whatever makes you and your customers happy :)
#         return super(CheckoutView, self).form_valid(form)
#
#     def get_success_url(self):
#         # Add your preferred success url
#         return reverse('home.html')




def home(request):
    return render(request,'home.html')

def aboutUS(request):
    return render(request,'aboutUS.html')

def ContactUS(request):
    return render(request,'ContactUS.html')

def Register(request):
    return render(request,'Register.html')

def specs(request):
    return render(request,'specs.html')

def portfolio(request):
    trans = TransactionSummary.objects.filter(user=request.user.id)
    context = {'object':trans}
    return render(request,'portfolio.html',context)

def transaction(request):
    trans = Transaction.objects.filter(user=request.user.id)
    context = {'object':trans}
    return render(request,'transactions.html',context)

def funds(request):
    trans = Fund.objects.filter(user=request.user.id)
    context = {'object':trans}
    return render(request,'funds.html')

def deposits(request):
    return render(request,'deposit.html')






@csrf_exempt
def purchase_made(request):
    """Purchase made accepts a POST request from our Trade Futures Contract
    Our if statment verifies that a POST request comes in and that the user is
    Authenticated. We then get each portion of the get request, storing them into
    variables. Lastly, we create an instance of the Transaction class and using the
    request object, we get our user, and add the seperate portions of the POST
    request into the database"""

    # multiplier = Instrument.objects.values_list('multiplier')[11][0]
    # print(multiplier)
    if request.method == 'POST' and request.user.is_authenticated():
        quantity = request.POST.get('quantity')
        price = request.POST.get('price')
        symbol = request.POST.get('symbol')
        multiplier = request.POST.get('multiplier')
        if (int(quantity)!=0):
            t = Transaction()
            t.user = request.user
            t.symbol = symbol
            # t.timestamp=timestamp
            t.quantity = int(quantity)
            t.price = float(price)
            z=Instrument()
            z.multiplier = int(multiplier)
            t.transaction_amount= z.multiplier*t.quantity*t.price
            t.save()
            # transaction_list = Transaction.objects.values('symbol').annotate(total=Sum('transaction_amount'))
            transaction_list = Transaction.objects.filter(user=request.user.id).values('symbol').annotate(total=Sum('transaction_amount'))
            TransactionSummary.objects.filter(user=request.user.id).delete()
            for item in range(len(transaction_list)):
                y=TransactionSummary()
                y.user=request.user
                y.symbol=transaction_list[item]['symbol']
                y.symbol_total=transaction_list[item]['total']
                y.absolute_symbol=abs(y.symbol_total)
                y.save()
            z=Fund()
            z.user=request.user
            z.total_funds=int(total_funds)
            fund_list = Fund.objects.all.values('user').annotate(total=Sum('total_funds'))
            # FundSummary.objects.filter(user=request.user.id).delete()
            # for item in range(len(fund_list)):
            #     k=Funded()
            #     k.user=request.user
            #     k.total_funded=fund_list[item]['symbol']
            #     k.save()


            print(fund_list)
            # print(type(transaction_list))
            # print(transaction_list[0]['symbol'])
            return JsonResponse({'success':'true'})
        return
