from django.shortcuts import render
from .models import Post

# Create your views here.


def home(request):
	context = {
		'posts': Post.objects.all()
	}
	return render(request, 'news_app/home.html', context)

def about(request):
	return render(request, 'news_app/about.html', {'title': 'About'})
