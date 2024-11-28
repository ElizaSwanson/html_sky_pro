from django.shortcuts import render


def mainpage(request):
    return render(request, 'catalogue/home.html')


def contact_page(request):
    return render(request, 'catalogue/contacts.html')
