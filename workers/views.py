from django.shortcuts import render
from .forms import WorkerForm
from .models import Worker


# Create your views here.
def worker_create_view(request):
    form = WorkerForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = WorkerForm()
    context = {
        'form': form
    }
    return render(request, "workers/worker_create.html", context)


