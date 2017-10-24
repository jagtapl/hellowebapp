from django.shortcuts import render
from collection.models import Thing

# the rewritten view!
def index(request):
    things = Thing.objects.all()

    # just getting one object!
    # things = Thing.objects.filter(name__contains='Hello')

    return render(request, 'index.html', {
	'things': things,
    })
