class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
    3
   / \
  9  20
    /  \
   15   7
"""


def buildTree(inorder, postorder):
    if len(inorder) == 1:
        return [TreeNode(inorder[0])]
    if len(inorder) == 2:
        list = [TreeNode(inorder[1]), TreeNode(inorder[0])]
        list[0].left = list[1]
        return list
    if len(inorder) == 3:
        list = [TreeNode(inorder[1]), TreeNode(inorder[0]), TreeNode(inorder[2])]
        list[0].left = list[1]
        list[0].right = list[2]
        return list
    
    index = inorder.index(postorder[-1])
    list = [inorder[0:index], inorder[index + 1:]]
    left_tree = buildTree(list[0], postorder[0:len(list[0])])
    right_tree = buildTree(list[1], postorder[len(list[0]):-1])
    add_tree = [TreeNode(postorder[-1])]
    add_tree[0].left = left_tree[0]
    add_tree[0].right = right_tree[0]
    add_tree.extend(left_tree)
    add_tree.extend(right_tree)
    return add_tree


def buildTreeCore1(inorder, postorder, instart, inend, postart, poend):
    if instart > inend or postart > poend:
        return None
    val = postorder[poend]
    res = TreeNode(val)
    try:
        flag = inorder.index(postorder[poend])
    except:
        pass
    
    res.left = buildTreeCore(inorder, postorder, instart, flag - 1, postart, postart - instart + flag - 1)
    res.right = buildTreeCore(inorder, postorder, flag + 1, inend, poend - inend + flag, poend - 1)
    return res


def buildTreeCore(inorder, preorder, instart, inend, prstart, prend):
    if instart > inend or prstart > prend:
        return None
    val = preorder[prstart]
    res = TreeNode(val)
    flag = 0
    try:
        flag = inorder.index(preorder[prstart])
    except:
        pass
    
    res.left = buildTreeCore(inorder, preorder, instart, flag - 1, prstart + 1, prstart - instart + flag)
    res.right = buildTreeCore(inorder, preorder, flag + 1, inend, prstart - instart + flag + 1, prend)
    return res


inorder = [9, 3, 15, 20, 7]
postorder = [9, 15, 7, 20, 3]
preorder = [3, 9, 20, 15, 7]

tree = buildTreeCore(inorder, preorder, 0, len(inorder) - 1, 0, len(preorder) - 1)
print("%s" % tree.val)
print("left->%s" % tree.left.val)
print("right->%s" % tree.right.val)
