# 
l1=[8,6,1,None,None,None,5,None,None]
root=construct(l1)
def construct(self, l1):
    if len(l1)==0:
        return None
    val=l1.pop(0)
    if val is None:
        return None
    node=Node(val)
    node.left=construct(l1)
    node.right=construct(l1)
    return node