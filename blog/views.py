from django.http import HttpResponse 

# Create your views here.
def bloghome(request):
    return HttpResponse("This is bloghome")

def blogpost(request, slug):
    return HttpResponse(f"This is blogpost : {slug}")