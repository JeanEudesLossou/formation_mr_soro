from django.shortcuts import render


def index(request):
    return render(request, 'portfolio/index.html')


def portfolio_details(request):
    return render(request, 'portfolio/portfolio-details.html')


def inner_page(request):
    return render(request, 'portfolio/inner-page.html')
