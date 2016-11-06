import thunder as td
import json
import matplotlib
from extraction import NMF
from pyspark import SparkContext


###########################################
# Setting up the chunk size and padding values from command-line arguments.
###########################################
chunk=int(sys.argv[3])
padding=int(sys.argv[4])

####
#Spark
####
spark = SparkSession\
        .builder\
        .appName("Neuron Finder")\
        .config("spark.driver.maxResultSize", "3g")\
        .getOrCreate()

sc=spark.sparkContext;

#######################
#Specifying the path and getting images
#######################
path = '/neurofinder.' + sys.argv[1] + '.test'
data = td.images.fromtif(path + '/images', stop=10, ext='tiff', engine=sc, npartitions= 10)

###############
#Applying NMF Algorithm
###############
algorithm = NMF(k=int(sys.argv[2]), percentile=99, max_iter=50, overlap=0.1)
model = algorithm.fit(data, chunk_size=(chunk,chunk), padding=(padding,padding))
merged = model.merge(0.1)

#####################
#Getting the regions and coordinates
#####################
regions = [{'coordinates': region.coordinates.tolist()} for region in merged.regions]
result = {'dataset': sys.argv[1], 'regions': regions}

with open('submission-' + sys.argv[1]  +'.json', 'w') as f:
	f.write(json.dumps(result))
