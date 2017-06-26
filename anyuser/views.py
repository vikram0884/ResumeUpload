from django.shortcuts import render
from django.http import HttpResponse
from su.models import Uploader
from datetime import datetime

def upload_page(request):
    """
    Renders the upload template for the users to upload file
    """
    return render(request, 'upload.html', {'user':'Guest', 'title': 'Upload Page',})

def upload_file(request):
    """
    Uploads the file to the database and renders the status of the upload.
    """
    email = request.POST.get('email', None)
    mobile = request.POST.get('mobile', None)
    fname = request.FILES['file']
    contents = fname.read()
    fname = str(fname)
    ts_as_id = datetime.now().strftime("%Y%m%d%H%M%S%f")
    obj_uploader = Uploader(TIMESTAMP_AS_ID=ts_as_id, EMAIL=email, PHONE=mobile, FILENAME=fname, FILE=contents)
    obj_uploader.save()
    updr = Uploader.objects.filter(TIMESTAMP_AS_ID=ts_as_id)
    status = " Uploaded Successfully" if len(updr) > 0 else " Upload Failed"
    return render(request, 'back_to_upload.html', {'filename': fname, 'status': status} )
