from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('Index page')

def hello(request, id):
    print(id)
    return HttpResponse('<h2>Hello %s</h2>' % id)

def about(request):
    return HttpResponse('About')