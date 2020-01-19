from django.shortcuts import render
from .forms import WorkerForm


# Create your views here.
def worker_create_view(request):
    form = WorkerForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.salary = instance.work_time * instance.cost_in_hour
        form.save()
        form = WorkerForm()
    context = {
        'form': form
    }

    return render(request, "workers/worker_create.html", context)

    # if form.is_valid(): instance = form.save(commit=False)
    # # do what you want with the form fields like
    # Instance.salary = instance.work_time * cost_in_hour
    # # then
    # Instance.save()

    # continue to response

# form include:

# <tr><th><label for="id_work_time">Work time:</label></th><td><input type="number" name="work_time" step="1" required id="id_work_time"></td></tr>
# <tr><th><label for="id_f_name">F name:</label></th><td><input type="text" name="f_name" maxlength="50" required id="id_f_name"></td></tr>
# <tr><th><label for="id_cost_in_hour">Cost in hour:</label></th><td><input type="number" name="cost_in_hour" step="0.01" required id="id_cost_in_hour"></td></tr>
# <tr><th><label for="id_position">Position:</label></th><td><select name="position" id="id_position">
#   <option value="MANAGER">MANAGER</option>
#
#   <option value="developer" selected>DEVELOPER</option>
#
#   <option value="teamlead">TEAMLEAD</option>
#
#   <option value="pm">PM</option>
#
#   <option value="hr">HR</option>
#
# </select></td></tr>
# <tr><th><label for="id_s_name">S name:</label></th><td><input type="text" name="s_name" maxlength="50" required id="id_s_name"></td></tr>
#
