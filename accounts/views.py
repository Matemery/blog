from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
# Create your views here.
class SignUpView(CreateView):
    template_name = 'registration/signup.html'

    # form class is an attribute from the CreateView generic class that allows us to let django know from any another
    #form class to handle the creation of objects
    form_class = UserCreationForm
    success_url = reverse_lazy('home')