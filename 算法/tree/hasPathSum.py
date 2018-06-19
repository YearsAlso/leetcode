class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
"""
def hasPathSumCore(root):
    if root.left == None and root.right == None:
        return [root.val]
    list = []
    if (root.left != None):
        left_tree = hasPathSumCore(root.left)
        i = 0
        while i<len(left_tree):
            left_tree[i]+=root.val
            i+=1
        list.extend(left_tree)

    if (root.right != None):
        right_tree = hasPathSumCore(root.right)
        i = 0
        while i < len(right_tree):
            right_tree[i] += root.val
            i += 1
        list.extend(right_tree)
    return list

def hasPathSum(root, sum):
    """
    :type root: TreeNode
    :type sum: int
    :rtype: bool
    """
    tree = []
    tree = hasPathSumCore(root)
    for value in tree:
        if value == sum:
            return True
    return False


test = [5,4,8,11,None,13,4,7,2,None,None,None,1]
tree_list=[]

for value in test:
    if value != None:
        tree_list.append(TreeNode(value))

tree_list[0].left = tree_list[1]
tree_list[0].right = tree_list[2]
tree_list[1].left = tree_list[3]
tree_list[3].left = tree_list[6]
tree_list[3].right = tree_list[7]
tree_list[2].left = tree_list[4]
tree_list[2].right = tree_list[5]
tree_list[5].right = tree_list[8]

print(hasPathSum(tree_list[0],22))