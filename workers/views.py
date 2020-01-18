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
    print(type(context))
    print(context['form'].Meta['cost_in_hour'])
    #print(context['form']['cost_in_hour'])
    #print(context['form']['work_time'])
    return render(request, "workers/worker_create.html", context)


