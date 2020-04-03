## Initial file
#-




#-

#- print content glasses
def print_content_glasses(glasses_filled, glasses_limit):
    return_string = ""
    ch = 'A'


    for i in range(len(glasses_limit)):
        return_string += ch + ": " + str(glasses_filled[i]) + "/" + str(glasses_limit[i]) + "  "
        ch= chr(ord(ch) + 1)

    print(return_string)
#-
glasses_limit = [1,2]
glasses_filled = [0,1]
print_content_glasses(glasses_filled, glasses_limit)

#-
