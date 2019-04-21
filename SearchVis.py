from graphics import *
from queue import *
import random
import copy

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

class PriorityNode(object):
	def __init__(self, priority, node):
		self.priority = priority
		self.node = node
		
	def __lt__(self, other):
		return self.priority < other.priority		
			
class NodeGrid:
	def __init__(total_rows, total_cols, win, start_pos=(0,0), end_pos = None, blocks=0):
		self.rows = total_rows
		self.cols = total_cols
		self.nodes = [VisNode(r, c) for c in range(total_cols) for r in range(total_rows)]
		if (blocks > 0):
			pass #self.make_blocks(blocks)
		if end_pos is None:
			end_pos = (self.rows-1, self.cols-1)
		self.start_node = self.nodes[start_pos[0] + self.rows*start_pos[1]]
		self.end_node = self.nodes[end_pos[0] + self.rows*end_pos[1]]
		
	def make_blocks(blocks):
		for i in range(blocks):
			r = random.randrange(0,total_rows)
			c = random.randrange(0,total_cols)
			n = nodes[r + total_rows*c]
			if (n is not start_node and n is not end_node):
				n.setColor("black")
				n.visited = True

		
def perform_search(nodes, priority_funct, start_pos = (2,10), end_pos = (6,3), sleep_time = .01, blocks = 0):
	start_node = nodes[start_pos[0] + total_rows*start_pos[1]]
	start_node.setColor("red")
	start_node.visited = True
	end_node = nodes[end_pos[0] + total_rows*end_pos[1]]
	end_node.setColor("green")
	
	for i in range(blocks):
		r = random.randrange(0,total_rows)
		c = random.randrange(0,total_cols)
		n = nodes[r + total_rows*c]
		if (n is not start_node and n is not end_node):
			n.setColor("black")
			n.visited = True
			
	q = PriorityQueue()
	q.put(PriorityNode(0,start_node))
	red = 255
	green = 0
	blue = 255
	nodes_visited = 0
	while(not q.empty()):
		cur_node = q.get().node
		
		if (cur_node == end_node):
			end_node.setColor(color_rgb(100,255,100))
			break
		
		cur_node.setColor(color_rgb(int(red),int(green),int(blue)))
		red = red*.995
		blue = blue*.995
		for r,c in ((cur_node.row, cur_node.col-1), (cur_node.row, cur_node.col+1), (cur_node.row-1, cur_node.col), (cur_node.row+1, cur_node.col)): 
			if (r >= 0 and c >= 0 and r < total_rows and c < total_cols):
				add_node = nodes[r + total_rows*c]
				if (not add_node.visited):
					add_node.visited = True
					nodes_visited += 1
					if (add_node != end_node):
						add_node.setColor(color_rgb(220,255,220))
					else: 
						add_node.setColor(color_rgb(30,180,30))
					
					add_node_priority = priority_funct(start_node, end_node, nodes_visited, add_node)
					q.put(PriorityNode(add_node_priority, add_node))

		if (sleep_time > 0):
			time.sleep(sleep_time)	

def greedy_priority(start_node, end_node, nodes_visited, add_node):
	return abs(end_node.row-add_node.row)+abs(end_node.col-add_node.col)

def bfs_priority(start_node, end_node, nodes_visited, add_node):
	return nodes_visited

def dfs_priority(start_node, end_node, nodes_visited, add_node):
	return total_rows*total_cols-nodes_visited
			
if __name__ == "__main__":
	total_rows = 20
	total_cols = 20
	win = GraphWin("Search Visualization", total_rows*node_width+1, total_cols*node_height+1)
	
	key_val = None
	while (key_val != "x"):	
		nodes = [VisNode(r, c) for c in range(total_cols) for r in range(total_rows)]
		for node in nodes:
			node.draw(win)
			
		perform_search(nodes, greedy_priority, start_pos = (17,17), blocks=0)
	
		key_val = win.getKey()
		if (key_val != "x"):
			for node in nodes:
				node.undraw()
		
	win.close()
	
	