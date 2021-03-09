from django.shortcuts import render


def PRINCIPAL(request):
	return render(request,'home.html')



def Segunda(request):

	return render (request, 'segunda.html')