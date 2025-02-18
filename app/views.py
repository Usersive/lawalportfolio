import cloudinary.utils
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, Http404
from .models import File

def download_file(request, file_id):
    try:
        file_obj = get_object_or_404(File, id=file_id)

        # Generate a signed Cloudinary URL (valid for 1 hour)
        signed_url, _ = cloudinary.utils.cloudinary_url(
            file_obj.file.name, secure=True, sign_url=True
        )

        # Redirect to the signed URL
        return HttpResponseRedirect(signed_url)

    except File.DoesNotExist:
        raise Http404("File not found")