tree = []
while True:
    try:
        N = int(input())
    except:
        break
    tree.append(N)
    
def postorder(start, end):
    if start > end:
        return
    
    div = end + 1

    for i in range(start+1, end+1):
        if tree[start] < tree[i]:
            div = i
            break

    postorder(start+1, div-1)
    postorder(div, end)
    print(tree[start])

postorder(0, len(tree)-1)


