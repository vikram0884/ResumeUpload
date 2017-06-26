from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import traceback
from su.models import Uploader

from datetime import datetime

# Create your views here.

@login_required
def view_files(request):
    """
    Renders list of files(view page) to the ADMIN that are in SUBMITTED state, which are to be viewed and decisioned as APPROVED or REJECTED
    """
    try:
        rows = Uploader.objects.filter(STATUS="SUBMITTED")
        fields = [ str(field).split('.')[-1] for field in Uploader._meta.get_fields() if str(field).split('.')[-1] not in ['id', 'CLOSEDON', 'FILE',] ]
        fields.extend(['View', 'Approve', 'Reject',])
        data = {}
        data['cols'] = fields
        data['rows'] = rows
    except Exception:
        print traceback.format_exc()
        return HttpResponse("Internal Error")
    return render(request, "view_list.html", data)

@login_required
def view_doc(request):
    """
    Renders the file to view the contents as opted the ADMIN in view page
    """
    id_pri = request.GET.get("id")
    record = Uploader.objects.get(id=id_pri)
    file_content = record.FILE
    response = HttpResponse(file_content)
    response['Content-Disposition'] = 'attachment; filename=%s'%record.FILENAME.replace(" ", "_")
    return response

def process_decision(request, decision=None):
    """
    Updates the STATUS as decisioned by ADMIN
    """
    id_pri = request.GET.get("id")
    record = Uploader.objects.get(id=id_pri)
    record.STATUS = decision
    record.CLOSEDON = datetime.now()
    record.save()
    success = Uploader.objects.get(id=id_pri).STATUS == decision
    return success, record.FILENAME

@login_required
def approve_doc(request):
    """
    Renders the STATUS of the approval made by ADMIN
    """
    result, fname = process_decision(request, "APPROVED")
    decision = "Approved" if result else "is not Approved"
    return render(request, 'decision_page.html', {'decision': decision, 'filename': fname })

@login_required
def reject_doc(request):
    """
    Renders the STATUS of the rejection made by ADMIN
    """
    result, fname = process_decision(request, "REJECTED")
    decision = "is Rejected" if result else "is not rejected"
    return render(request, 'decision_page.html', {'decision': decision, 'filename': fname })

