from django.shortcuts import render

# Create your views here.
def home(request):
	context = dict()
	context['name'] = 'Susmoy'
	context['list'] = [1, 2, 3, 4]
	return render(request, 'calc/index.html', context)

def add(request):

	val1 = int(request.POST['num1'])
	val2 = int(request.POST['num2'])

	res = val1 + val2

	return render(request, 'calc/result.html', {'result':res})