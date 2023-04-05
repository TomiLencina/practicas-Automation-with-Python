class Continentes:
  def __init__(self, nombre):
    self.nombre = nombre
    self.paises = []
    self.poblacion = 0
    self.idioma = {} 

  def agregar_pais(self, pais):
    self.paises.append(pais)

  def get_nombre(self):
    return self.nombre

  def get_poblacion(self):
    return self.poblacion

  def get_idioma(self):
    return self.idioma

  def get_paises(self):
    return self.paises

  def cant_poblacion(self, cant):
    self.poblacion += cant

  def language_add(self, lengua):
    self.idioma[lengua] = 1 

  def l_usada(self, lengua):
    self.idioma[lengua] += 1

  def get_lengua_popular(self):
    cantidad = -1
    for clave, valor in self.get_idioma().items():
      if valor > cantidad:
        pais = clave
        cantidad = valor
    return pais, cantidad

  def language_update(self, cant_leng):
    for i in range(len(cant_leng)):
      if self.idioma.get(cant_leng[i], -1) == -1 :
        self.language_add(cant_leng[i])
      else:
        self.l_usada(cant_leng[i])






class Pais:

  def __init__(self, nombre, monedas):
    self.nombre = nombre   
    self.monedas = monedas 
    self.poblacion = 0     
    self.lenguaje = []
    self.continente = None

  def get_continente(self):
    return self.continente

  def get_nombre(self):
    return self.nombre  

  def get_monedas(self):
    return self.monedas  
  
  def get_poblacion(self):
    return self.poblacion

  def get_lenguaje(self):
    return self.lenguaje

  def set_continente(self, cont):
    self.continente = cont  

  def set_poblacion(self, cantidad):
    self.poblacion = cantidad

  def agregar_lenguaje(self, lengua):
    self.lenguaje.append(lengua)

  def update_p(self):
    self.continente.cant_poblacion(self.get_poblacion())

  def update_l(self):
    self.continente.language_update(self.get_lenguaje())
