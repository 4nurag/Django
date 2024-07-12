from django.http import HttpResponse

# This is views
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
