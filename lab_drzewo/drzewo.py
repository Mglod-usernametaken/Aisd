from typing import Any, List

class TreeNode:
    value: Any
    children: List['TreeNode']

    def __init__(self, value=None):
        self.value = value
        self.children = []

    def __str__(self):
        return self.value

    def is_leaf(self, branch)-> bool:
        if branch.children == []:
            return True
        else:
            return False

    # def add(self, child: TreeNode)-> None:

    # def for_each_deep_first
    # def for_each_level_order
    # def search


class Tree:
    root: TreeNode

# todo
    def __init__(self, root: TreeNode):
        self.root = root

    def add(self, new: TreeNode, parrent: TreeNode)->None:
        parrent.children.append(new)


# def for_each_level_order
#     def for_each_deep_first(visit: Callable[['TreeNode'], None]):

# show


f = TreeNode('F')
b = TreeNode('B')
g = TreeNode('G')
drz = Tree(f)
print(drz.root.is_leaf(f))
 
drz.add(b, f)
drz.add(g, b)

print(drz.root.is_leaf(f))
print(f.children)





#
# def look(node):
#     for x in node.children:
#         look(node)
#     print(node)