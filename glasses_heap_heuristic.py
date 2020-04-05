#- imports
import heapq
#- initial functions


#- function heuristic
import numpy as np


def heuristic(state, desired_capacity):
    # print("state", state)
    # print("desired capacity", desired_capacity)
    state_liquid = state[1]
    des_cap_arr = np.array(desired_capacity)

    state_arr = np.array(state_liquid)
    # print(state_liquid)
    # print(des_cap_arr)
    sum_state = np.sum(state_arr)
    sub_des = np.sum(des_cap_arr)

    diff = sum_state - sub_des
    absolute = np.absolute(diff)
    # sum_ = np.sum(absolute)
    # print("heuristic: ", absolute)
    return absolute
# dfsdfs
#-

#- function heuristic
import numpy as np


def heuristic2(state, desired_capacity):
    # print("state", state)
    # print("desired capacity", desired_capacity)
    state_liquid = state[1]
    des_cap_arr = np.array(desired_capacity)

    state_arr = np.array(state_liquid)
    # print(state_liquid)
    # print(des_cap_arr)

    diff = des_cap_arr - state_arr
    absolute = np.absolute(diff)
    sum_ = np.sum(absolute)
    print("heuristic: ", sum_)
    return sum_
# dfsdfs
#-

h = []
heapq.heappush(h, (5, 'write code'))
heapq.heappush(h, (7, 'release product'))
heapq.heappush(h, (1, 'write spec'))
heapq.heappush(h, (3, 'create tests'))
print(heapq.heappop(h))
print(heapq.heappop(h))
print(heapq.heappop(h))
print(heapq.heappop(h))

if h == []:
    print("heap empty")
print(h)

#-

heur1 = heuristic(list1, desired_capacity)
# 30
heur2 = heuristic(list2, desired_capacity)
# 4
heur3 = heuristic(list3, desired_capacity)
# 106
print(heur1)
print(heur2)
print(heur3)
print("dupa")

#-

import numpy as np

desired_capacity = (0, 3, 5, 22)

list1 = ((0), (0, 0, 0, 0))
list2 = ((0), (0, 3, 3, 20))
list3 = ((0), (31, 33, 35, 37))

list1_ar = np.array(list1)
list2_ar = np.array(list2)
list3_ar = np.array(list3)

desired_ar = np.array(desired_capacity)

result1 = desired_ar - list1_ar
result2 = desired_ar - list2_ar
result3 = desired_ar - list3_ar

abs_res1 = np.absolute(result1)
abs_res2 = np.absolute(result2)
abs_res3 = np.absolute(result3)

sum_res1 = np.sum(abs_res1)
sum_res2 = np.sum(abs_res2)
sum_res3 = np.sum(abs_res3)

print(sum_res1)
print(sum_res2)
print(sum_res3)

# print(result1)
#-
print("dupa")


#- Tuple update
def new_tuple(tuple_, i, change):
    tpl = tuple_[:i] + (change,) + tuple_[i + 1:]
    return tpl


# print(tpl)
#-

#- print content glasses
def print_content_glasses(state_filled, desired_level, glasses_capacity):
    return_string = ""
    ch = 'A'

    for i in range(len(glasses_capacity)):
        return_string += ch + ": " + str(state_filled[i]) + "/" + str(desired_level[i]) + "/" + str(
            glasses_capacity[i]) + "  "
        ch = chr(ord(ch) + 1)

    print(return_string)


#-
glasses_capacity = [10, 20]
desired_level = [5, 10]
glasses_filled = [0, 1]
print_content_glasses(glasses_filled, desired_level, glasses_capacity)


#- main function
def fill_glasses(desired_level, glasses_capacity):
    state_initial = (0, (0,) * len(glasses_capacity))
    queued_states = set()
    level = 0
    visited_states = 0
    queue_heap = []  # append() and pop(0)
    heapq.heapify(queue_heap)

    heapq.heappush(queue_heap, (0, state_initial))
    # print(queue_heap)
    queued_states.add(state_initial[1])

    while queue_heap != []:
        state_ = heapq.heappop(queue_heap)
        state_current = state_[1]
        visited_states += 1
        # print("visited states ", visited_states)
        # print()
        # print("restarting while loop. current heap state ", state_current, "heuristic :", state_[0])
        # visited_states.add(state_current[1])


        level = state_current[0]

        if state_current[1] == desired_level:
            print("returning level", level)
            return level

        # print("visiting state: ", state_current[1], "level: ", state_current[0])

        for i in range(len(glasses_capacity)):

            # pour glass full
            if state_current[1][i] < glasses_capacity[i]:
                # print(state_current[i], glasses_capacity[i])

                # state_filled_copy = new_tuple.copy(state_filled)
                capacity = glasses_capacity[i]
                new_state = (state_current[0] + 1, new_tuple(state_current[1], i, capacity))
                # print("new state", new_state)
                # state_filled_copy[i] = glasses_capacity[i]
                # print("new state", new_state)

                if new_state[1] not in queued_states:
                    value_heuristic = heuristic(new_state, desired_level)# heappush(h, (3, 'create tests'))
                    new_state_with_heuristic = (value_heuristic, new_state)
                    # print("new state with heuristic :", new_state_with_heuristic)
                    heapq.heappush(queue_heap, new_state_with_heuristic)
                    queued_states.add(new_state[1])
                    # print("fill whole glass. adding state to the queue: ", new_state, "level: ", new_state[0])

            # empty glass
            if state_current[1][i] > 0:
                # state_filled_copy = list.copy(state_filled)
                new_state = (state_current[0] + 1, new_tuple(state_current[1], i, 0))
                # print(new_state)
                # state_filled_copy[i] = 0

                if new_state[1] not in queued_states:

                    value_heuristic = heuristic(new_state, desired_level)# heappush(h, (3, 'create tests'))
                    new_state_with_heuristic = (value_heuristic, new_state)
                    # print("new state with heuristic :", new_state_with_heuristic)
                    heapq.heappush(queue_heap, new_state_with_heuristic)

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

                        new_state = (state_current[0] + 1, new_tuple(state_current[1], i, state_current[1][i] - difference))
                        # print("pouring out ", new_state)
                        new_state = (new_state[0], new_tuple(new_state[1], j, state_current[1][j] + difference))
                        # print("pouring in ", new_state)
                        # print("new state", new_state)
                        # state_filled_copy[i] = glasses_capacity[i]

                        if new_state[1] not in queued_states:

                            value_heuristic = heuristic(new_state, desired_level)# heappush(h, (3, 'create tests'))
                            new_state_with_heuristic = (value_heuristic, new_state)
                            # print("new state with heuristic :", new_state_with_heuristic)
                            heapq.heappush(queue_heap, new_state_with_heuristic)
                            queued_states.add(new_state[1])
                            # print("pouring from glass ", i, "to glass ", j, ". adding state to the queue: ", new_state, "level: ", new_state[0])

        # print("set queued states: ", len(queued_states))
        # print("heap_queue lenght", len(queue_heap))

        if len(queued_states) < 5:
            print("queued states set ", queued_states)
            print("queue heap: ", queue_heap)
        
    if desired_level in queued_states:
        print(level)
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
sdf
#-


#- Test 1
test_capacity = (10, 20)
test_desired = (0, 10)

# 2

# glasses_filled = (0,1)
fill_glasses(test_desired, test_capacity)

#- Test 1
test_capacity = (10, 40, 40)
test_desired = (10, 30, 40)
# glasses_filled = (0,1)
fill_glasses(test_desired, test_capacity)

# 3

#- Test 3
test_capacity = (31, 33, 35, 37)
test_desired = (0, 3, 5, 22)
# glasses_filled = (0,1)
fill_glasses(test_desired, test_capacity)

# 41 kroków

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
