from django.shortcuts import render
from .models import Work

# Create your views here.
def index(request):

	work1 = Work()
	work1.first_name = 'Computer'
	work1.last_name = 'Vision'
	work1.img = '01.jpg'
	work1.caption = 'I am working on CNN and Computer vision for 1 year.'
	work1.offer = True

	work2 = Work()
	work2.first_name = 'Natural'
	work2.last_name = 'Language Processing'
	work2.img = '02.jpg'
	work2.caption = 'NLP is old..'
	work2.offer = False

	work3 = Work()
	work3.first_name = 'Speech'
	work3.last_name = 'Recognition'
	work3.img = '03.jpg'
	work3.caption = 'Speech Recognition is so complex'
	work3.offer = True

	work4 = Work()
	work4.first_name = 'Computer'
	work4.last_name = 'Science'
	work4.img = '04.jpg'
	work4.caption = 'I love cse'
	work4.offer = False

	work5 = Work()
	work5.first_name = 'Electric'
	work5.last_name = 'Engineering'
	work5.img = '05.jpg'
	work5.caption = 'EEE is bad'
	work5.offer = True

	work6 = Work()
	work6.first_name = 'Information'
	work6.last_name = 'Technology'
	work6.img = '06.jpg'
	work6.caption = 'ICE is not bad'
	work6.offer = False

	works = [work1, work2, work3, work4, work5, work6]

	return render(request, 'mysite/index.html', {'works': works})
