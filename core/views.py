from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.core.mail import send_mail
from .forms import ContactForm
from .models import *
from .models import Contact

class HomeTemplateView(TemplateView):
    template_name = 'home.html'

    # override get context date method
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # first, call super get context data
        context['about'] = About.objects.first()
        context['skills'] = Skill.objects.all()
        context['works'] = RecentWork.objects.all()
        context['cskills'] = CodeSkill.objects.all()
        context['sskills'] = SoftSkill.objects.all()
        context['home'] = MyIcon.objects.first()
        #context['form'] = ContactForm()
        return context

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            options = form.cleaned_data['options']
            concern = form.cleaned_data['concern']
            print(name, email, phone, options, concern)
            contact = Contact(name=name, email=email, phone=phone, options=options, concern=concern)
            contact.save()
            return redirect('/')
        else:
            return render(request, 'home.html', {'form': form})
    else:
        form = ContactForm()
    return render(request, 'home.html', {'form': form})
