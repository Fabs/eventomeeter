from clusters import merge_clusters, Cluster, order_tags

class Contextable:
    def __init__(self, tags):
        self.content_tags = map(str.strip, tags.split(","))

    def __repr__(self):
        return "|".join(self.content_tags)

    def belongs_to(self, cluster):
        content_tags_set = set(self.content_tags)
        intersection = set(content_tags_set).intersection(cluster.tags)
        return intersection in (content_tags_set, cluster.tags) 

ctxs = [Contextable("python, brhackday, eventomeeter"),
    Contextable("python, brhackday, eventomeeter"),
    Contextable("python, brhackday, eventomeeter"),
    Contextable("python, brhackday, eventomeeter"),
    Contextable("python, brhackday, eventomeeter"),
    Contextable("python, brhackday, eventomeeter"),
    Contextable("python, brhackday, eventomeeter"),
    Contextable("python, brhackday, eventomeeter"),
    Contextable("python, brhackday, eventomeeter"),
    Contextable("python, brhackday, eventomeeter"),
    Contextable("python, brhackday, eventomeeter"),
    Contextable("python, brhackday, eventomeeter"),
    #  12
    Contextable("brhackday, eventomeeter"),
    Contextable("brhackday, eventomeeter"),
    Contextable("brhackday, eventomeeter"),
    Contextable("brhackday, eventomeeter"),
    Contextable("brhackday, eventomeeter"),
    Contextable("brhackday, eventomeeter"),
    Contextable("brhackday, eventomeeter"),
    Contextable("brhackday, eventomeeter"),
    Contextable("brhackday, eventomeeter"),
    # 9
    Contextable("eventomeeter"),
    Contextable("eventomeeter"),
    Contextable("eventomeeter"),
    Contextable("eventomeeter"),
    Contextable("eventomeeter"),
    Contextable("eventomeeter"),
    # 6
    Contextable("php, ruby"),
    # 1
    Contextable("php"),
    # 1
    Contextable("ruby"),
    # 1
    Contextable("python"),
    Contextable("python"),
    Contextable("python"),
    Contextable("python"),
    # 4
    Contextable("brhackday, senac"),
    Contextable("brhackday, senac"),
    # 2
    Contextable("brhackday, senac, python"),
    Contextable("brhackday, senac, python"),
    # 2
]


import unittest

class TestCluster(unittest.TestCase):
    def test_brhackday_senac_python_clustering(self):
        clusters = merge_clusters(ctxs, 3)
        cluster = Cluster(set(["brhackday", "senac", "python"]))
        for c in clusters:
            if c == cluster:
                break
        else:
            self.fail("Cluster not found!")

        self.assertEquals(len(c), 8)

    def test_brhackday_eventomeeter_clustering(self):
        clusters = merge_clusters(ctxs, 2)
        cluster = Cluster(set(["brhackday", "eventomeeter"]))
        for c in clusters:
            if c == cluster:
                break
        else:
            self.fail("Cluster not found!")

        self.assertEquals(len(c), 27, c.contextables)

    def test_php_clustering(self):
        clusters = merge_clusters(ctxs, 1)
        cluster = Cluster(set(["php"]))
        for c in clusters:
            if c == cluster:
                break
        else:
            self.fail("Cluster not found!")

        self.assertEquals(len(c), 2, c.contextables)

    def test_php_ruby_clustering(self):
        clusters = merge_clusters(ctxs, 2)
        cluster = Cluster(set(["php", "ruby"]))
        for c in clusters:
            if c == cluster:
                break
        else:
            self.fail("Cluster not found!")

        self.assertEquals(len(c), 3)


unittest.main()
