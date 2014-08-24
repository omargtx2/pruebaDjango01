from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404

# Create your views here.
def inicio(request):
   return render_to_response('index.html')
   ##return render_to_response('base.html')
