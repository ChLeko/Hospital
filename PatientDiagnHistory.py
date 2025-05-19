import random
import string
from collections import deque

# Patient Node for the BST
class PatientNode:
    def __init__(self, patient_id, name, diagnosis):
        self.patient_id = patient_id
        self.name = name
        self.diagnosis = diagnosis
        self.left = None
        self.right = None

# Binary Search Tree for storing patient records
class BST:
    def __init__(self):
        self.root = None
    
    # Insert a new patient record
    def insert(self, patient_id, name, diagnosis):
        new_node = PatientNode(patient_id, name, diagnosis)
        if self.root is None:
            self.root = new_node
        else:
            self._insert(self.root, new_node)
    
    def _insert(self, root, new_node):
        if new_node.patient_id < root.patient_id:
            if root.left is None:
                root.left = new_node
            else:
                self._insert(root.left, new_node)
        elif new_node.patient_id > root.patient_id:
            if root.right is None:
                root.right = new_node
            else:
                self._insert(root.right, new_node)

    # Search for a patient record by Patient ID
    def search(self, patient_id):
        return self._search(self.root, patient_id)
    
    def _search(self, root, patient_id):
        if root is None or root.patient_id == patient_id:
            return root
        elif patient_id < root.patient_id:
            return self._search(root.left, patient_id)
        else:
            return self._search(root.right, patient_id)

    # Delete a patient record by Patient ID
    def delete(self, patient_id):
        self.root = self._delete(self.root, patient_id)
    
    def _delete(self, root, patient_id):
        if root is None:
            return root
        if patient_id < root.patient_id:
            root.left = self._delete(root.left, patient_id)
        elif patient_id > root.patient_id:
            root.right = self._delete(root.right, patient_id)
        else:
            # Node to be deleted found
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                min_larger_node = self._min_value_node(root.right)
                root.patient_id, root.name, root.diagnosis = min_larger_node.patient_id, min_larger_node.name, min_larger_node.diagnosis
                root.right = self._delete(root.right, min_larger_node.patient_id)
        return root

    # Helper method to find the node with the minimum value in the right subtree
    def _min_value_node(self, root):
        current = root
        while current.left is not None:
            current = current.left
        return current

    # Inorder traversal (left, root, right)
    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result
    
    def _inorder(self, root, result):
        if root:
            self._inorder(root.left, result)
            result.append((root.patient_id, root.name, root.diagnosis))
            self._inorder(root.right, result)

    # Preorder traversal (root, left, right)
    def preorder(self):
        result = []
        self._preorder(self.root, result)
        return result
    
    def _preorder(self, root, result):
        if root:
            result.append((root.patient_id, root.name, root.diagnosis))
            self._preorder(root.left, result)
            self._preorder(root.right, result)

    # Postorder traversal (left, right, root)
    def postorder(self):
        result = []
        self._postorder(self.root, result)
        return result
    
    def _postorder(self, root, result):
        if root:
            self._postorder(root.left, result)
            self._postorder(root.right, result)
            result.append((root.patient_id, root.name, root.diagnosis))

    # Level-order traversal (BFS)
    def level_order(self):
        result = []
        if self.root is None:
            return result
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            result.append((node.patient_id, node.name, node.diagnosis))
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result

# Generate random patient data
def generate_random_patient():
    patient_id = ''.join(random.choices(string.digits, k=6))
    name = ''.join(random.choices(string.ascii_uppercase, k=5))
    diagnosis = random.choice(["Flu", "Cold", "Covid", "Allergy", "Asthma"])
    return patient_id, name, diagnosis

# Test case to insert 10 random patient records and perform traversals
def test_case():
    bst = BST()

    # Insert 10 random patient records
    for _ in range(10):
        patient_id, name, diagnosis = generate_random_patient()
        bst.insert(patient_id, name, diagnosis)
    
    # Display traversals
    print("Inorder Traversal (Sorted by Patient ID):")
    inorder_result = bst.inorder()
    for patient in inorder_result:
        print(f"ID: {patient[0]}, Name: {patient[1]}, Diagnosis: {patient[2]}")

    print("\nPreorder Traversal:")
    preorder_result = bst.preorder()
    for patient in preorder_result:
        print(f"ID: {patient[0]}, Name: {patient[1]}, Diagnosis: {patient[2]}")

    print("\nPostorder Traversal:")
    postorder_result = bst.postorder()
    for patient in postorder_result:
        print(f"ID: {patient[0]}, Name: {patient[1]}, Diagnosis: {patient[2]}")

    print("\nLevel-order Traversal:")
    level_order_result = bst.level_order()
    for patient in level_order_result:
        print(f"ID: {patient[0]}, Name: {patient[1]}, Diagnosis: {patient[2]}")

# Run the test case
test_case()
