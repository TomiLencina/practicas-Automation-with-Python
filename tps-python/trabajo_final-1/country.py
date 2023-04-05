
class Country:

  def __init__(self, nombre, codigo):
    self.nombre = nombre   
    self.codigo = codigo   
    self.poblacion = 0     
    self.lenguaje = []
    self.provincias = []
    self.continente = None

  def get_continente(self):
    return self.continente

  def set_continente(self, contienete):
    self.continente = contienete

  def get_nombre(self):
    return self.nombre

  def get_codigo(self):
    return self.codigo

  def get_poblacion(self):
    return self.poblacion

  def get_lenguaje(self):
    return self.lenguaje

  def get_provincias(self):
    return self.provincias

  def set_poblacion(self, cantidad):
    self.poblacion = cantidad

  def add_lenguaje(self, lengua):
    self.lenguaje.append(lengua)

  def add_provincia(self, prov):
    self.provincias.append(prov)

  def update_p(self):
    self.continente.population_update(self.get_poblacion())

  def update_l(self):
    self.continente.language_update(self.get_lenguaje())
