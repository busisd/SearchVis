from graphics import *
from queue import *
import random

node_width = 20
node_height = 20
		
class VisNode:
	def __init__(self, row, col):
		self.row = row
		self.col = col
		self.visited = False
		self.vis_rect = Rectangle(Point(row*node_width,col*node_height), Point((row+1)*node_width,(col+1)*node_height))
		self.vis_rect.setOutline("black")
		self.vis_rect.setFill("white")
		
	def draw(self, win):
		self.vis_rect.draw(win)

	def undraw(self):
		self.vis_rect.undraw()
		
	def setColor(self, color):
		self.vis_rect.setFill(color)	
	
def BFS(nodes, start_pos = (2,10), end_pos = (6,3), sleep_time = .01, blocks=0):
	startNode = nodes[start_pos[0] + total_rows*start_pos[1]]
	startNode.setColor("red")
	startNode.visited = True
	endNode = nodes[end_pos[0] + total_rows*end_pos[1]]
	endNode.setColor("green")
	
	for i in range(blocks):
		r = random.randrange(0,total_rows)
		c = random.randrange(0,total_cols)
		n = nodes[r + total_rows*c]
		if (n is not startNode and n is not endNode):
			n.setColor("black")
			n.visited = True
	
	q = SimpleQueue()
	q.put(startNode)
	red = 255
	green = 0
	blue = 255
	while(not q.empty()):
		cur_node = q.get()
		
		if (cur_node == endNode):
			endNode.setColor(color_rgb(100,255,100))
			break
		
		cur_node.setColor(color_rgb(int(red),int(green),int(blue)))
		red = red*.995
		blue = blue*.995
		for r,c in ((cur_node.row, cur_node.col-1), (cur_node.row, cur_node.col+1), (cur_node.row-1, cur_node.col), (cur_node.row+1, cur_node.col)): 
			if (r >= 0 and c >= 0 and r < total_rows and c < total_cols):
				add_node = nodes[r + total_rows*c]
				if (not add_node.visited):
					add_node.visited = True
					if (add_node != endNode):
						add_node.setColor(color_rgb(220,255,220))
					else: 
						add_node.setColor(color_rgb(30,180,30))
						
					q.put(add_node)
		if (sleep_time > 0):
			time.sleep(sleep_time)
						
def DFS(nodes, start_pos = (2,10), end_pos = (6,3), sleep_time = .01, blocks=0):
	startNode = nodes[start_pos[0] + total_rows*start_pos[1]]
	startNode.setColor("red")
	startNode.visited = True
	endNode = nodes[end_pos[0] + total_rows*end_pos[1]]
	endNode.setColor("green")
	
	for i in range(blocks):
		r = random.randrange(0,total_rows)
		c = random.randrange(0,total_cols)
		n = nodes[r + total_rows*c]
		if (n is not startNode and n is not endNode):
			n.setColor("black")
			n.visited = True
	
	q = LifoQueue()
	q.put(startNode)
	red = 255
	green = 0
	blue = 255
	while(not q.empty()):
		cur_node = q.get()
		
		if (cur_node == endNode):
			endNode.setColor(color_rgb(100,255,100))
			break
		
		cur_node.setColor(color_rgb(int(red),int(green),int(blue)))
		red = red*.995
		blue = blue*.995
		for r,c in ((cur_node.row, cur_node.col-1), (cur_node.row, cur_node.col+1), (cur_node.row-1, cur_node.col), (cur_node.row+1, cur_node.col)): 
			if (r >= 0 and c >= 0 and r < total_rows and c < total_cols):
				add_node = nodes[r + total_rows*c]
				if (not add_node.visited):
					add_node.visited = True
					if (add_node != endNode):
						add_node.setColor(color_rgb(220,255,220))
					else: 
						add_node.setColor(color_rgb(30,180,30))
						
					q.put(add_node)
		if (sleep_time > 0):
			time.sleep(sleep_time)

class PriorityNode(object):
	def __init__(self, priority, node):
		self.priority = priority
		self.node = node
		
	def __lt__(self, other):
		return self.priority < other.priority		
			
def Greedy(nodes, start_pos = (2,10), end_pos = (6,3), sleep_time = .01, blocks = 0):
	startNode = nodes[start_pos[0] + total_rows*start_pos[1]]
	startNode.setColor("red")
	startNode.visited = True
	endNode = nodes[end_pos[0] + total_rows*end_pos[1]]
	endNode.setColor("green")
	
	for i in range(blocks):
		r = random.randrange(0,total_rows)
		c = random.randrange(0,total_cols)
		n = nodes[r + total_rows*c]
		if (n is not startNode and n is not endNode):
			n.setColor("black")
			n.visited = True
			
	q = PriorityQueue()
	q.put(PriorityNode(0,startNode))
	red = 255
	green = 0
	blue = 255
	while(not q.empty()):
		cur_node = q.get().node
		
		if (cur_node == endNode):
			endNode.setColor(color_rgb(100,255,100))
			break
		
		cur_node.setColor(color_rgb(int(red),int(green),int(blue)))
		red = red*.995
		blue = blue*.995
		for r,c in ((cur_node.row, cur_node.col-1), (cur_node.row, cur_node.col+1), (cur_node.row-1, cur_node.col), (cur_node.row+1, cur_node.col)): 
			if (r >= 0 and c >= 0 and r < total_rows and c < total_cols):
				add_node = nodes[r + total_rows*c]
				if (not add_node.visited):
					add_node.visited = True
					if (add_node != endNode):
						add_node.setColor(color_rgb(220,255,220))
					else: 
						add_node.setColor(color_rgb(30,180,30))
					
					add_node_dist = abs(endNode.row-add_node.row)+abs(endNode.col-add_node.col)
					q.put(PriorityNode(add_node_dist, add_node))

		if (sleep_time > 0):
			time.sleep(sleep_time)

			
			
if __name__ == "__main__":
	key_val = None
	total_rows = 20
	total_cols = 20
	win = GraphWin("Search Visualization", total_rows*node_width+1, total_cols*node_height+1)
	
	while (key_val != "x"):	
		nodes = [VisNode(r, c) for c in range(total_cols) for r in range(total_rows)]
		for node in nodes:
			node.draw(win)
			
		Greedy(nodes, start_pos = (17,17), blocks=150)
	
		key_val = win.getKey()
		if (key_val != "x"):
			for node in nodes:
				node.undraw()
		
	win.close()
	
	