#coding=utf-8

class Food():
	def __init__(self, name=u'Unknown Food'):
		self.name = name

	def __str__(self):
		return u'[%s]' % self.name
		
class Employee():
	def __init__(self, name=u'Unknown Employee'):
		self.name = name

	def __str__(self):
		return u'[%s]' % self.name

	def takeOrder(self, food):
		return Food(food)

class Customer():
	def __init__(self, name=u'Unknown Customer'):
		self.name = name
		
	def __str__(self):
		return u'[%s]' % self.name

	def placeOrder(self, emp):
		pass


if __name__ == '__main__':
	pass
	