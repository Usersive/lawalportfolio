from django.shortcuts import get_object_or_404, render
from django.http import FileResponse, Http404, HttpResponse, HttpResponseRedirect
from .models import File
import os
from django.conf import settings

def file_list(request):
    files = File.objects.all()
    return render(request, 'downloads/file_list.html', {'files': files})

# def download_file(request, file_id):
#     try:
#         file_obj = File.objects.get(id=file_id)
#         file_path = os.path.join(settings.MEDIA_ROOT, str(file_obj.file))

#         return FileResponse(open(file_path, 'rb'), as_attachment=True)
#     except File.DoesNotExist:
#         raise Http404("File not found")


def download_file(request, file_id):
    try:
        file_obj = get_object_or_404(File, id=file_id)

        # Cloudinary URL
        file_url = file_obj.file.url  # This should return the Cloudinary URL

        # Redirect to the Cloudinary URL for the file
        return HttpResponseRedirect(file_url)

    except File.DoesNotExist:
        raise Http404("File not found")

