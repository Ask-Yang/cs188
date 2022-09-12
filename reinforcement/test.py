import util

states = [(0,0), (0,1), (0,2)]
predecessors = {states[0]:[]}
state = (0,0)
for next_state in states:
    if next_state not in predecessors:
        predecessors.update({next_state: []})
    predecessors[next_state].append(state)
print()
