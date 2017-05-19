from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Gallery
from .forms import GalleryForm


# Create your views here.
def gallery(request):
    image_list = Gallery.objects.all().order_by('-uploaded_at')
    paginator = Paginator(image_list, 3)  # 3 in each page
    page = request.GET.get('page')
    try:
        images = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page
        images = paginator.page(1)
    except EmptyPage:
        #  If page is out of range (e.g. 9999), deliver last page of results
        images = paginator.page(paginator.num_pages)
    return render(request, 'gallery/gallery.html', {'page': page, 'images': images})

# def gallery(request):
#     images = Gallery.objects.all().order_by('-uploaded_at')
#     return render(request, 'gallery/gallery.html', {'images': images})


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
