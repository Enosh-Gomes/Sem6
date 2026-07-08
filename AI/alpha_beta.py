from math import inf

def alphabeta(node, alpha, beta, tree, evals, depth=0):
    indent = "  " * depth
    children = tree.get(node, [])
    a = -inf
    b = inf

    if not children:
        if node not in evals:
            print(f"{indent}Terminal {node} has no value! Defaulting to 0.")
            return 0
        print(f"{indent}Terminal {node} = {evals[node]}")
        return evals[node]

    is_max = (depth % 2 == 0)

    if is_max:
        print(f"{indent}MAX node {node} (a={_f(alpha)}, b={_f(beta)})")
        for child in children:
            child_val = alphabeta(child, alpha, b, tree, evals, depth + 1)
            a = max(a, child_val)
            alpha = max(alpha, a)
            print(f"{indent}  a updated to {_f(a)}")
            if alpha >= beta:
                print(f"{indent}  >> b-pruning")
                break
        return alpha
    else:
        print(f"{indent}MIN node {node} (a={_f(alpha)}, b={_f(beta)})")
        for child in children:
            child_val = alphabeta(child, a, beta, tree, evals, depth + 1)
            b = min(b, child_val)
            beta = min(beta, b)
            print(f"{indent}  b updated to {_f(b)}")
            if alpha >= beta:
                print(f"{indent}  >> a-pruning")
                break
        return beta

def _f(v):
    if v == inf: return "+inf"
    if v == -inf: return "-inf"
    return str(v)

if __name__ == "__main__":
    print("Alpha-Beta Pruning")
    print("==================")
    print("PASTE your entire tree below. Type 'done' on a new line when finished.")
    print("Format -> Parent Child1 Child2 ...")
    print("Format -> Leaf Value\n")

    tree = {}
    evals = {}
    root = None

    while True:
        try:
            line = input().strip()
        except EOFError:
            break

        if not line:
            continue
        if line.lower() == "done":
            break

        parts = line.split(maxsplit=1)

        if len(parts) < 2:
            continue

        node = parts[0]
        rest = parts[1]

        if root is None:
            root = node

        try:
            val = int(rest.strip())
            evals[node] = val
            tree[node] = []
        except ValueError:
            children = rest.replace(',', ' ').split()
            tree[node] = children

    print("\n--- Starting Alpha-Beta Search ---\n")
    if root:
        result = alphabeta(root, -inf, inf, tree, evals)
        print(f"\nFinal Result: {result}")
    else:
        print("No tree data entered.")

'''
A B C
B D E
D H I
H P Q
I R S
E J K
J T U
K V W
C F G
F L M
L X Y
G N D
P 10
Q 7
R 8
S 9
T 12
U 11
V 12
W 5
X 8
Y 9
M 8
N 11
O 5
done
'''

'''
A B C D
B E F
C G H I
D J K
E L M
F N O
G P Q
H R S
I T U
J V W
K X Y
L 10
M 7
N 8
O 9
P 12
Q 11
R 12
S 5
T 8
U 9
V 8
W 12
X 7
Y 10
done
'''