# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec(object):
    def __init__(self):
        pass
    
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        que = [root]
        str_req = ""
        while (que):
            node = que.pop(0)
            if node.left != None:
                que.append(node.left )
            elif node.right!=None:
                que.append(TreeNode('*'))
                
            if node.right !=None:
                que.append(node.right)
            elif node.left!=None: #r=N l!=N
                que.append(TreeNode('*'))

            if node.val == '*':
                str_req += "null,"
            else:
                str_req += str(node.val)+","
        return str_req[:-1]
    
    
    def deserializeCore(self,data):
        if len(data) == 0:
            return None
        val = data.pop(0)
        if val == "null":
            return None
        else:
            tree = TreeNode(int(val))
            tree.left = self.deserializeCore(data)
            tree.right = self.deserializeCore(data)
            return tree
    
    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        #print(data.split(','))
        return self.deserializeCore(data.split(','))


def main():
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    
    node1.left = node2
    node1.right = node3
    
    node2.left = None
    node2.right = node4
    
    node3.left = node5
    node3.right = node6
    codec = Codec()

    
    node = codec.deserialize("1,2,3,4,null,6,7")
    print(codec.serialize(node))

if __name__ == '__main__':
    main()
