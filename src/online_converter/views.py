from django.http import HttpResponse
from django.shortcuts import render
from .forms import convertForm




def home_page(request):
	form = convertForm(request.POST or None)
	if form.is_valid():
	 	print(form.cleaned_data)
	content = {"answer": 'answer',
			   "form": form}
	# doc = "<h1>{title}</h1>".format(title=title)
	# django_rendered_doc = "<h1>{{title}}</h1>".format(title=title)

	return render(request, 'converter_frontend.html', content, )