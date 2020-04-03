## Initial file
#-
init = (0) * 8
print(init)



#- main function
def fill_glasses(desired_level, glasses_capacity):
    state_initial = (0,) * len(glasses_capacity)
    visited_states = set()

    queue = [] # append() and pop(0)
    queue.append(state_initial)

    while queue != []:
        state_current = queue.pop(0)
        visited_states.add(state_current)
        print("visiting state: ", state_current)

        for i in range(len(glasses_capacity)):

            # pour glass full
            if state_current[i] < glasses_capacity[i]:
                # print(state_current[i], glasses_capacity[i])

                # state_filled_copy = new_tuple.copy(state_filled)
                capacity = glasses_capacity[i]
                new_state = new_tuple(state_current, i, capacity)
                # print("new state", new_state)
                # state_filled_copy[i] = glasses_capacity[i]

                if new_state not in visited_states:
                    queue.append(new_state)
                    print("fill whole glass. adding state to the queue: ", new_state)

            # empty glass
            if state_current[i] > 0:
                # state_filled_copy = list.copy(state_filled)
                new_state = new_tuple(state_current, i, 0)
                # print(new_state)
                # state_filled_copy[i] = 0

                if new_state not in visited_states:
                    queue.append(new_state)
                    print("empty glass. adding state to the queue: ", new_state)

            # other_glasses

    if desired_level in visited_states:
        return 1

    else:
        return False

#- Test 1
test_capacity = (10,20)
test_desired = (0, 10)
# glasses_filled = (0,1)
fill_glasses(test_desired, test_capacity)

#- Test 1
test_capacity = (10,20,40)
test_desired = (10, 10, 40)
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
