#Escriba un programa que tenga inicialmente un diccionario con los siguientes datos de
#dos personas:
#Nombre
#Apellido
#Edad
#Email
#Persona 1: Emilia, Cabrera de 23 años de edad, email ecabrera@curso.com
#Persona 2: Gustavo Andrés, Peralta de 26 años de edad, email gperalta@curso.com
#El programa debe permitir la carga de una persona más y agregarla al diccionario.
#Ingresados los datos de esta persona nueva deben imprimirse los datos de las 3 personas
#cargadas de manera tabular.

datos = {
    "persona1" : {"Nombre" : "Emilia",
                "Apellido" : "Cabrera",
                "Edad" : "23 años",
                "Mail" : "ecabrera@curso.com"},

    "persona2" : {"Nombre" : "Gustavo Andres",
                "Apellido" : "Peralta",
                "Edad" : "26 años",
                "Mail" : "gperalta@curso.com"}
}

def agregar_persona():
    print("Responda las siguientes preguntas...")
    nombre = input("Ingrese su nombre: \n")
    apellido = input("Ingrese su apellido: \n")
    edad = input("Ingrese su edad: \n")
    mail = input("Ingrese su mail: \n")

    datos["persona3"] = { "Nombre" : nombre,
                        "Apellido" : apellido,
                "Edad" : edad,
                "Mail" : mail}

    print("Persona1: {} \n Persona2: {} \n Persona3: {}".format(datos["persona1"], datos["persona2"], datos["persona3"]))

agregar_persona()

#print(datos)