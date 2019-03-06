import geojson, fiona, fiona.crs, urllib.parse, urllib.request, os
from gdal import ogr

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
		   'f': 'geojson'
		   }

# Encode parameters with urllib.parse: https://docs.python.org/3/library/urllib.parse.html
encode_params = urllib.parse.urlencode(params).encode("utf-8")

# Make request and read it using urllib.request: https://docs.python.org/3/library/urllib.request.html
response = urllib.request.urlopen(url, encode_params)




geojson_resp = geojson.loads(response.read())

with open('mapservice.geojson', 'w') as f:
    geojson.dump(geojson_resp, f)

f_in = 'mapservice.geojson'
f_out = 'mapservice.shp'

with fiona.open(f_in) as source:
    with fiona.open(
            f_out,
            'w',
            driver='ESRI Shapefile',
            crs = source.crs,
            schema=source.schema) as sink:

        for rec in source:
            sink.write(rec)
