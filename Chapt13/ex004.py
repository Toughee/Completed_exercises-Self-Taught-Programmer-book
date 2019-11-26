# Public Variables

class PublicPrivateExamples:
	def __init__(self):
		self.public = "safe"
		self.unsafe = "unsafe"


	def public_method(self):
		# clients can use this
		pass


	def _unsafe_method(self):
		# clients shouldn't use thos
		pass
