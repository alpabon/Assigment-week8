class DoctorNode:
    def __init__ (self, name):
        self.name = name
        self.right = None
        self.left = None
        



class DoctorTree:
    def __init__(self):
        self.root = None

    def insert(self, Doctor, name, side, current_node=None):
        if self.root is None:
            return
        
        if current_node is None:
            current_node = self.root

        if current_node.name == name:
            print(f"Doctor {name} already exists in the tree.")
            return True
        if side not in ["left", "right"]:
            print("Side must be 'left' or 'right'.")
            return
        if current_node.name == Doctor:
            if side == "left":
                if current_node.left is None:
                    current_node.left = DoctorNode(name)
                    print(f"Doctor {name} added to the left of {Doctor}")
                else:
                    print(f"Doctor {Doctor} already has a left doctor.")
                    
                return True
            elif side == "right":
                if current_node.right is None:
                    current_node.right = DoctorNode(name)
                    print(f"Doctor {name} added to the right of {Doctor}")
                else:
                    print(f"Doctor {Doctor} already has a {side} doctor.") 
                return True
            
        found_left= False
        found_right= False

        if current_node.left:
            found_left =self.insert(Doctor, name, side, current_node.left)

        if current_node.right: 
            found_right =self.insert(Doctor,name, side, current_node.right)
        
        if not(found_left or found_right):
            if current_node == self.root:
                print(f"Doctor {Doctor} not found in the tree.")
            return False
        return True
    def preorder(self, node):
        if node is None:
            return []
        result = [node.name]
        result += self.preorder(node.left)
        result += self.preorder(node.right)
        return result 
    def inorder(self,node):
        if node is None:
            return []
        result = []
        result += self.inorder (node.left)
        result.append(node.name)
        result += self.inorder (node.right)
        return result
    def postorder(self,node):
        if node is None:
            return []
        result = []
        result += self.postorder (node.left)
        result += self.postorder (node.right)
        result.append(node.name)
        return result 
tree = DoctorTree()

tree.root = DoctorNode("Dr. Croft") 
# Insert values
tree.insert("Dr. Croft", "Dr. Goldsmith", "right") 
tree.insert("Dr. Croft", "Dr. Phan", "left")
tree.insert("Dr. Phan", "Dr. Carson", "right") 
tree.insert("Dr. Phan", "Dr. Morgan", "left")
            
print(tree.preorder(tree.root)) # ["Dr. Croft", "Dr. Phan", "Dr. Morgan", "Dr. Carson", "Dr. Goldsmith"]
print(tree.inorder(tree.root)) # ["Dr. Morgan", "Dr. Phan", "Dr. Carson", "Dr. Croft", "Dr. Goldsmith"]
print(tree.postorder(tree.root)) # ["Dr. Morgan", "Dr. Carson", "Dr. Phan", "Dr. Goldsmith", "Dr. Croft"]        
        




# Test your DoctorTree and DoctorNode classes here
