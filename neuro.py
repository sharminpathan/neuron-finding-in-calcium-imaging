import matplotlib
import thunder as td
import json
import sys
import neurofinder
from extraction import NMF
from PIL import Image

print 'processing dataset: ' + sys.argv[1]
path = '/home/sharmin/Downloads/neurofinder' + sys.argv[1] 

#load images and perform median filtering
data = td.images.fromtif(path + '/images', stop=10, ext='tiff').median_filter(3)

algorithm = NMF(k=5, percentile=99, max_iter=50, overlap=0.1)

model = algorithm.fit(data, chunk_size=(50,50), padding=(25,25))

merged = model.merge(0.1)
print 'found ' + str(merged.regions.count) + 'regions'
regions = [{'coordinates': region.coordinates.tolist()} for region in merged.regions]
result = {'dataset': sys.argv[1], 'regions': regions}

print('writing results')
with open('submission.json', 'w') as f:
	f.write(json.dumps(result))

print "done"
