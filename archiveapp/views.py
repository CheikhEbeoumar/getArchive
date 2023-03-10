from django.shortcuts import redirect, render,get_object_or_404
from django.template.loader import render_to_string
from django.http import HttpResponse
from .forms import ArchiveForm
from .models import Archive
import os
from django.http import StreamingHttpResponse

# def index(request):
#   form = ArchiveForm()
#   return render(request, 'index.html', {'form': form})
  
def index(request):
   if request.method == 'POST':
     try: 
          semester = request.POST.get('semester')
          filiere = request.POST.get('filiere')
          archive = Archive.objects.get(semester=semester,filiere=filiere)
          zip_file=archive.file 
          file_name=archive.file_name
          response = StreamingHttpResponse(zip_file, content_type='application/zip')
          response['Content-Disposition'] = 'attachment; filename= {}'.format(file_name)
          return response
         
     except:
       return HttpResponse("<h1  style='position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);'> Archive "+ filiere +" " + semester +" N'a pas encore été ajouté</h1>" )      
   else:
     form = ArchiveForm()
     return render(request, 'index.html', {'form': form})
