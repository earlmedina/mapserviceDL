import fiona, fiona.crs, requests

# DEPENDENCIES/INFO BELOW:
# Installing GDAL: http://www.gisinternals.com/query.html?content=filelist&file=release-1900-x64-gdal-2-3-2-mapserver-7-2-1.zip
# https://sandbox.idre.ucla.edu/sandbox/tutorials/installing-gdal-for-windows
# Fiona: https://media.readthedocs.org/pdf/fiona/latest/fiona.pdf

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

# Make Request
request = requests.post(url, data=params)
geojson_resp = fiona.ogrext.buffer_to_virtual_file(bytes(request.content))

with fiona.open(geojson_resp) as source:
    with fiona.open(
            'mapservice.shp',
            'w',
            driver='ESRI Shapefile',
            crs = source.crs,
            schema=source.schema) as sink:
        for rec in source:
            sink.write(rec)
