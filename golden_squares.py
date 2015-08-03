#!/usr/bin/python
#-*-coding: utf-8 -*-

from decimal import *
getcontext().prec = 8

# Insert a new square into the HTML file with the specified parameters:
def makeNewSquare(edge_size, offset_left, offset_top, color):
	new_square_string = "\t\t\t\t<i style=\"position:absolute;display:inline-block;width: %sem;height: %sem;border:none;left: %sem;top: %sem;background-color: %s \"></i>\n" % (edge_size, edge_size, offset_left, offset_top, color)
	output_file.write(new_square_string)


# How long the shortest edge will be (for now in ems)
spiral_size_short_edge = Decimal('30')
# The smallest square is guaranteed to be larger than this:
shortest_premissible_edge = Decimal('0.00001')
golden_ratio = Decimal('1.61803398875')
# The long edge in ems given that one knows the length of the short edge:
spiral_size_long_edge = spiral_size_short_edge + (spiral_size_short_edge/golden_ratio)

# Inserting the start of the HTML file:
output_file = open('spiral' + str(spiral_size_short_edge) + '.html', 'w+')
output_file.write("""\
<html>
	<head>
		<title>Golden Spiral Squares, size """ +
		str(spiral_size_short_edge) + """ems</title>
		<meta content="">
		<style></style>
	</head>
	<body>\n""")
output_file.write("""\
		<span style="display: inline-block; width: """ + 
			str(spiral_size_short_edge) + """em; height: """ + 
			str(spiral_size_long_edge) + """em">
			<span style="position: relative; display: inline-block; width: """ + 
				str(spiral_size_short_edge) + """em; height: """ + 
				str(spiral_size_long_edge) + """em">\n""")

# Variables needed for the loop:
colors = ["#0dff27","#00ffac","#0dc9ff","#0ce862","#0ce8df"]
iterator = 0
leftmost_edge = Decimal(0)
rightmost_edge = spiral_size_long_edge
top_edge = Decimal(0)
bottom_edge = spiral_size_short_edge
edge_size = spiral_size_short_edge

while(edge_size > shortest_premissible_edge):

	# Make the leftmost square:
	edge_size = spiral_size_short_edge / (golden_ratio ** Decimal(iterator))
	makeNewSquare(edge_size, leftmost_edge, top_edge, colors[iterator % len(colors)])
	# Only the offset from the left has changed when making this square
	# therefore only the leftmost edge parameter is updated here
	leftmost_edge = leftmost_edge + edge_size
	iterator = iterator + 1

	# Make the top right square:
	edge_size = spiral_size_short_edge / (golden_ratio ** Decimal(iterator))
	makeNewSquare(edge_size, leftmost_edge, top_edge, colors[iterator % len(colors)])
	# Update only the topmost edge at this point
	top_edge = top_edge + edge_size
	iterator = iterator + 1

	# Make the bottom right square:
	edge_size = spiral_size_short_edge / (golden_ratio ** Decimal(iterator))
	makeNewSquare(edge_size, rightmost_edge - edge_size, top_edge, colors[iterator % len(colors)])
	# Update the rightmost_edge edge at this point
	rightmost_edge = rightmost_edge - edge_size
	iterator = iterator + 1

	# Make the bottom left (central) square of this iteration:
	edge_size = spiral_size_short_edge / (golden_ratio ** Decimal(iterator))
	makeNewSquare(edge_size, leftmost_edge, bottom_edge - edge_size, colors[iterator % len(colors)])
	# update bottom_edge:
	bottom_edge = bottom_edge - edge_size
	iterator = iterator + 1

# Closing the HTML file:
output_file.write("""\
			</span>
		</span>
	</body>
</html>""")
