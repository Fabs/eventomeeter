class Contextable:
    def belongs_to(self, cluster):
        content_tags_set = set(self.content_tags)
        intersection = set(content_tags_set).intersection(cluster.tags)
        return intersection in (content_tags_set, cluster.tags)

