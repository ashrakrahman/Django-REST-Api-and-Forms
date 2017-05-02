from django.shortcuts import redirect ,render
from django.http import HttpResponse
from django.template import loader
from .forms import RegistrationForm

def register (request):
    template = loader.get_template("register.html")
    context = {

    }
    return HttpResponse(template.render(context,request))

def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        form = RegistrationForm()
        args = {'form': form}
        return render(request,"reg_user.html",args)

