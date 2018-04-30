from Tkinter import *
import random
from utils import *
import tkFont
import math

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

		# self.loadImage = PhotoImage(file="123.png")
		helv36 = tkFont.Font(family='Helvetica', size=30, weight=tkFont.BOLD)
		self.markPointsButton = Button(self.buttonToolBarFrame, text="Points Generated", command=self.markPointsButtonCallback, activebackground="green", bg="white", font=helv36)
		# self.markPointsButton = Button(self.buttonToolBarFrame, command=self.markPointsButtonCallback, image=self.loadImage, width="200", height="70", bg ="black", bd=0)
		# self.markPointsButton.config(width=200,height=100)
		self.markPointsButton.place(x=100, y=150)

		self.setGuardsButton = Button(self.buttonToolBarFrame, text="Guards Finalised", command=self.setGuardsButtonCallback, activebackground="green", bg="white",font=helv36)
		self.setGuardsButton.place(x=600, y=150)

		self.buildPolygonButton = Button(self.buttonToolBarFrame, text="Build Polygon", command=self.buildPolygonButtonCallback, activebackground="green", bg="white", font=helv36)
		self.buildPolygonButton.place(x=1080, y=150)

		self.ResetButton = Button(self.buttonToolBarFrame, text="Reset Game", command=self.resetButtonCallback, activebackground="green", bg="white", font=helv36)
		self.ResetButton.place(x=1500, y=150)

		self.titleLabel = Label(self.buttonToolBarFrame, text="GUARDING GAME!", font="System 40 bold underline", fg="black", bg="green")
		self.titleLabel.place(x=700, y = 20)

		self.guarderLabel = Label(self.buttonToolBarFrame, text="Guarder", font="System 20 bold", fg="green", bg="black")
		self.guarderLabel.place(x=280, y=20)

		self.polygoniserLabel = Label(self.buttonToolBarFrame, text="Polygoniser", font="System 20 bold", fg="green", bg="black")
		self.polygoniserLabel.place(x=1440, y=20)

		self.resultLabel = Label(self.buttonToolBarFrame, font="System 40 bold", fg="red", bg="black")
		self.resultLabel.place(x=700, y = 300)

		self.numPointsLabel = Label(self.buttonToolBarFrame, font="System 18 bold", fg="green", bg="black")
		self.numPointsLabel.config(text = "# Points = ")
		self.numPointsLabel.place(x=190,y=230)

		self.numGuardsLabel = Label(self.buttonToolBarFrame, font="System 18 bold", fg="green", bg="black")
		self.numGuardsLabel.config(text = "Max # Guards = ")
		self.numGuardsLabel.place(x=670,y=230)
		# self.buttonToolBarFrame.grid(row=1, column=1, sticky="nsew")

		self.root.grid_columnconfigure(0, weight=1, uniform="group1")
		self.root.grid_columnconfigure(1, weight=1, uniform="group1")
		self.root.grid_rowconfigure(0, weight=1)
		self.root.grid_rowconfigure(1, weight=1)

		# G = Guarder()
		# P = Polygoniser()
		

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
			self.numPointsLabel.config(text = "# Points = " + str(len(self.points)))
			self.numGuardsLabel.config(text = "Max # Guards = " + str(int(math.floor(len(self.points)/3))))
		elif (self.isGuardpointsMarked==False):
			p = self.getPoint(event.x, event.y, self.points)
			p1 = self.getPoint(event.x, event.y, self.points1)
			print("Guard X = "+str(p.x)+" Guard Y = "+str(p.y))
			if p is not None:
				self.guards.append(p)
				self.canvas.itemconfigure(p.pointObject, fill='red')
			# if p1 is not None:
			# 	self.canvas1.itemconfigure(p1.pointObject, fill='red')
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
					l1 = self.canvas1.create_line(p.x, p.y, self.markPoint1.x, self.markPoint1.y, fill="red", width=2)
					self.lines.append(l1)
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
		self.markPointsButton.config(bg="green")
		for p in self.points:
			print("X = "+str(p.x)+" Y = "+str(p.y))

	def setGuardsButtonCallback(self):
		self.isGuardpointsMarked = True
		self.setGuardsButton.config(bg="green")
		for p in self.guards:
			print("X = "+str(p.x)+" Y = "+str(p.y))

	def buildPolygonButtonCallback(self):
		self.buildPolygonButton.config(bg="green")
		self.polygonPoints = self.polygonPoints[:-1]
		self.polygon.points = self.polygonPoints
		print("Polygon Coordinates======")
		for p in self.polygon.points:
			print("X = "+str(p.x)+" Y = "+str(p.y))
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
			# print("Guarder Wins!")
			self.resultLabel.config(text="GUARDER WINS!")
		else: self.resultLabel.config(text="POLYGONISER WINS!")
		for i in range(len(self.polygon.points)):
			if self.polygon.flags[i]==1:
				self.canvas1.itemconfigure(self.polygon.points[i].pointObject, fill='yellow')
		for g in self.guards:
			p = p1 = self.getPoint(g.x, g.y, self.points1)
			if p1 is not None:
				self.canvas1.itemconfigure(p1.pointObject, fill='red')
			# print("Polygoniser wins")

	def clearCanvas(self):
		for i in range(len(self.points)):
			self.canvas.delete(self.points[i].pointObject)
			self.canvas1.delete(self.points1[i].pointObject)
		for l in self.lines:
			self.canvas1.delete(l)

	def resetButtonCallback(self):
		self.clearCanvas()
		self.polygon = Polygon()
		self.isPointsGenerated = False
		self.isGuardpointsMarked = False
		self.points = []
		self.points1 = []
		self.guards = []
		self.lines = []
		self.polygonPoints = []
		self.markPoint1 = None
		self.markPointsButton.config(bg="white")
		self.setGuardsButton.config(bg="white")
		self.buildPolygonButton.config(bg="white")
		self.resultLabel.config(text="")
		self.numGuardsLabel.config(text = "Max # Guards = ")
		self.numPointsLabel.config(text = "# Points = ")
		

if __name__ == '__main__':
	g = GuardingGame()
	g.root.title("Guarding Game!")
	g.root.mainloop()
	# x, y = g.getCanvasSize()
	# print(x)
	# print(y)