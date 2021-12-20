from django.shortcuts import render
from django.http import HttpResponse
from xhtml2pdf import pisa
from django.template.loader import get_template
from .models import Person

# Create your views here.

def pdf(request):
    people = Person.objects.all()
    template_path = 'home.html'
    context = {'people':people}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline;filename="people.pdf"'
    template = get_template(template_path)
    html = template.render(context)

    pisa_status = pisa.CreatePDF(html,dest=response)
    if pisa_status.err:
        return HttpResponse('some errors occured <pre>'+ html + '</pre>')
    return response