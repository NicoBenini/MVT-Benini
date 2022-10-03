import email
from django.shortcuts import HttpResponse
from django.template import loader, Template, Context
from django.shortcuts import render

# Create your views here.
from .models import Familiar

def familiar(self):
   mihtml = open("C:/Users/Nicolas/Desktop/Python/ProyectoCoderFamilia/AppFamilia/templates/template.html")
   template = Template(mihtml.read())#loader.get_template("template.html")
   mihtml.close()
   
   familiar1 = Familiar(nombre = "Nicolas", edad = 31, fecha_nacimiento = "1991-05-21", email = "nicolas@hotmail.com")
   familiar1.save()
   familiar2 = Familiar(nombre = "Lucia", edad = 31, fecha_nacimiento = "1987-03-01", email = "lucia@hotmail.com")
   familiar2.save()
   familiar3 = Familiar(nombre = "Milagros", edad = 31, fecha_nacimiento = "2005-01-31", email = "milagros@hotmail.com")
   familiar3.save()
   #mensaje1 = f"Soy {familiar1.nombre}, tengo {familiar1.edad} años, nací el {familiar1.fecha_nacimiento} y mi mail es {familiar1.email}"
   #mensaje2 = f"Soy {familiar2.nombre}, tengo {familiar2.edad} años, nací el {familiar2.fecha_nacimiento} y mi mail es {familiar2.email}"
   #mensaje3 = f"Soy {familiar3.nombre}, tengo {familiar3.edad} años, nací el {familiar3.fecha_nacimiento} y mi mail es {familiar3.email}"

   
   dict_de_contexto = {
        "familiar1": familiar1,
        "familiar2": familiar2,
        "familiar3": familiar3,
    }
   micontexto = Context(dict_de_contexto)
   #mensaje = f" {mensaje1}<br>{mensaje2}<br>{mensaje3}"
   res = template.render(micontexto)
   
   return HttpResponse(res)