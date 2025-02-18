from django.shortcuts import get_object_or_404, render
from django.http import FileResponse, Http404, HttpResponse, HttpResponseRedirect, JsonResponse
import requests
from .models import File
import os
from django.conf import settings
import cloudinary
# def file_list(request):
#     files = File.objects.all()
#     return render(request, 'downloads/file_list.html', {'files': files})

# def download_file(request, file_id):
#     try:
#         file_obj = get_object_or_404(File, id=file_id)

#         # Generate a signed Cloudinary URL (valid for 1 hour)
#         signed_url, _ = cloudinary.utils.cloudinary_url(
#             file_obj.file.name, secure=True, sign_url=True
#         )

#         # Redirect user to the signed URL
#         return HttpResponseRedirect(signed_url)

#     except File.DoesNotExist:
#         raise Http404("File not found")
def download_pdf(request, file_id):
    # Retrieve file instance
    file_instance = get_object_or_404(File, id=file_id)

    # Get Cloudinary file URL
    file_url = file_instance.file.url

    # Fetch the file from Cloudinary
    response = requests.get(file_url, stream=True)

    if response.status_code == 200:
        # Create HTTP response to force download
        download_response = HttpResponse(response.raw, content_type='application/pdf')
        download_response['Content-Disposition'] = f'attachment; filename="{file_instance.name}.pdf"'

        return download_response
    else:
        return HttpResponse("File not found", status=404)