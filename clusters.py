class Cluster:
    def __init__(self, tags=None):
        if tags is None:
            tags = set()
        self.tags = tags
        self.contextables = set()

    def add(self, *args):
        self.contextables.add(*args)

    def __repr__(self):
        return "%s => %s" %(self.tags, self.contextables)

    def __contains__(self, item):
        return item in self.tags


def create_clusters(contextables, clusters, tags):
    new_clusters = [ Cluster(cluster.tags.union(set([tag]))) for cluster in clusters 
                           for tag in tags if tag not in cluster ]
    for contextable in contextables:
        for cluster in new_clusters:
            if contextable.belongs_to(cluster):
                cluster.add(contextable)
    return new_clusters

def order_tags(contextables):
    tags = {}
    for contextable in contextables:
        for tag in contextable.content_tags:
            tag = tag.strip()
            if tags.has_key(tag):
                tags[tag] += 1
            else:
                tags[tag] = 1
    return sort_dict_by_value(tags, limit=160)

def sort_dict_by_value(d, limit):
    items=d.items()
    backitems=[ [v[1],v[0]] for v in items]
    backitems.sort()
    return [ item[1] for item in reversed(backitems[-limit:]) ]

ctxs = order_tags(ctx)
print create_clusters(ctx, [ Cluster(set([tag])) for tag in ctxs ], ctxs)

