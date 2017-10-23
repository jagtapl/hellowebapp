from django.shortcuts import render

# Create your views here.
def index(request):
    # this is your new view
    # defining the variable
    number = 6

    #enclose string in quotes
    thing = "Thing name"

    # passing the variable to the view
    return render(request, 'index.html', {
	'number': number,
        'thing' : thing,
    })
