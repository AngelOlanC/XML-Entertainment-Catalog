import xml.etree.ElementTree as ET
import requests
import json

def meter_series(root):
  root_series = ET.SubElement(root, 'series')

  for pagina in range(1):
    meter_series_pagina(pagina + 1, root_series)
  print("series acaba")

def meter_series_pagina(pagina, root):
  series_json = get_series_json(pagina)
  series_dict = json.loads(series_json)

  for serie in series_dict["results"]:
    meter_serie(serie, root)
    break

def meter_serie(serie_general, root):
  id_serie = serie_general["id"]
  serie_json = get_serie_json(id_serie)
  serie_dict = json.loads(serie_json)
  
  _codigo = "a" + str(id_serie)
  nodo_serie = ET.SubElement(root, 
                            'serie', 
                            codigo = str(_codigo))

  ET.SubElement(nodo_serie, 'titulo').text = serie_dict["name"]
  ET.SubElement(nodo_serie, 'descripcion').text = serie_dict["overview"]
  ET.SubElement(nodo_serie, 'pais_origen').text = serie_dict["origin_country"][0] 
  ET.SubElement(nodo_serie, 'lenguaje').text = serie_dict["original_language"]

  fecha_lanzamiento = str(serie_dict["first_air_date"])
  anio, mes, dia = fecha_lanzamiento.split("-")
  nodo_fecha = ET.SubElement(nodo_serie, 'fecha_lanzamiento')
  ET.SubElement(nodo_fecha, 'anio').text = anio
  ET.SubElement(nodo_fecha, 'mes').text = mes
  ET.SubElement(nodo_fecha, 'dia').text = dia

  nodo_temporadas = ET.SubElement(nodo_serie, 'temporadas')
  for temporada in serie_dict["seasons"]:
    _num_episodios = temporada["episode_count"]
    _calificacion = temporada["vote_average"]
    nodo_temporada = ET.SubElement(nodo_temporadas, 
                                   'temporada',
                                    num_episodios = str(_num_episodios),
                                    calificacion = str(_calificacion))
    ET.SubElement(nodo_temporada, 'nombre').text = temporada["name"]
    ET.SubElement(nodo_temporada, 'descripcion').text = temporada["overview"]
    nodo_temporada_fecha = ET.SubElement(nodo_temporada, 
                                        'fecha_lanzamiento')
    if (temporada["air_date"] == None):
      ET.SubElement(nodo_temporada_fecha, 'anio').text = anio
      ET.SubElement(nodo_temporada_fecha, 'mes').text = mes
      ET.SubElement(nodo_temporada_fecha, 'dia').text = dia
    else:
      anio, mes, dia = fecha_lanzamiento.split("-")
      ET.SubElement(nodo_temporada_fecha, 'anio').text = anio
      ET.SubElement(nodo_temporada_fecha, 'mes').text = mes
      ET.SubElement(nodo_temporada_fecha, 'dia').text = dia

  nodo_autores = ET.SubElement(nodo_serie, 'autores')
  for autor in serie_dict["created_by"]:
    nodo_autor = ET.SubElement(nodo_autores, 'autor')
    ET.SubElement(nodo_autor, 'nombre').text = autor["name"]
    ET.SubElement(nodo_autor, 'genero').text = str(autor["gender"])

  nodo_generos = ET.SubElement(nodo_serie, 'generos')
  for genero in serie_dict["genres"]:
    ET.SubElement(nodo_generos, 'genero').text = genero["name"]

  creditos_json = get_creditos_json(id_serie)
  creditos_dict = json.loads(creditos_json)
  nodo_creditos = ET.SubElement(nodo_serie, 'creditos')
  
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
  url = f"https://api.themoviedb.org/3/tv/{id}/credits"

  headers = {
      "accept": "application/json",
      "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1ZjYwMjMxZWM0ZTY0Zjk5OTQxOWUyMWUyMDlmYjU2MiIsInN1YiI6IjY2NTUyOTFkMWM1MjljNjU5MTExMTI5MiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.Qv-5dHpCCvVHMkUwEbGEL5rUlpBenfZLjhmLpzWbDuw"
  }

  response = requests.get(url, headers=headers)

  return response.text

def get_serie_json(id):
  url = f"https://api.themoviedb.org/3/tv/{id}"

  headers = {
      "accept": "application/json",
      "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1ZjYwMjMxZWM0ZTY0Zjk5OTQxOWUyMWUyMDlmYjU2MiIsInN1YiI6IjY2NTUyOTFkMWM1MjljNjU5MTExMTI5MiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.Qv-5dHpCCvVHMkUwEbGEL5rUlpBenfZLjhmLpzWbDuw"
  }

  response = requests.get(url, headers=headers)
  
  return response.text

def get_series_json(pagina) :
  url = f"https://api.themoviedb.org/3/discover/tv?page={pagina}"

  headers = {
      "accept": "application/json",
      "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1ZjYwMjMxZWM0ZTY0Zjk5OTQxOWUyMWUyMDlmYjU2MiIsInN1YiI6IjY2NTUyOTFkMWM1MjljNjU5MTExMTI5MiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.Qv-5dHpCCvVHMkUwEbGEL5rUlpBenfZLjhmLpzWbDuw"
  }

  response = requests.get(url, headers=headers)

  return response.text