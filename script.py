# exec(open('/home/louca/Documents/Scolaire/M1/Algorithmique de base et python/pygis/script.py'.encode('utf-8')).read())
import os

# Loading layers
wdir = "/home/louca/Documents/Scolaire/M1/Algorithmique de base et python/pygis/data/"

layers = [
	QgsVectorLayer(os.path.join(wdir, "shapefiles/regions.shp"), "Regions", "ogr"),
	QgsVectorLayer(os.path.join(wdir, "shapefiles/trees.shp"), "Trees", "ogr")
]

QgsProject.instance().removeAllMapLayers()

for layer in layers:
	if not layer.isValid():
		print("Error in loading layer", layer)
	else: 
		QgsProject.instance().addMapLayer(layer)

print("Layers loaded")

# Layer info
for l in QgsProject.instance().mapLayers().values():
	print("Couche", l.name())
	print("Couche de type", l.type(), ", d'emprise ", l.extent())
	print("Contient ", l.featureCount(), " entités")
	print("Liste des attributs :", l.fields().names())
	print("Liste des attributs :", [f.name() for f in l.fields()])
	print("--------")

# ...