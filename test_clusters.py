from clouds import create_clouds, Contextable

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
    #  13
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
]


import unittest

class TestCluster(unittest.TestCase):
    def test_
