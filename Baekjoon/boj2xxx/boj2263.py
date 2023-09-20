import sys
sys.setrecursionlimit(10**7)
n = int(input())
inorder = [*map(int, input().split())]
postorder = [*map(int, input().split())]
postindex = [0 for _ in range(n + 1)]
inindex = [0 for _ in range(n + 1)]
preorder = []
for i in range(n):
    postindex[postorder[i]] = i
    inindex[inorder[i]] = i


def pre(root, minlimit, maxlimit):
    preorder.append(inorder[root])
    if minlimit == maxlimit:
        return
    lefts, rights = root - minlimit, maxlimit - root
    postrootind = postindex[inorder[root]]
    if lefts == 0:
        rightroot = inindex[postorder[postrootind - 1]]
        pre(rightroot, root + 1, maxlimit)
    elif rights == 0:
        leftroot = inindex[postorder[postrootind - 1 - rights]]
        pre(leftroot, minlimit, root - 1)
    else:
        leftroot = inindex[postorder[postrootind - 1 - rights]]
        pre(leftroot, minlimit, root - 1)
        rightroot = inindex[postorder[postrootind - 1]]
        pre(rightroot, root + 1, maxlimit)


pre(inindex[postorder[-1]], 0, n - 1)
print(*preorder)
