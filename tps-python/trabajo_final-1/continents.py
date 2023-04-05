
class Continents:
  def __init__(self, nombre):
    self.nombre = nombre
    self.paises = []
    self.poblacion = 0
    self.idioma = {} 

  def add_pais(self, pais):
    self.paises.append(pais)

  def get_nombre(self):
    return self.nombre

  def get_poblacion(self):
    return self.poblacion

  def get_idioma(self):
    return self.idioma

  def get_paises(self):
    return self.paises

  def population_update(self, cant):
    self.poblacion += cant

  def language_add(self, lengua):
    self.idioma[lengua] = 1 

  def use_add(self, lengua):
    self.idioma[lengua] += 1

  def language_update(self, list_leng):
    for i in range(len(list_leng)):
      if self.idioma.get(list_leng[i], -1) == -1 :
        self.language_add(list_leng[i])
      else:
        self.use_add(list_leng[i])

  def get_lengua_popular(self):
    cantidad = -1
    for clave, valor in self.get_idioma().items():
      if valor > cantidad:
        pais = clave
        cantidad = valor
    return pais, cantidad

