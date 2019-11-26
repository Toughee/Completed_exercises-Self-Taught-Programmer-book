#OOP - object oriented programming - instantiating a class - creating an object 5
class Orange():
	def __init__(self, w, c):
		"""weights are in oz"""
		self.weight = w
		self.color = c
		self.mold = 0
		print("Created!")

	def rot(self, days, temp):
		self.mold = days * temp

orange = Orange(6, "orange")
print(orange.mold)
orange.rot = Orange(10, 98)
print(orange.mold)