#!/usr/bin/env python
from os import listdir, system, mkdir

# HTML header
header = """<html><head><title>Thumbnails</title>
<style type="text/css">
img {
border: 0px solid white;
}
</style>
</head>
<body bgcolor="#404040">"""

# Trailing HTML
footer = '</body></html>'

def jpeg_images(filenames):
	for name in filenames:
		if name[-5:].lower() == '.jpeg' or \
			name[-4:].lower() == '.jpg':
			yield name

def raw_images(filenames):
	for name in filenames:
		if name[-4:].lower() in ('.nef', '.dng', '.crw', '.cr2' '.orf'):
			yield name
			
def thumbnail(img, thumb):
	v = system('convert -auto-orient -resize 180x180 "%s" -quality 85 "%s"' % (img, thumb)) or \
	system('jpegtran -copy none -outfile "%s" -optimize  "%s"' % (thumb, thumb))
	return v == 0

def main():
	filenames = listdir('.')
	html_lines = []
	try:
		mkdir('thumbs')
	except:
		pass
		
	for img in jpeg_images(filenames):
		print img
		thumb = 'thumbs/thumb-' + img[:-4] + '.jpg'
		if thumbnail(img, thumb):
			html_lines.append('<a href="%s"><img src="%s"></a>' % (img, thumb))
	
	for raw in raw_images(filenames):
		print raw
		thumb = 'thumbs/thumb-' + raw[:-4] + '.jpg'
		html_lines.append('<a href="%s"><img src="%s"></a>' % (raw, thumb))
	
	# Present images in alphabetical order	
	html_lines.sort()
	index = open('index.html', 'w')
	index.write(header + '\n')
	index.write('\n'.join(html_lines))
	index.write('\n' + footer)
	
main()
