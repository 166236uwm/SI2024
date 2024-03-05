from collections import deque

def is_goal_state(state):
    return state['A'] == 'clean' and state['B'] == 'clean'

def breadth_first_search():
    initial_state = {'agent_location': 'A', 'A': 'dirty', 'B': 'dirty'}
    queue = deque([(initial_state, [])])

    while queue:
        current_state, actions = queue.popleft()

        if is_goal_state(current_state):
            print("Osiągnięto cel!")
            print("Sekwencja akcji:", actions)
            break

        left_result = apply_action(current_state, 'left')
        left_actions = actions + ['left']
        queue.append((left_result, left_actions))

        right_result = apply_action(current_state, 'right')
        right_actions = actions + ['right']
        queue.append((right_result, right_actions))

        suck_result = apply_action(current_state, 'suck')
        suck_actions = actions + ['suck']
        queue.append((suck_result, suck_actions))

def apply_action(state, action):
    new_state = state.copy()

    if action == 'left':
        new_state['agent_location'] = 'A'
    elif action == 'right':
        new_state['agent_location'] = 'B'
    elif action == 'suck':
        new_state[new_state['agent_location']] = 'clean'

    return new_state

breadth_first_search()
