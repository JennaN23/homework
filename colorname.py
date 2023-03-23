import argparse
import math
import sys

# R G B

# 255 (FF) R + 255 (FF) G + 255 (FF) B = white

# white  = 0xFFFFFF
# black  = 0x000000
# red    = 0xFF0000
# green  = 0x00FF00
# blue   = 0x0000FF
# yellow = 0xFFFF00

# given a new color, return a name

# 250 16 135  mauve
# 251 16 135  mauve
# 250 100 135 blood

# figure out distance between input and color
# |p-q|

colornames = {
	 'white':            [255, 255, 255], 'the void':      [0, 0, 0],
	 'party poison red': [255, 0, 0],     'green':         [0, 255, 0],
	 'blue':             [0, 0, 255],     'danger days dirt': [92, 60, 6],
	 'digust (yellow)':  [255, 255, 0],   'magenta':       [255, 0, 255],
	 'cyan':             [0, 255, 255],   'orange':        [255, 200, 0],
	 'purple':           [175, 0, 255],   'blood red':     [150, 2, 2],
	 'vampire red':      [97, 1, 1],      'forest green':  [6, 54, 0],
	 'bubblegum':        [255, 179, 237], 'wizard purple': [54, 6, 43],
	 'jet star blue':    [1, 3, 54],      'sky blue':      [114, 217, 237],
	 'black parade grey':[120, 120, 120], 'fun ghoul green': [0, 255, 76],
	 'cirice (blue-grey)': [55, 94, 94],  'gash red':      [128, 3, 38],
	 'light brown':     [163, 128, 88],   'marsh':         [113, 148, 71],
	 'kobra kid yellow': [212, 163, 4],  'feather boa pink': [237, 7, 134],
	 'feral femme':      [163, 8, 83],   'halloween orange': [221, 97, 14],
	 'traffic cone':     [245, 134, 49], 'ethmoid':        [246, 247, 210],
	 'bone':            [242, 240, 237], 
	 'bullets pink/purp': [224, 99, 201], 
	 'foundations blue': [37, 4, 92]
}


def find_color(lst):
	for key, value in colornames.items():
		dist = 0
		for i in range(3):
			dist += abs(int(lst[i]) - int(value[i]))
		tup = (dist, key)
		color_dist.append(tup)
	min_dist = min(color_dist)
	return min_dist[1]
	
# setup
parser = argparse.ArgumentParser(description='Brief description of program.')

# positional arguments (always required)
parser.add_argument('file', type=str, metavar='<file>', help='some file')

"""
# optional arguments with default parameters
parser.add_argument('-r', required=False, type=int, default=255,
	metavar='<int>', help='red value [%(default)s]')
parser.add_argument('-g', required=False, type=int, default=255,
	metavar='<int>', help='green value [%(default)s]')
parser.add_argument('-b', required=False, type=int, default=255,
	metavar='<int>', help='blue value [%(default)s]')
"""

# finalization
arg = parser.parse_args()

filename = arg.file

with open(filename, 'rt') as fp:
	for line in fp:
		if line.split() == []: continue
		color_dist = []
		try:
			r, g, b = line.split()
			r = int(r)
			g = int(g)
			b = int(b)
			assert(r >= 0 and r <= 255)
			assert(g >= 0 and g <= 255)
			assert(b >= 0 and b <= 255)
			rgb = [r, g, b]
			print(find_color(rgb))
		except:
			print(f'Line does not contain exactly 3 integers between 0 and 255', file=sys.stderr)
