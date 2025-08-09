from django.shortcuts import render

# Create your views here.
from .model import ContactForm

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form,is_valid(){
            name = form.cleaned_data.get("name")
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]
            
            return render(request,"contact_success.html", {"name": name})
            else:
                form = ContactForm()

                return render(request, "contact.html", {"form": form})
        }


