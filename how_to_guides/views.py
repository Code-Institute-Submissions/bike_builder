from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import HowTo
from .forms import HowToForm
from django.shortcuts import render, redirect


def how_to_guides(request):
    """
    Render list of how-to guides, subject to pagination
    """
    guide_list = HowTo.objects.all().order_by('-uploaded_at')
    paginator = Paginator(guide_list, 10)  # 10 in each page
    page = request.GET.get('page')
    try:
        guides = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page
        guides = paginator.page(1)
    except EmptyPage:
        #  If page is out of range (e.g. 9999), deliver last page of results
        guides = paginator.page(paginator.num_pages)
    return render(request, 'how_to_guides/how_to_guides.html', {'page': page, 'guides': guides})


@login_required(login_url='/accounts/login/')
def upload_guide(request):
    """
    Allow authorised users to post guides
    """
    if request.method == "POST":
        form = HowToForm(request.POST)

        if form.is_valid():

            new_guide = form.save(commit=False)
            new_guide.uploader = request.user
            new_guide.save()
            return redirect('how_to_guides')

        else:
            messages.error(request, "We were unable to submit the form. Please check your details and try again.")

    else:
        form = HowToForm()

    return render(request, 'how_to_guides/how_to_guides_form.html', {'form': form})
