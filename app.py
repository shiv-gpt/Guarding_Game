from Tkinter import *
import random
from utils import *


class SuperVisor:
	polygon = Polygon()
	isMarked = False
	def AddPoint(self, x, y):
		P = Point()
		P.x = x
		P.y = y
		P.pNum = len(self.polygon.points)
		self.polygon.points.append(P)
	# def generateRandomPoints(self, width, height):



class Guarder:
	polygon = Polygon()
	guardPointNumber = 0
	def setGuardPointNumber(self, x):
		self.guardPointNumber = x

	def copyFromSuperVisor(self, S):
		self.polygon.points = S.polygon.points
		self.polygon.guards = S.polygon.guards
		self.polygon.nPoints = S.polygon.nPoints

	def getPoint(self, x, y):
		for p in self.polygon.points:
			if x >= (p.x - 5) and x <= (p.x + 5):
				return p
		return None

	def markGuardPoint(self, p):
		if p is not None and p.isGuardPoint is False:
			p.isGuardPoint = True
			self.polygon.guards.append(p)

class Polygoniser:
	polygon = Polygon()
	# def 



class GuardingGame(Tk):
	polygon = Polygon()
	isPointsGenerated = False
	isGuardpointsMarked = False
	points = []
	points1 = []
	guards = []
	lines = []
	polygonPoints = []
	markPoint1 = None
	# markPoint2 = None
	def __init__(self, *args, **kwargs):
		# tk.Tk.__init__(self, *args, **kwargs)

		self.root = Tk()
		self.root.geometry("1920x1080")
		
		self.frame = Frame(self.root, bd=0, bg="white")
		self.canvas = Canvas(self.frame, bg="white")
		self.canvas.pack(expand=1,fill=BOTH)
		self.canvas.configure(cursor="crosshair")
		self.canvas.bind("<Button-1>", self.point)
		self.frame.grid(row=0,column=0,sticky="nsew")
		

		self.frame1 = Frame(self.root, bd = 0, bg="white")
		self.canvas1 = Canvas(self.frame1, bg="white")
		self.canvas1.pack(expand=1,fill=BOTH)
		self.canvas1.configure(cursor="mouse")
		self.canvas1.bind("<Button-1>", self.point1)
		self.frame1.grid(row=0, column=1, sticky="nsew")
		
		self.buttonToolBarFrame = Frame(self.root, bd=0, bg="black")
		self.buttonToolBarFrame.grid(row=1, columnspan=2, sticky="nsew")

		self.markPointsButton = Button(self.buttonToolBarFrame, text="Generate Points", command=self.markPointsButtonCallback)
		self.markPointsButton.place(x=50, y=70)

		self.setGuardsButton = Button(self.buttonToolBarFrame, text="Finalise Guards", command=self.setGuardsButtonCallback)
		self.setGuardsButton.place(x=300, y=70)

		self.buildPolygonButton = Button(self.buttonToolBarFrame, text="Build Polygon", command=self.buildPolygonButtonCallback)
		self.buildPolygonButton.place(x=550, y=70)

		# self.buttonToolBarFrame.grid(row=1, column=1, sticky="nsew")

		self.root.grid_columnconfigure(0, weight=1, uniform="group1")
		self.root.grid_columnconfigure(1, weight=1, uniform="group1")
		self.root.grid_rowconfigure(0, weight=1)
		self.root.grid_rowconfigure(1, weight=1)

		G = Guarder()
		P = Polygoniser()
		

	def point(self, event):
		if(self.isPointsGenerated==False):
			o = self.canvas.create_oval(event.x-5, event.y-5, event.x+5, event.y+5, fill='black')
			o1 = self.canvas1.create_oval(event.x-5, event.y-5, event.x+5, event.y+5, fill='black')

			p = Point()
			p.x = event.x
			p.y = event.y
			p.pNum = len(self.points)
			p.isGuard = False
			p.isGuardPoint = False
			p.pointObject = o
			self.points.append(p)

			p1 = Point()
			p1.x = event.x
			p1.y = event.y
			p1.pNum = len(self.points1)
			p1.isGuard = False
			p1.isGuardPoint = False
			p1.pointObject = o1
			self.points1.append(p1)
		elif (self.isGuardpointsMarked==False):
			p = self.getPoint(event.x, event.y, self.points)
			print("Guard X = "+str(p.x)+" Guard Y = "+str(p.y))
			if p is not None:
				self.guards.append(p)
				self.canvas.itemconfigure(p.pointObject, fill='red')
		# self.canvas.itemconfigure(p, fill='black')
		# points.append(event.x)
		# points.append(event.y)
		# print(event.x)
		# print(event.y)

	def point1(self, event):
		if(self.isPointsGenerated==True and self.isGuardpointsMarked == True):
			p = self.getPoint(event.x, event.y, self.points1)
			if p is not None:
				if self.markPoint1 is None:
					self.markPoint1 = p
				else:
					# self.make_line(p, markPoint1)
					l1 = self.canvas1.create_line(p.x, p.y, self.markPoint1.x, self.markPoint1.y, fill="red")
					self.markPoint1 = p
				self.polygonPoints.append(p)
		# self.canvas1.create_oval(event.x, event.y, event.x+1, event.y+1, fill="red", width="10.0")
		# # points.append(event.x)
		# # points.append(event.y)
		# print(event.x)
		# print(event.y)
		# return points

	def getCanvasSize(self):
		# assert self.canvas.winfo_width == self.canvas1.winfo_width
		# assert self.canvas.winfo_height == self.canvas1.winfo_height
		print(self.canvas.winfo_width())
		print(self.canvas1.winfo_width())
		print(self.canvas.winfo_height())
		print(self.canvas1.winfo_height())
		return self.canvas.winfo_width, self.canvas.winfo_height

	def getPoint(self, x, y, P):
		for p in P:
			if x >= (p.x - 5) and x <= (p.x + 5) and y>= (p.y - 5) and y<=(p.y + 5):
				return p
		return None

	def markPointsButtonCallback(self):
		self.isPointsGenerated = True
		for p in self.points:
			print("X = "+str(p.x)+" Y = "+str(p.y))

	def setGuardsButtonCallback(self):
		self.isGuardpointsMarked = True
		for p in self.guards:
			print("X = "+str(p.x)+" Y = "+str(p.y))

	def buildPolygonButtonCallback(self):
		self.polygonPoints = self.polygonPoints[:-1]
		self.polygon.points = self.polygonPoints
		self.polygon.guards = self.guards
		for g in self.polygon.guards:
			for p in self.polygon.points:
				if g.pNum == p.pNum:
					p.isGuard = True
					print("In loop")
					print("X = "+str(p.x)+" Y = "+str(p.y)) 
		for p in self.polygon.points:
			if p.pNum == True:
				print("X = "+str(p.x)+" Y = "+str(p.y)) 
		if(self.polygon.isGuarded()==True):
			print("Guarder Wins!")
		else: print("Polygoniser wins")
			# def check_lin)e()





		# self.root = tk.Tk(6666666666666666666666666)
		# self.root.title("Guarding Game!")
		# self.root.resizable(900,900)
		# self.canvas1 = tk.Canvas(self.root, width = 300, height=300)
		# self.canvas1.configure(cursor="crosshair")
		# self.canvas1.pack()
		# self.canvas1.bind()
		# self.root.mainloop()

if __name__ == '__main__':
	g = GuardingGame()
	g.root.title("Guarding Game!")
	g.root.mainloop()
	x, y = g.getCanvasSize()
	print(x)
	print(y)