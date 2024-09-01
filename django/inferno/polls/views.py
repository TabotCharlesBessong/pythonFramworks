from django.http import HttpResponse

# Create your views here.
def index(request):
  return HttpResponse("Hello world and welcome to the nord poll")
