from config import settings
from django.contrib.auth.views import redirect_to_login
from chore_main.forms import ChoreModelForm, PersonForm
from django.shortcuts import redirect, render
from django.views import generic
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from chore_main.forms import UserCreationForm
from chore_main.forms import PersonForm
from django.views.generic.base import RedirectView
from .models import Chore, Person, User
from django.contrib.auth.mixins import LoginRequiredMixin
class HomeView(TemplateView):
    template_name = "base_generic.html"
def create_user(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        person_form = PersonForm(request.POST)
        if user_form.is_valid() and person_form.is_valid():
            user = user_form.save()
            person = person_form.save(commit=False)
            person.user = user
            person.save()
            return redirect('/')
    else:
        user_form = UserCreationForm()
        person_form = PersonForm()
    return render(
        request,
        'register.html',
        {'user_form': user_form, 'person_form': person_form}
    )

def chore_list(request):
    chores = Chore.objects.all()
    context = {
        "chores" : chores
    }
    return render(request, 'chores.html', context)

class ChoresView(TemplateView):
    template_name = "chores.html"
    

def chore_create(request):

    if not request.user.is_authenticated:
        messages.info(request, 'You have to log in first!')
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    form  = ChoreModelForm()
    if request.method == "POST":
        form = ChoreModelForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            master = form.cleaned_data['master']
            slave = form.cleaned_data['slave']
            task = form.cleaned_data['task']
            Chore.objects.create(
                title = title,
                master = master,
                slave = slave,
                task = task
            )
            return redirect("/chores")
    context = {
        "form" : form
    }
    return render(request, 'chore_create.html', context)

# def register(request):
#     if request.method == 'POST':
#         f = UserCreationForm(request.POST)
#         if f.is_valid():
#             f.save()
#             messages.success(request, 'Account created successfully')
            

#     else:
#         f = UserCreationForm()

#     return render(request, 'register.html', {'form': f})

# Create your views here.
