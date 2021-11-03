

def saludo(idiomaFuncion):
  if idiomaFuncion=="Español":
    print ("Hola")
  if idiomaFuncion=="English":
    print ("Hello")

def preguntaNombre (idioma):
  nombre =""
  if idioma=="Español":
    nombre=input("¿Cómo te llamas?: ")
  if idioma=="English":
    nombre=input ("What's your name?: ")
  return nombre


def saludoPersonal(idiomaFuncion, nombre):
  if idiomaFuncion=="Español":
    print ("Hola " + nombre)
  if idiomaFuncion=="English":
    print ("Hello " + nombre)


## Aquí empieza a ejecutarse mi código
idioma = input ("Elige un idioma (Español/English)")
saludo(idioma)
nombre=preguntaNombre(idioma)
saludoPersonal(idioma, nombre)