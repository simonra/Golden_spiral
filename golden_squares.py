#!/usr/bin/python
#-*-coding: utf-8 -*-

from decimal import *
getcontext().prec = 8

def makeNewSquare(edge_size, offset_left, offset_top, color):
	new_square_string = "\t\t\t\t<i style=\"position:absolute;display:inline-block;width: %sem;height: %sem;border:none;left: %sem;top: %sem;background-color: %s \"></i>\n" % (edge_size, edge_size, offset_left, offset_top, color)
	output_file.write(new_square_string)


# How long the shortest edge will be (for now in ems)
spiral_size_short_edge = Decimal('30')
shortest_premissible_edge = Decimal('0.00001');
golden_ratio = Decimal('1.61803398875')
spiral_size_long_edge = spiral_size_short_edge + (spiral_size_short_edge/golden_ratio)

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

colors = ["#0dff27","#00ffac","#0dc9ff","#0ce862","#0ce8df"]
current_shortest_edge = spiral_size_short_edge
offset_left = Decimal(0)
offset_top = Decimal(0)
iterator = 0

current_longest_horisontal_edge = spiral_size_short_edge
offset_left = Decimal(0)
offset_top = Decimal(0)
current_shortest_horisontal_edge = current_longest_horisontal_edge / golden_ratio
makeNewSquare(current_longest_horisontal_edge, offset_left, offset_top, colors[iterator])

#while(current_shortest_edge > shortest_premissible_edge):
for x in xrange(1,8):
	iterator = iterator + 1
	current_longest_vertical_edge = current_shortest_horisontal_edge
	current_total_vertical_edge = current_longest_horisontal_edge
	current_shortest_vertical_edge = current_total_vertical_edge - current_longest_vertical_edge
	offset_left, offset_top = (offset_left + current_longest_horisontal_edge, offset_top)
	makeNewSquare(current_shortest_horisontal_edge, offset_left, offset_top, colors[iterator % len(colors)])
	iterator = iterator + 1

	current_total_horisontal_edge = current_longest_vertical_edge
	current_longest_horisontal_edge = current_shortest_vertical_edge
	current_shortest_horisontal_edge = current_total_horisontal_edge - current_longest_horisontal_edge
	offset_left, offset_top = (offset_left + current_shortest_horisontal_edge, offset_top +current_longest_vertical_edge)
	makeNewSquare(current_longest_horisontal_edge, offset_left, offset_top, colors[iterator % len(colors)])
	iterator = iterator + 1

	current_longest_vertical_edge = current_shortest_horisontal_edge
	current_total_vertical_edge = current_longest_horisontal_edge
	current_shortest_vertical_edge = current_total_vertical_edge - current_longest_vertical_edge
	offset_left, offset_top = (offset_left - current_shortest_horisontal_edge, offset_top + current_shortest_vertical_edge)
	makeNewSquare(current_longest_vertical_edge, offset_left, offset_top, colors[iterator % len(colors)])
	iterator = iterator + 1

	current_total_horisontal_edge = current_longest_vertical_edge
	current_longest_horisontal_edge = current_shortest_vertical_edge
	current_shortest_horisontal_edge = current_total_horisontal_edge - current_longest_horisontal_edge
	offset_left, offset_top = (offset_left, offset_top - current_shortest_vertical_edge)
	makeNewSquare(current_longest_horisontal_edge, offset_left, offset_top, colors[iterator % len(colors)])

	current_shortest_edge = current_shortest_horisontal_edge
	# makeNewSquare(current_shortest_edge, offset_left, offset_top, colors[iterator % len(colors)])
	# iterator = iterator + 1
	# current_shortest_edge = current_shortest_edge / (golden_ratio ** Decimal(iterator))
	# offset_left = spiral_size_short_edge
	# offset_top = 0
# output_file.write(string_1 + str(shortest_premissible_edge) + string_2 + str(shortest_premissible_edge))

output_file.write("""\
			</span>
		</span>
	</body>
</html>""")
