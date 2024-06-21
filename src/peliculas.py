import xml.etree.ElementTree as ET
import requests
import json

def meter_peliculas(root):
  root_peliculas = ET.SubElement(root, 'peliculas')

  for pagina in range(1):
    meter_peliculas_pagina(pagina + 1, root_peliculas)
  print("Peliculas acaba")

def meter_peliculas_pagina(pagina, root):
  peliculas_json = get_peliculas_json(pagina)
  peliculas_dict = json.loads(peliculas_json)

  for pelicula in peliculas_dict["results"]:
    meter_pelicula(pelicula, root)
    break

def meter_pelicula(pelicula_general, root):
  id_pelicula = pelicula_general["id"]
  pelicula_json = get_pelicula_json(id_pelicula)
  pelicula_dict = json.loads(pelicula_json)
  
  _codigo = "a" + str(id_pelicula)
  _duracion = pelicula_dict["runtime"]
  _presupuesto = pelicula_dict["budget"]
  _ganancia =  pelicula_dict["revenue"]
  _calificacion = pelicula_dict["vote_average"]
  nodo_pelicula = ET.SubElement(root, 
                                'pelicula', 
                                codigo = str(_codigo), 
                                duracion = str(_duracion),
                                presupuesto = str(_presupuesto),
                                ganancia = str(_ganancia),
                                calificacion = str(_calificacion))

  ET.SubElement(nodo_pelicula, 'titulo').text = pelicula_dict["title"]
  ET.SubElement(nodo_pelicula, 'descripcion').text = pelicula_dict["overview"]
  ET.SubElement(nodo_pelicula, 'pais_origen').text = pelicula_dict["origin_country"][0] 
  ET.SubElement(nodo_pelicula, 'lenguaje').text = pelicula_dict["original_language"]

  fecha_lanzamiento = str(pelicula_dict["release_date"])
  anio, mes, dia = fecha_lanzamiento.split("-")
  nodo_fecha = ET.SubElement(nodo_pelicula, 'fecha_lanzamiento')
  ET.SubElement(nodo_fecha, 'anio').text = anio
  ET.SubElement(nodo_fecha, 'mes').text = mes
  ET.SubElement(nodo_fecha, 'dia').text = dia

  nodo_generos = ET.SubElement(nodo_pelicula, 'generos')
  for genero in pelicula_dict["genres"]:
    ET.SubElement(nodo_generos, 'genero').text = genero["name"]

  nodo_productoras = ET.SubElement(nodo_pelicula, 'productoras')
  for productora in pelicula_dict["production_companies"]:
    nodo_productora = ET.SubElement(nodo_productoras, 'productora')
    ET.SubElement(nodo_productora, 'nombre').text = productora["name"]
    ET.SubElement(nodo_productora, 'pais_origen').text = productora["origin_country"]

  creditos_json = get_creditos_json(id_pelicula)
  creditos_dict = json.loads(creditos_json)
  nodo_creditos = ET.SubElement(nodo_pelicula, 'creditos')
  
  nodo_elenco = ET.SubElement(nodo_creditos, 'elenco')
  for actor in creditos_dict["cast"]:
    nodo_actor = ET.SubElement(nodo_elenco, 'actor')
    ET.SubElement(nodo_actor, 'nombre').text = actor["name"]
    ET.SubElement(nodo_actor, 'personaje').text = actor["character"]

  nodo_produccion = ET.SubElement(nodo_creditos, 'produccion')
  for operario in creditos_dict["crew"]:
    nodo_operario = ET.SubElement(nodo_produccion, 'operario')
    ET.SubElement(nodo_operario, 'nombre').text = operario["name"]
    ET.SubElement(nodo_operario, 'departamento').text = operario["department"]
    ET.SubElement(nodo_operario, 'puesto').text = operario["job"]

def get_creditos_json(id):
  url = f"https://api.themoviedb.org/3/movie/{id}/credits"

  headers = {
      "accept": "application/json",
      "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1ZjYwMjMxZWM0ZTY0Zjk5OTQxOWUyMWUyMDlmYjU2MiIsInN1YiI6IjY2NTUyOTFkMWM1MjljNjU5MTExMTI5MiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.Qv-5dHpCCvVHMkUwEbGEL5rUlpBenfZLjhmLpzWbDuw"
  }

  response = requests.get(url, headers=headers)

  return response.text

def get_pelicula_json(id):
  url = f"https://api.themoviedb.org/3/movie/{id}"

  headers = {
      "accept": "application/json",
      "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1ZjYwMjMxZWM0ZTY0Zjk5OTQxOWUyMWUyMDlmYjU2MiIsInN1YiI6IjY2NTUyOTFkMWM1MjljNjU5MTExMTI5MiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.Qv-5dHpCCvVHMkUwEbGEL5rUlpBenfZLjhmLpzWbDuw"
  }

  response = requests.get(url, headers=headers)
  
  return response.text

def get_peliculas_json(pagina) :
  url = f"https://api.themoviedb.org/3/discover/movie?page={pagina}"

  headers = {
      "accept": "application/json",
      "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1ZjYwMjMxZWM0ZTY0Zjk5OTQxOWUyMWUyMDlmYjU2MiIsInN1YiI6IjY2NTUyOTFkMWM1MjljNjU5MTExMTI5MiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.Qv-5dHpCCvVHMkUwEbGEL5rUlpBenfZLjhmLpzWbDuw"
  }

  response = requests.get(url, headers=headers)

  return response.text