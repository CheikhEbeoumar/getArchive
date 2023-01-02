from django.shortcuts import redirect, render,get_object_or_404
from django.template.loader import render_to_string
from django.http import HttpResponse
from .forms import ArchiveForm
from .models import Archive
import os

# def index(request):
#   form = ArchiveForm()
#   return render(request, 'index.html', {'form': form})
  
def index(request):
   if request.method == 'POST':
     try: 
          semester = request.POST.get('semester')
          filiere = request.POST.get('filiere')
          archive = Archive.objects.get(semester=semester,filiere=filiere)
          zip_file=archive.files
          file_name=archive.file_name
          response = HttpResponse(zip_file, content_type='application/zip')
          response['Content-Disposition'] = 'attachment; filename= {}'.format(file_name)
          return response
          
     except:
       return HttpResponse(" Archive introuvable")      
   else:
     form = ArchiveForm()
     return render(request, 'index.html', {'form': form})
