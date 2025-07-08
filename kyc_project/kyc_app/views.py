from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import base64
from datetime import datetime
import os
from django.conf import settings
 
def home(request):
    return render(request, 'login.html')
 
@login_required
def admin_dashboard(request):
    return render(request, 'dashboard.html')
 
@login_required
def user_call(request):
    return render(request, 'user_call.html')
 
@login_required
def upload_screenshot(request):
    if request.method == 'POST':
        image_data = request.POST.get('image')
        format, imgstr = image_data.split(';base64,')
        img_bytes = base64.b64decode(imgstr)
        filename = f'screenshot_{datetime.now().strftime("%Y%m%d_%H%M%S")}.png'
        path = os.path.join(settings.MEDIA_ROOT, 'screenshots', filename)
 
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'wb') as f:
            f.write(img_bytes)
 
        return JsonResponse({'status': 'success', 'file': filename})
 