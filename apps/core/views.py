from django.shortcuts import render


def frontpage(request):
    return render(request, 'core/frontpage.html')


def privacy(request):
    return render(request, 'core/privacy.html')


def terms(request):
    return render(request, 'core/terms.html')


def contact(request):
    return render(request, 'core/contact.html')
