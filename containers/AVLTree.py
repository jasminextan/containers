'''
This file implements the AVL Tree data structure.
The functions in this file are considerably harder than the
functions in the BinaryTree and BST files,
but there are fewer of them.
'''

from containers.BinaryTree import BinaryTree, Node
from containers.BST import BST


class AVLTree(BST):
    '''
    FIXME:
    AVLTree is currently not a subclass of BST.
    You should make the necessary changes in the class declaration line above
    and in the constructor below.
    '''

    def __init__(self, xs=None):
        '''
        FIXME:
        Implement this function.
        '''
        super().__init__()

    def balance_factor(self):
        '''
        Returns the balance factor of a tree.
        '''
        return AVLTree._balance_factor(self.root)

    @staticmethod
    def _balance_factor(node):
        '''
        Returns the balance factor of a node.
        '''
        if node is None:
            return 0
        return BinaryTree._height(node.left) - BinaryTree._height(node.right)

    def is_avl_satisfied(self):
        '''
        Returns True if the avl tree satisfies that all nodes
        have a balance factor in [-1,0,1].
        '''
        return AVLTree._is_avl_satisfied(self.root)

    @staticmethod
    def _is_avl_satisfied(node):
        '''
        FIXME:
        Implement this function.
        '''
        if node is None:
            return True
        good = [-1, 0, 1]
        ret = True
        bf = AVLTree._balance_factor(node)
        if bf not in good:
            ret = False
        else:
            if node.left:
                ret &= AVLTree._is_avl_satisfied(node.left)
            if node.right:
                ret &= AVLTree._is_avl_satisfied(node.right)
        return ret

    @staticmethod
    def _left_rotate(node):
        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level overview of tree rotations,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL tree code
        is fairly different from our class hierarchy,
        however, so you will have to adapt their code.
        '''
        new_root = Node(node.right.value)
        print('node 1=', node)
        print('new 1=', new_root)

        t = node.right.left
        print('node 2=', node)
        print('new 2=', new_root)

        new_root.left = Node(node.value)
        print('node 3=', node)
        print('new 3=', new_root)

        new_root.right = node.right.right
        print('node 4=', node)
        print('new 4=', new_root)

        new_root.left.left = node.left
        print('node 5=', node)
        print('new 6=', node)

        new_root.left.right = t
        print('node 6=', node)
        print('new 6=', new_root)

        return new_root

    @staticmethod
    def _right_rotate(node):
        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level overview of tree rotations,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL
        tree code is fairly different from our class hierarchy,
        however, so you will have to adapt their code.
        '''
        new_root = Node(node.left.value)
        print('node 1=', node)
        print('new 1=', new_root)

        # t = new_root.right
        t = node.left.right
        print('node 2=', node)
        print('new 2=', new_root)

        new_root.right = Node(node.value)
        print('node 3=', node)
        print('new 3=', new_root)

        new_root.left = node.left.left
        print('node 4=', node)
        print('new 4=', new_root)

        new_root.right.right = node.right
        print('node 5=', node)
        print('new 5=', new_root)

        new_root.right.left = t
        print('node 6=', node)
        print('new 6=', new_root)

        return new_root

    def insert(self, value):
        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level
        overview of how to insert into an AVL tree,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL
        tree code is fairly different from our class hierarchy,
        however, so you will have to adapt their code.

        HINT:
        It is okay to add @staticmethod helper functions for this code.
        The code should look very similar to the code
        for your insert function for the BST,
        but it will also call the left and right rebalancing functions.
        '''
        if self.root:
            self.root = AVLTree._insert(self.root, value)
        else:
            self.root = Node(value)

    @staticmethod
    def _insert(node, value):
        if node is None:
            return Node(value)
        if value > node.value:
            node.right = AVLTree._insert(node.right, value)
        else:
            node.left = AVLTree._insert(node.left, value)
        if AVLTree._balance_factor(node) < -1:
            if value > node.right.value:
                return AVLTree._left_rotate(node)
            else:
                node.right = AVLTree._right_rotate(node.right)
                return AVLTree._left_rotate(node)
        if AVLTree._balance_factor(node) > 1:
            if value < node.left.value:
                return AVLTree._right_rotate(node)
            else:
                node.left = AVLTree._left_rotate(node.left)
                return AVLTree._right_rotate(node)
        return node

    def insert_list(self, xs):
        if self.root:
            for x in xs:
                self.insert(x)

    @staticmethod
    def _rebalance(node):
        '''
        There are no test cases for the rebalance function,
        so you do not technically have to implement it.
        But both the insert function needs the rebalancing code,
        so I recommend including that code here.
        '''
        if AVLTree._balance_factor(node) < -1:
            if AVLTree._balance_factor(node.right) > 1:
                node.right = AVLTree._right_rotate(node.right)
                return AVLTree._left_rotate(node)
            else:
                return AVLTree._left_rotate(node)
        elif AVLTree._balance_factor(node) > 1:
            if AVLTree._balance_factor(node.left) < 1:
                node.left = AVLTree._left_rotate(node.left)
                return AVLTree._right_rotate(node)
            else:
                return AVLTree._right_rotate(node)
