class TreeNode:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left  # 左子树
        self.right = right  # 右子树


node1 = TreeNode("A", TreeNode("B", TreeNode("D"), TreeNode("E")),
                 TreeNode("C", TreeNode("F"), TreeNode("G")))


def bfs(root):
    h = height(root)
    for i in range(1, h + 1):
        givenOrder(root, i)


def givenOrder(node, level):
    if node:
        if level == 1:
            print(node.value)
        else:
            givenOrder(node.left, level - 1)
            givenOrder(node.right, level - 1)


def height(root):
    if not root:
        return 0
    return max(height(root.left), height(root.right)) + 1


def preTraverse(root):
    if root:
        print(root.value)
        preTraverse(root.left)
        preTraverse(root.right)


def recursive(root):
    if root:
        l = [root]
        while l:
            for _ in range(len(l)):
                r = l.pop(0)
                if r.left:
                    l.append(r.left)
                if r.right:
                    l.append(r.right)
                print(r.value)

if __name__ == '__main__':
    # preTraverse(node1)
    # print(height(node1))
    # bfs(node1)
    recursive(node1)