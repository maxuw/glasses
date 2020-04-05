#- initial functions

#- Tuple update
def new_tuple(tuple_, i, change):
    tpl = tuple_[:i] + (change,) + tuple_[i+1:]
    return tpl

# print(tpl)
#-

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




#- main function
def fill_glasses(desired_level, glasses_capacity):
    state_initial = (0, (0,) * len(glasses_capacity))
    queued_states = set()
    level = 0
    visited_states = 0

    queue = [] # append() and pop(0)
    queue.append(state_initial)
    queued_states.add(state_initial[1])

    while queue != []:
        state_current = queue.pop(0)
        visited_states += 1
        # visited_states.add(state_current[1])

        if state_current[0] > level:
            level = state_current[0]

        if state_current[1] == desired_level:
            return level

        # print("visiting state: ", state_current[1], "level: ", state_current[0])

        for i in range(len(glasses_capacity)):

            # pour glass full
            if state_current[1][i] < glasses_capacity[i]:
                # print(state_current[i], glasses_capacity[i])

                # state_filled_copy = new_tuple.copy(state_filled)
                capacity = glasses_capacity[i]
                new_state = (state_current[0]+1, new_tuple(state_current[1], i, capacity))
                # print("new state", new_state)
                # state_filled_copy[i] = glasses_capacity[i]

                if new_state[1] not in queued_states:
                    queue.append(new_state)
                    queued_states.add(new_state[1])
                    # print("fill whole glass. adding state to the queue: ", new_state, "level: ", new_state[0])

            # empty glass
            if state_current[1][i] > 0:
                # state_filled_copy = list.copy(state_filled)
                new_state = (state_current[0]+1, new_tuple(state_current[1], i, 0))
                # print(new_state)
                # state_filled_copy[i] = 0

                if new_state[1] not in queued_states:
                    queue.append(new_state)
                    queued_states.add(new_state[1])
                    # print("emptying the glass. adding state to the queue: ", new_state, "level: ", new_state[0])

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

                        if new_state[1] not in queued_states:
                            queue.append(new_state)
                            queued_states.add(new_state[1])
                            # print("pouring from glass ", i, "to glass ", j, ". adding state to the queue: ", new_state, "level: ", new_state[0])


        print("set queued states: ", len(queued_states))
        print("queue lenght", len(queue))


        # if desired_level in queued_states:
        #     return level

                    # print(i, " ", other_glasses)
    print(desired_level)
    print(queued_states)
    if desired_level in queued_states:
        return level

    else:
        return -1


#-


#-

#- Reading standard in
import sys
lines = []

for line in sys.stdin:
    if 'Exit' == line.rstrip():
        break
    lines.append(line)
    # print(f'Processing Message from sys.stdin *****{line}*****')
    # dupa()

    if len(lines) >= 3:

        glasses_amount = int(lines[0])
        glasses_capacity = tuple([int(i) for i in lines[1].split()])
        glasses_desired = tuple([int(i) for i in lines[2].split()])
        # tup_cut = tuple([int(i) for i in str_list[0].split()])


        # print(glasses_capacity)
        result = fill_glasses(glasses_desired, glasses_capacity)
        print(result)
        # print(type(lines[0]))        print(lines[0])
        lines = []



#-
# 3
# 12 8 3
# 1 0 0
print("dupa")
#-


#- Test 1
test_capacity = (10,20)
test_desired = (0, 10)

# 2

# glasses_filled = (0,1)
fill_glasses(test_desired, test_capacity)

#- Test 1
test_capacity = (10, 40, 40)
test_desired = (10, 30, 40)
# glasses_filled = (0,1)
fill_glasses(test_desired, test_capacity)

#3

#- Test 3
test_capacity = (31, 33, 35, 37)
test_desired = (0, 3, 5, 22)
# glasses_filled = (0,1)
fill_glasses(test_desired, test_capacity)

#41 kroków

#-
str_list = []
string1 = "1 2 3 4"
str_list.append("1 2 3 4")

cut = string1.split()
cut_int = [int(i) for i in string1.split()]
tup_cut = tuple([int(i) for i in str_list[0].split()])

print("dupa")
print(cut_int)
print(tup_cut)
#-




#-
