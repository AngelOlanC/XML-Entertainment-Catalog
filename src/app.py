import xml.etree.ElementTree as ET
from peliculas import meter_peliculas
from series import meter_series

def main():
  root = ET.Element('catalogo_entretenimiento')

  meter_peliculas(root)
  meter_series(root)

  tree = ET.ElementTree(root)
  tree.write('../out/data.xml')
main()