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

# our new view
def thing_detail(request, slug):
    # grab the object...
    thing = Thing.objects.get(slug=slug)

    # and pass to the template
    return render(request, 'things/thing_detail.html', {
	'thing': thing,
    })

