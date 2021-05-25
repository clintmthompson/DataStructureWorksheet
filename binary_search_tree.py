class TreeNode:
    def __init__(self, value):
        self.value = value
        self.right_child = None
        self.left_child = None

    def insert(self, data):
        if self.value == data:
            return False
        elif self.value > data:
            if self.left_child:
                return self.left_child.insert(data)
            else:
                self.left_child = TreeNode(data)
                return True
        else:
            if self.right_child:
                return self.right_child.insert(data)
            else:
                self.right_child = TreeNode(data)
                return True

    def find(self, data):
        if self.value == data:
            print(f"This tree contains the number {data}, thanks for asking.")
            return True
        elif self.value > data:
            if self.left_child:
                return self.left_child.find(data)
            else:
                print(f"I'm afraid this tree doesn't contain the number {data}, sorry chump.")
                return False
        else:
            if self.right_child:
                return self.right_child.find(data)
            else:
                return False


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = TreeNode(data)
            return True

    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False
