class Point:
	x = 0
	y = 0
	pNum = 0
	isGuard = False
	isGuardPoint = False
	pointObject = None
	def init(self, x, y, pNum):
		self.x = x
		self.y = y
		self.pNum = pNum
	def setGuardFlag(self):
		self.isGuard = True

class Line:
	point1 = None
	point2 = None
	lineObject = None

class Polygon:
	points = []
	guards = []
	nPoints = 0
	def init(self, points):
		for p in points:
			self.points.append(p)
		self.nPoints = len(points)

	def getNextPoint(self, p):
		# if(p.pNum == self.nPoints - 1):
		# 	return self.points[0]
		# else:
		# 	return self.points[p.pNum+1]
		j = -1
		for i in range(len(self.points)):
			if self.points[i].pNum == p.pNum:
				j = i
				break
		assert j != -1
		if j == len(self.points) - 1:
			return self.points[0]
		else: return self.points[j+1]




	def getPrevPoint(self, p):
		# if(p.pNum == 0):
		# 	return self.points[self.nPoints-1]
		# else:
		# 	return self.points[p.pNum-1]
		j = -1
		for i in range(len(self.points)):
			if self.points[i].pNum == p.pNum:
				j = i
				break
		assert j != -1
		if j == 0:
			return self.points[len(self.points) - 1]
		else: return self.points[j-1]

	def Diagonalie(self, a, b):
		# c = Point()
		# c1 = Point()

		for i in range(len(self.points)):
			if(i!=(len(self.points)-1)):
				p1 = self.points[i]
				p2 = self.points[i+1]
			else:
				p1 = self.points[i]
				p2 = self.points[0]

			if(p1.pNum != a.pNum and p2.pNum != a.pNum and p1.pNum != b.pNum and p2.pNum != b.pNum and self.Intersect(a,b,p1,p2)):
				return False
		return True

	def Intersect(self, a, b, p1, p2):
		if(self.IntersectProp(a, b, p1, p2) == True):
			return True
		elif (self.Between(a,b,p1) or self.Between(a,b,p2) or self.Between(p1,p2,a) or self.Between(p1,p2,b)):
			return True
		else:
			return False

	def Between(self, a, b, p):
		if self.Collinear(a,b,p) == False:
			return False
		if(a.x != b.x):
			return (((a.x<=p.x) and (p.x<=b.x)) or ((a.x>=p.x) and (p.x>=b.x)))
		else:
			return (((a.y<=p.y) and (p.y<=b.y)) or ((a.y>=p.y) and (p.y>=b.y)))

	def Collinear(self, a, b, p):
		return self.Area2(a,b,p)==0

	def Area2(self, a, b, p):
		# print(a.x)
		return (b.x - a.x)*(p.y - a.y) - (p.x - a.x)*(b.y - a.y)

	def IntersectProp(self, a, b, p1, p2):
		if(self.Collinear(a,b,p1) or self.Collinear(a,b,p2) or self.Collinear(p1,p2,a) or self.Collinear(p1,p2,b)):
			return False
		return self.Xor(self.Left(a,b,p1), self.Left(a,b,p2)) and self.Xor(self.Left(p1,p2,a), self.Left(p1,p2,b))

	def Xor(self, x, y):
		return x^y
		# return (not x) ^ (not y)

	def Left(self, a, b, p):
		return self.Area2(a,b,p)>0

	def LeftOn(self, a, b, p):
		return self.Area2(a,b,p)>=0


	#the points in the points list are inserted in a particular order, Either counter clockwise or clockwise
	def InCone(self, a, b):
		# a1 = Point()
		# a0 = Point()
		a1 = self.getNextPoint(a)
		a0 = self.getPrevPoint(a)
		if (self.LeftOn(a,a1,a0)==True):
			return (self.Left(a,b,a0) and self.Left(b,a,a1))
		else:
			return not(self.LeftOn(a,b,a1) and self.LeftOn(b,a,a0))

	def Diagonal(self,a,b):
		print("******************************************************")
		print("a coordinates = ")
		print("X = "+str(a.x)+" Y = "+str(a.y))
		print("b coordinates = ")
		print("X = "+str(b.x)+" Y = "+str(b.y))
		result = self.InCone(a,b) and self.InCone(b,a) and self.Diagonalie(a,b)
		print("result = " + str(result))
		print("-------------------------------------------------------")
		return result

	def getIndex(self, p):
		j = -1
		for i in range(len(self.points)):
			if self.points[i].pNum == p.pNum:
				j = i
				break
		assert j != -1
		return j

	def isGuarded(self):
		flags = [0 for p in self.points]
		print("#############################")
		for p in self.points:
			print("p coordinates = ")
			print("X = "+str(p.x)+" Y = "+str(p.y))
			if p.isGuard == True:
				j = self.getIndex(p)
				flags[j] = 1


				# flags[p.pNum] = 1
		print("#############################")
		# flags = [0 if p.isGuard is not True else 1 for p in self.points]
		print(flags)
		print("")
		print("")
		print("")
		for g in self.guards:
			for p in self.points:
				if p.isGuard == False:
					if self.Diagonal(g,p) == True:
						j = self.getIndex(p)
						# p.isGuard = True
						flags[j] = 1
						# flags[p.pNum] = 1
		for g in self.guards:
			print("Guard Index = " + str(self.getIndex(g)))
			p1 = self.getNextPoint(g)
			p2 = self.getPrevPoint(g)
			j1 = self.getIndex(p1)
			print("NextPointIndex = " + str(j1))
			j2 = self.getIndex(p2)
			print("PrevPointIndex = " + str(j2))
			flags[j1] = 1
			flags[j2] = 1
		print(flags)
		if 0 in flags:
			return False
		else: return True

	# def isPolygon(self):










