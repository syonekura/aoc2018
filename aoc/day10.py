import numpy as np
import re


def parse_points(points):
    pattern = re.compile(r'position=<(\s+)?(-?\d+),(\s+)?(-?\d+)>\svelocity=<(\s+)?(-?\d+),(\s+)?(-?\d+)>')

