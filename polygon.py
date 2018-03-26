import math
from point import Point

class Polygon:
    def __init__(self, vertices):
        self.vertices = vertices

    def __len__(self):
        return len(self.vertices)

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        if self.i < len(self.vertices):
            i = self.i
            self.i += 1
            return self.vertices[i]

        raise StopIteration

    def __str__(self):
        s = ""
        for v in self.vertices:
            s += "%s " % v
        return "[ %s]" % s

    def __getitem__(self, item):
        return self.vertices[item]

    @property
    def cx(self):
        return float(sum(v.x for v in self.vertices)) / len(self.vertices)

    @property
    def cy(self):
        return float(sum(v.y for v in self.vertices)) / len(self.vertices)

    def _sort_vertices_ccw(self):
        centroid = Point(self.cx, self.cy)
        return sorted(self.vertices, key=lambda v: v.angle(centroid))

    def sort(self):
        '''
            In-place sorting vertices in counter-clockwise order
        '''
        self.vertices = self._sort_vertices_ccw()