class Point:
	x = 0
	y = 0
	pNum = 0
	def init(self, x, y, pNum):
		self.x = x
		self.y = y
		self.pNum = pNum




class Polygon:
	points = []
	nPoints = 0
	def init(self, points):
		for p in points:
			self.points.append(p)
		self.nPoints = len(points)

	def Diagonalie(self, a, b):
		# c = Point()
		# c1 = Point()

		for i in range(len(self.points)):
			if(i!=len(self.points)-1):
				p1 = self.points[i]
				p2 = self.points[i+1]
			else:
				p1 = self.points[i]
				p2 = self.points[0]

			if(p1.pNum != a.pNum and p1.pNum != b.pNum and p2.pNum != a.pNum and p2.pNum != b.pNum and Intersect(a,b,p1,p2)):
				return False
		return True

	def Intersect(self, a, b, p1, p2):
		if(IntersectProp(a, b, p1, p2)):
			return True
		elif (Between(a,b,p1) or Between(a,b,p2) or Between(p1,p2,a) or Between(p1,p2,b)):
			return True
		else:
			return False

	def Between(self, a, b, p):
		if Collinear(a,b,p) is not True:
			return False
		if(a.x != b.x):
			return ((a.x<=p.x) and (p.x<=b.x)) or ((a.x>=p.x) and (p.x>=b.x))
		else:
			return ((a.y<=p.y) and (p.y<=b.y)) or ((a.y>=p.y) and (p.y>=b.y))

	def Collinear(self, a, b, p):
		return Area2(a,b,p)==0

	def Area2(self, a, b, p):
		return (b.x - a.x)*(p.y - a.y) - (p.x - a.x)*(b.y - a.y)

	def IntersectProp(self, a, b, p1, p2):
		if(Collinear(a,b,p1) or Collinear(a,b,p2) or Collinear(p1,p2,a) or Collinear(p1,p2,b)):
			return False
		return Xor(Left(a,b,p1), Left(a,b,p2)) and Xor(Left(p1,p2,a), Left(p1,p2,b))

	def Xor(self, x, y):
		return ~x ^ ~y

	def Left(self, a, b, p):
		return Area2(a,b,p)>0

	def InCone(selft, a, b):








