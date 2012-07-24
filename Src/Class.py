class Student:
	name = ''

	#constructor
	def __init__(self,name = 'daniel'):
		self.name = name

	#
	def __del__(self):
		pass

	def say(self):
		print(self.name)

s = Student('tony')
s.say();