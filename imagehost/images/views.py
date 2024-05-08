import os
from django.conf import settings
from django.shortcuts import render
from .forms import ImageForm
from .models import Image
from django.shortcuts import render, redirect

def home(request):
    return render(request, 'images/home.html')

def image_upload(request):
    message = ''
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save()
            message = 'Image uploaded successfully!'
            return render(request, 'images/image_upload.html', {'form': form, 'image': image, 'message': message})
    else:
        form = ImageForm()
    return render(request, 'images/image_upload.html', {'form': form, 'message': message})

def image_view(request):
    if request.method == 'POST':
        if 'delete_all' in request.POST:
            images = Image.objects.all()
            for image in images:
                os.remove(os.path.join(settings.MEDIA_ROOT, str(image.image)))
            images.delete()
        else:
            image = Image.objects.get(id=request.POST['image_id'])
            os.remove(os.path.join(settings.MEDIA_ROOT, str(image.image)))
            image.delete()
        return redirect('image_view')
    else:
        images = Image.objects.all()
        return render(request, 'images/image_view.html', {'images': images})