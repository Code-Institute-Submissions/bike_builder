from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Gallery
from .forms import GalleryForm
from django.shortcuts import render, redirect


# Create your views here.
def gallery(request):
    images = Gallery.objects.all().order_by('-uploaded_at')
    return render(request, 'gallery/gallery.html', {'images': images})


@login_required(login_url='/login/')
def upload_image(request):
    if request.method == "POST":
        form = GalleryForm(request.POST, request.FILES)

        if form.is_valid():

            new_image = form.save(commit=False)
            new_image.uploader = request.user
            new_image.save()
            return redirect('gallery')

        else:
            messages.error(request, "We were unable to submit the form. Please check your details and try again.")

    else:
        form = GalleryForm()

    return render(request, 'gallery/gallery_form.html', {'form': form})