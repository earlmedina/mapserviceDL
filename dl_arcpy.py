# This works for Python 3 installed with ArcGIS Pro

import urllib.parse, urllib.request, os, arcpy

# URL to query
url = "https://sampleserver6.arcgisonline.com/arcgis/rest/services/Census/MapServer/3/query?"

# Query Parameters
params = {'where': '1=1',
		   'geometryType': 'esriGeometryEnvelope',
		   'spatialRel': 'esriSpatialRelIntersects',
		   'relationParam': '',
		   'outFields': '*',
		   'returnGeometry': 'true',
		   'geometryPrecision':'',
		   'outSR': '',
		   'returnIdsOnly': 'false',
		   'returnCountOnly': 'false',
		   'orderByFields': '',
		   'groupByFieldsForStatistics': '',
		   'returnZ': 'false',
		   'returnM': 'false',
		   'returnDistinctValues': 'false',
		   'f': 'pjson'
		   }

# Encode parameters with urllib.parse: https://docs.python.org/3/library/urllib.parse.html
encode_params = urllib.parse.urlencode(params).encode("utf-8")

# Make request and read it using urllib.request: https://docs.python.org/3/library/urllib.request.html
response = urllib.request.urlopen(url, encode_params)
json = response.read()


#Get JSON response and write to json text file
with open("mapservice.json", "wb") as ms_json:
	ms_json.write(json);

# Covert JSON to Shapefile with JSON to Features: http://pro.arcgis.com/en/pro-app/tool-reference/conversion/json-to-features.htm
ws = os.getcwd() + os.sep
arcpy.JSONToFeatures_conversion("mapservice.json", ws + "mapservice.shp")
