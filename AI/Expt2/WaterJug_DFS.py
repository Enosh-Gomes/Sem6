from math import gcd

def water_jug_dfs(jug1_capacity,jug2_capacity, target):
    visited = set()
    all_paths = []
    def dfs(jug1, jug2, path):
        if jug1 == target or jug2 == target:
            all_paths.append(path + [(jug1, jug2)])
            return
        state = (jug1, jug2)
        if state in visited:
            return
        visited.add(state)
        rules = [
            (jug1_capacity, jug2),
            (jug1, jug2_capacity),
            (0, jug2),
            (jug1, 0),
            (max(0, jug1 - (jug2_capacity - jug2)),min(jug2_capacity, jug1 + jug2)),
            (min(jug1_capacity, jug1 + jug2),max(0, jug2 - (jug1_capacity - jug1)))
        ]
        for next_state in rules:
            dfs(next_state[0], next_state[1], path + [state])
    dfs(0, 0, [])
    return all_paths if all_paths else None

def get_data():
    jug1_cap, jug2_cap = map(int, input("Enter capacities of Jugs (in litres): ").split())
    target = int(input("Enter the target amount (in litres): "))
    if target > max(jug1_cap, jug2_cap) or target % gcd(jug1_cap, jug2_cap) != 0:
        print("\nNo solution possible with given capacities.")
        return None
    return jug1_cap, jug2_cap, target

if __name__ == "__main__":
    data = get_data()
    if not data:
        exit()
    jug1_cap, jug2_cap, target = data
    
    if target > max(jug1_cap, jug2_cap) or target % gcd(jug1_cap, jug2_cap) != 0:
        print("\nNo solution possible with given capacities.")
    else:
        result = water_jug_dfs(jug1_cap, jug2_cap, target)
        if result:
            print(f"\nSolution(s) found using Depth-First Search for target {target} litre with jug capacities {jug1_cap} litre and {jug2_cap} litre:")
            for path_num, path in enumerate(result, start=1):
                print(f"\nPath of Solution {path_num}:")
                print("-"*30)
                for step, state in enumerate(path):
                    print(f"Step{step:2d} => Jug 1:{state[0]:2d}L, Jug 2:{state[1]:2d}L")
                print("-"*30)
            print(f"\nTotal Solutions Found: {len(result)}")