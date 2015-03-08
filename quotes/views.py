from django.shortcuts import render

from .models import Quote

def quote(request):
    quote = Quote.objects.order_by('?')[0]
    return render(request, 'quotes/quote.html', {'quote': quote})
