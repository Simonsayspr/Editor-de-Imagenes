from filters.filter import Filter
from PIL import Image, ImageDraw
import math

class Star(Filter):
    def __init__(self, x, y, size, color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color

    def apply(self, im):
        self.im = im
        draw = ImageDraw.Draw(self.im)
        points = self.calculate_star_points(self.x, self.y, self.size)
        draw.polygon(points, outline=self.color)
        return self.im

    def calculate_star_points(self, x, y, size):
        outer_radius = size
        inner_radius = size // 2

        points = []
        for i in range(5):
            outer_x = x + outer_radius * math.cos(math.radians(i * 72))
            outer_y = y + outer_radius * math.sin(math.radians(i * 72))
            inner_x = x + inner_radius * math.cos(math.radians((i * 72) + 36))
            inner_y = y + inner_radius * math.sin(math.radians((i * 72) + 36))
            points.extend([(outer_x, outer_y), (inner_x, inner_y)])

        return points