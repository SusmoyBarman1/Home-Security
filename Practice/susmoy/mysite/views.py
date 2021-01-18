from django.shortcuts import render
from .models import Work

# Create your views here.
def index(request):

	works = Work.objects.all()

	return render(request, 'mysite/index.html', {'works': works})
