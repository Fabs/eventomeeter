from analyser import dig_web
from clusters import merge_clusters

mc = merge_clusters(dig_web(), 2)
