## Initial file
#-
set1 = {((0), (1,2,3,4)), ((1), (2,3,4,5))}

for set_ in set1:
    print(set_[1])

print(set1)

state_initial = (0, (0,) * 5)
print(state_initial)
#-
init = (0, (0,) * 8)
print(init)

print(init[0])
state_initial = (0, (0,) * 5)

print(state_initial)

#- main function
def fill_glasses(desired_level, glasses_capacity):
    state_initial = (0, (0,) * len(glasses_capacity))
    visited_states = set()
    level = 0

    queue = [] # append() and pop(0)
    queue.append(state_initial)

    while queue != []:
        state_current = queue.pop(0)
        visited_states.add(state_current[1])

        if state_current[0] > level:
            level = state_current[0]

        print("visiting state: ", state_current[1], "level: ", state_current[0])

        for i in range(len(glasses_capacity)):

            # pour glass full
            if state_current[1][i] < glasses_capacity[i]:
                # print(state_current[i], glasses_capacity[i])

                # state_filled_copy = new_tuple.copy(state_filled)
                capacity = glasses_capacity[i]
                new_state = (state_current[0]+1, new_tuple(state_current[1], i, capacity))
                # print("new state", new_state)
                # state_filled_copy[i] = glasses_capacity[i]

                if new_state[1] not in visited_states:
                    queue.append(new_state)
                    print("fill whole glass. adding state to the queue: ", new_state, "level: ", new_state[0])

            # empty glass
            if state_current[1][i] > 0:
                # state_filled_copy = list.copy(state_filled)
                new_state = (state_current[0]+1, new_tuple(state_current[1], i, 0))
                # print(new_state)
                # state_filled_copy[i] = 0

                if new_state[1] not in visited_states:
                    queue.append(new_state)
                    print("empty glass. adding state to the queue: ", new_state, "level: ", new_state[0])

            # pour from one glass to another
            if state_current[1][i] > 0:

                other_glasses = list(range(len(glasses_capacity)))
                other_glasses.remove(i)
                for j in other_glasses:
                    if state_current[1][j] < glasses_capacity[j]:
                        # print(state_current[i], glasses_capacity[i])

                        # state_filled_copy = new_tuple.copy(state_filled)
                        difference_newglass = glasses_capacity[j] - state_current[1][j]
                        difference = min(state_current[1][i], difference_newglass)
                        # print("difference", difference)

                        new_state = (state_current[0]+1, new_tuple(state_current[1], i, state_current[1][i]-difference))
                        # print("pouring out ", new_state)
                        new_state = (new_state[0], new_tuple(new_state[1], j, state_current[1][j]+difference))
                        # print("pouring in ", new_state)
                        # print("new state", new_state)
                        # state_filled_copy[i] = glasses_capacity[i]

                        if new_state[1] not in visited_states:
                            queue.append(new_state)
                            print("pouring from glass ", i, "to glass ", j, ". adding state to the queue: ", new_state)

        if desired_level in visited_states:
            return desired_level, level
            
                    # print(i, " ", other_glasses)
    print(visited_states)

    if desired_level in visited_states:
        return 1

    else:
        return False

#-



#- Test 1
test_capacity = (10,20)
test_desired = (0, 10)
# glasses_filled = (0,1)
fill_glasses(test_desired, test_capacity)

#- Test 1
test_capacity = (10, 40, 40)
test_desired = (10, 30, 40)
# glasses_filled = (0,1)
fill_glasses(test_desired, test_capacity)



#- print content glasses
def print_content_glasses(state_filled, desired_level, glasses_capacity):
    return_string = ""
    ch = 'A'


    for i in range(len(glasses_capacity)):
        return_string += ch + ": " + str(state_filled[i]) + "/" + str(desired_level[i]) + "/" + str(glasses_capacity[i]) + "  "
        ch= chr(ord(ch) + 1)

    print(return_string)
#-
glasses_capacity = [10,20]
desired_level = [5, 10]
glasses_filled = [0,1]
print_content_glasses(glasses_filled, desired_level, glasses_capacity)

#- Tuple update
def new_tuple(tuple_, i, change):
    tpl = tuple_[:i] + (change,) + tuple_[i+1:]
    return tpl



#-
#- Tuple update
tuple_ = (0,0)
tpl = tuple_[:0] + (5,) + tuple_[0+1:]

print(tpl)
#-

print(new_tuple((0,0,0), 2, 3))

#-
t = (0,) * 8
print(t)

#-

new_tuple((0,0), 0, 5)

#-
