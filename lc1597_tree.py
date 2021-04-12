class Solution:
    def expTree(self, s):
        op_pr = {"+":2, "-": 2, "*":1, "/":1, "(":3, ")":2}
        node_stack, op_stack = [], []
        for c in s:
            if c.isdigit():
                node_stack.append(Node(c))
            elif c == '(':
                op_stack.append(c)
            else:
                while op_stack and op_pr[c] >= op_pr[op_stack[-1]]:
                    temp = Node(op_stack.pop(), right = node_stack.pop())
                    temp.left = node_stack.pop()
                    node_stack.append(temp)
                if c == ')': op_stack.pop()
                else:
                    op_stack.append(c)
        while op_stack:
            temp = Node(op_stack.pop(), right = node_stack.pop())
            temp.left = node_stack.pop()
            node_stack.append(temp)
        return node_stack.pop()
