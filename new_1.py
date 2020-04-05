#- main function
def fill_glasses(desired_level, glasses_capacity):
    state_initial = (0, (0,) * len(glasses_capacity))
    queued_states = set()
    level = 0

    queue_heap = [] # append() and pop(0)
    heappush(queue, (0, state_initial)
    queued_states.add(state_initial[1])

    while queue != []:
        state_current = heappop(queue_heap)
        # visited_states.add(state_current[1])

        if state_current[0] > level:
            level = state_current[0]

        if state_current[1] == desired_level:
            return level

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

                if new_state[1] not in queued_states:
                    queue.append(new_state)
                    queued_states.add(new_state[1])
                    print("fill whole glass. adding state to the queue: ", new_state, "level: ", new_state[0])

            # empty glass
            if state_current[1][i] > 0:
                # state_filled_copy = list.copy(state_filled)
                new_state = (state_current[0]+1, new_tuple(state_current[1], i, 0))
                # print(new_state)
                # state_filled_copy[i] = 0

                if new_state[1] not in queued_states:
                    queue.append(new_state)
                    queued_states.add(new_state[1])
                    print("emptying the glass. adding state to the queue: ", new_state, "level: ", new_state[0])

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
                            print("pouring from glass ", i, "to glass ", j, ". adding state to the queue: ", new_state, "level: ", new_state[0])


        print("set queued states: ", len(queued_states))
        print("queue lenght", len(queue))

    print(desired_level)
    print(queued_states)
    if desired_level in queued_states:
        return level

    else:
        return -1


#-
