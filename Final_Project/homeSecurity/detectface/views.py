from django.shortcuts import render

# Create your views here.
def detect(request):
	return render(request, 'detectface/detect.html')