CLUSTERS = {}

class Cluster:
    def __init__(self, tags=None):
        if tags is None:
            tags = frozenset()
        elif not isinstance(tags, frozenset):
            tags = frozenset(tags)
        self.tags = frozenset(tags)
        self.contextables = set()
        CLUSTERS[self.tags] = self

    def add(self, *args):
        self.contextables.add(*args)

    def populate(self, contextables):
        for contextable in contextables:
            if contextable.belongs_to(self):
                self.add(contextable)

    def __repr__(self):
        return "%s => %s" %(self.tags, self.contextables)

    def __contains__(self, item):
        return item in self.tags

    def __eq__(self, other):
        return self.tags == other.tags
    
    def __ne__(self, other):
        return not self.__eq__(other)

    def __len__(self):
        return len(self.contextables)


def create_clusters(contextables, clusters, tags):
    new_clusters = []
    for cluster in clusters:
        for tag in tags:
            if tag not in cluster:
                tag_cluster = CLUSTERS[frozenset([tag])]
                new_cluster = Cluster(cluster.tags.union(tag_cluster.tags))
                new_cluster.populate(cluster.contextables.union(tag_cluster.contextables))
                if new_cluster.contextables:
                    new_clusters.append(new_cluster)
    return list(sorted(new_clusters, key=lambda i: len(i)))

def merge_clusters(contextables, number=5):
    tags = order_tags(contextables)[:260]
    new_clusters = []
    for tag in tags:
        cluster = Cluster(frozenset([tag]))
        cluster.populate(contextables)
        new_clusters.append(cluster)
    for i in range(number-1):
        nclusters = create_clusters(contextables, new_clusters, tags)[:260/(i+2)]
        if nclusters:
            new_clusters = nclusters
        else:
            return new_clusters
    return new_clusters

def order_clusters(clusters):
    clusters = {}
    for cluster in clusters:
        for tag in contextable.content_tags:
            tag = tag.strip()
            if tags.has_key(tag):
                tags[tag] += 1
            else:
                tags[tag] = 1
    return sort_dict_by_value(tags)


def order_tags(contextables):
    tags = {}
    for contextable in contextables:
        for tag in contextable.content_tags:
            tag = tag.strip()
            if tags.has_key(tag):
                tags[tag] += 1
            else:
                tags[tag] = 1
    return sort_dict_by_value(tags)

def sort_dict_by_value(d):
    items=d.items()
    backitems=[ [v[1],v[0]] for v in items]
    backitems.sort()
    return [ item[1] for item in reversed(backitems) ]
