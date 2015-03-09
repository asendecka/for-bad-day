from django.shortcuts import render, redirect

from .models import Quote
from .forms import QuoteForm

def quote(request):
    quote = Quote.objects.order_by('?')[0]
    return render(request, 'quotes/quote.html', {'quote': quote})

def add_quote(request):
    if request.method == "POST":
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thanks')
    else:
        form = QuoteForm()
    return render(request, 'quotes/add_quote.html', {'form': form})

def thanks(request):
    return render(request, 'quotes/thanks.html')
