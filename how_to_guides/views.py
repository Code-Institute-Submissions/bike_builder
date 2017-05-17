from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import HowTo
from .forms import HowToForm
from django.shortcuts import render, redirect


# Create your views here.
def how_to_guides(request):
    guides = HowTo.objects.all().order_by('uploaded_at')
    return render(request, 'how_to_guides/how_to_guides.html', {'guides': guides})


@login_required(login_url='/login/')
def upload_guide(request):
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
