from enum import Enum

class EdgeType(Enum):
	directed = 1
	undirected =2 


from typing import Any
class Vertex:
	data: Any
	index: int


from typing import Optional
class Edge:
	source: Vertex
	destination: Vertex
	weight: Optional[float]


from typing import Dict, List
class Graph:
	adjacencies: Dict[Vertex, List[Edge]]
	
	def create_vertex(self, data:Any)-> Vertex:
		pass
	
	def add_directed_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None)->None:
		pass

	def add_undirected_edge(self, source:Vertex, destination: Vertex, weight: Optional[float] = None)->None:
		pass

	def traverse_breadth_first(self, visit:Callable[[Any], None])->None:
		pass

	def traverse_depth_first(self, visit:Callable[[Any], None])->None:
		pass

	def show():
		pass
	
