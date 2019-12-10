#Shapes
#Do not run


# Drawing shapes
# w/o polymorphism
shapes = [trl, sql, crl]
for a_shape in shapes:
	if type(a_shape) == "Triangle":
		a_shape.draw_triangle()
	if type(a_shape) == "Square":
		a_shape.draw_square()
	if type(a_shape) == "Circle":
		a_shape.draw_circle()


# Drawing shapes
# with polymorphism
shapes == [trl,
		   swl,
		   crl]
for a_shape in shapes:
	a_shape.draw()