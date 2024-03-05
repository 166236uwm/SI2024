from heapq import heappush, heappop

def heuristic(state, goal_state):
    # Heurystyka: suma odległości bloku miasta (city block distance)
    h_value = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != ' ':
                row_goal, col_goal = find_goal_position(state[i][j], goal_state)
                h_value += abs(i - row_goal) + abs(j - col_goal)
    return h_value

def find_goal_position(value, goal_state):
    for i in range(3):
        for j in range(3):
            if goal_state[i][j] == value:
                return i, j
def astar_search(initial_state, goal_state):
    priority_queue = [(heuristic(initial_state, goal_state), 0, initial_state, [])]

    while priority_queue:
        _, cost, current_state, actions = heappop(priority_queue)

        if current_state == goal_state:
            print("Osiągnięto cel!")
            print("Sekwencja akcji:", actions)
            break

        zero_row, zero_col = find_zero_position(current_state)

        for action in possible_actions(zero_row, zero_col):
            new_state = apply_action(current_state, zero_row, zero_col, action)
            new_cost = cost + 1
            priority = new_cost + heuristic(new_state, goal_state)
            new_actions = actions + [action]

            heappush(priority_queue, (priority, new_cost, new_state, new_actions))

def find_zero_position(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == ' ':
                return i, j

def possible_actions(row, col):
    actions = []
    if row > 0:
        actions.append('up')
    if row < 2:
        actions.append('down')
    if col > 0:
        actions.append('left')
    if col < 2:
        actions.append('right')
    return actions

def apply_action(state, row, col, action):
    new_state = [list(row) for row in state]
    if action == 'up':
        new_state[row][col], new_state[row - 1][col] = new_state[row - 1][col], new_state[row][col]
    elif action == 'down':
        new_state[row][col], new_state[row + 1][col] = new_state[row + 1][col], new_state[row][col]
    elif action == 'left':
        new_state[row][col], new_state[row][col - 1] = new_state[row][col - 1], new_state[row][col]
    elif action == 'right':
        new_state[row][col], new_state[row][col + 1] = new_state[row][col + 1], new_state[row][col]
    return tuple(tuple(row) for row in new_state)

# Stan początkowy i docelowy w formie krotek
initial_state = (
    (' ', '1', '3'),
    ('4', '2', '5'),
    ('7', '6', '8')
)

goal_state = (
    ('1', '2', '3'),
    ('4', '5', '6'),
    ('7', '8', ' ')
)

astar_search(initial_state, goal_state)
