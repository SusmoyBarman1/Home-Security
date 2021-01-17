from django.shortcuts import render
from .models import Work

# Create your views here.
def index(request):

	work1 = Work()
	work1.first_name = 'Computer'
	work1.last_name = 'Vision'
	work1.caption = 'I am working on CNN and Computer vision for 1 year.'

	return render(request, 'mysite/index.html', {'work1': work1})
