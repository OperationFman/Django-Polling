from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
	return render(request, "hello_world.html", {"title": "Hello There!     General kenobi!"})

def about_page(request):
	return render(request, "about.html", {"title": "what ABOUT the droid attack on the wookies?"})

def contact_page(request):
	return render(request, "hello_world.html", {"title": "you MUST contact me. It's a trick, send no reply"})
