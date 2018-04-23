from Tkinter import *
import random
from utils import *


class SuperVisor():
	polygon = Polygon()
	isMarked = False
	def AddPoint(self, x, y):
		P = Point()
		P.x = x
		P.y = y
		P.pNum = len(self.polygon.points)
		self.polygon.points.append(P)
	# def generateRandomPoints()

class Guarder():
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


	# def 



class GuardingGame(Tk):

	def __init__(self, *args, **kwargs):
		# tk.Tk.__init__(self, *args, **kwargs)

		self.root = Tk()
		self.root.geometry("1920x1080")
		
		self.frame = Frame(self.root, bd=0, bg="black")
		self.canvas = Canvas(self.frame, bg="red")
		self.canvas.pack(expand=1,fill=BOTH)
		self.canvas.configure(cursor="crosshair")
		self.canvas.bind("<Button-1>", self.point)
		self.frame.grid(row=0,column=0,sticky="nsew")
		

		self.frame1 = Frame(self.root, bd = 0, bg="blue")
		self.canvas1 = Canvas(self.frame1, bg="green")
		self.canvas1.pack(expand=1,fill=BOTH)
		self.canvas1.configure(cursor="mouse")
		self.canvas1.bind("<Button-1>", self.point1)
		self.frame1.grid(row=0, column=1, sticky="nsew")
		
		self.buttonToolBarFrame = Frame(self.root, bd=0, bg="yellow")
		self.buttonToolBarFrame.grid(row=1, columnspan=2, sticky="nsew")

		self.markPointsButton = Button(self.buttonToolBarFrame, text="Mark Points")
		self.markPointsButton.place(x=50, y=70)

		self.setGuardsButton = Button(self.buttonToolBarFrame, text="Finalise Guards")
		self.setGuardsButton.place(x=300, y=70)

		self.buildPolygonButton = Button(self.buttonToolBarFrame, text="Build Polygon")
		self.buildPolygonButton.place(x=550, y=70)

		# self.buttonToolBarFrame.grid(row=1, column=1, sticky="nsew")

		self.root.grid_columnconfigure(0, weight=1, uniform="group1")
		self.root.grid_columnconfigure(1, weight=1, uniform="group1")
		self.root.grid_rowconfigure(0, weight=1)
		self.root.grid_rowconfigure(1, weight=1)

	def point(self, event):
		self.canvas.create_oval(event.x, event.y, event.x, event.y, fill="white", width="10.0")
		# points.append(event.x)
		# points.append(event.y)
		print(event.x)
		print(event.y)

	def point1(self, event):
		self.canvas1.create_oval(event.x, event.y, event.x+1, event.y+1, fill="black", width="10.0")
		# points.append(event.x)
		# points.append(event.y)
		print(event.x)
		print(event.y)
		# return points







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