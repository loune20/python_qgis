import os

wdir = "/home/louca/Documents/Scolaire/M1/Algorithmique de base et python/pygis/data/"

layers = [
	QgsVectorLayer(os.path.join(wdir, "shapefiles/regions.shp"), "Regions", "ogr"),
	QgsVectorLayer(os.path.join(wdir, "shapefiles/trees.shp"), "Trees", "ogr"),
	QgsVectorLayer(os.path.join(wdir, "shapefiles/rivers.shp"), "Rivers", "ogr")
]

QgsProject.instance().removeAllMapLayers()

for layer in layers:
	# print(layer)
	if not layer.isValid():
		print("Error in loading layer", layer)
	else: 
		QgsProject.instance().addMapLayer(layer)

print("Layers loaded")

for layer in QgsProject.instance().mapLayers().values():
	print(layer)
	print("Couche", layer.name())
	print("Couche de type", layer.type(), ", d'emprise ", layer.extent())
	print("Contient ", layer.featureCount(), " entités")
	print("Liste des attributs :", layer.fields().names())

for layer in QgsProject.instance().mapLayers().values():
	if layer.name() == "Trees":
		l_trees = layer

print(l_trees)
tree_type = set()
for feature in l_trees.getFeatures():
	tree_type.add(feature["VEGDESC"])

print(tree_type)

request = QgsFeatureRequest(QgsExpression("VEGDESC = 'Deciduous'"))
total_deciduous = 0
area_deciduous = 0

for feature in l_trees.getFeatures(request):
	total_deciduous += 1
	area_deciduous += feature["AREA_KM2"]

print(f"{total_deciduous=}, {area_deciduous=}")


for layer in QgsProject.instance().mapLayers().values():
	if layer.name() == "Rivers":
		rivers = layer

rivers_names = set()
for feature in rivers.getFeatures():
	rivers_names.add(feature["NAM"])

rivers_calc = {}
for name in rivers_names:
	request = QgsFeatureRequest(QgsExpression("NAM = '"+name+"'"))
	tot = 0
	longueur = 0
	for feature in rivers.getFeatures(request):
		tot += 1
		longueur += feature.geometry().length()
	rivers_calc[name] = longueur
	# print("Rivière : ", name, " ", tot, "segments", "longueur :", longueur)

