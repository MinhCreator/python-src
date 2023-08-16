import math

def is_prime(Int):

    if  Int == 2 or Int == 3:
        return True
    elif Int % 2 == 0 or Int % 3 == 0:
        return False
    else:
        step_k = 5
        can_bac = math.sqrt(Int)    
        lam_tron_xuong = math.floor(can_bac)
        while step_k <= lam_tron_xuong:
            if Int % step_k == 0 or Int % (step_k + 2) == 0:
                return False
            step_k += 6
    return True
    

def is_postive_and_prime_position(lst):
    num_pos = []
    position_num = []
    for i in range(0, len(lst)):
        if lst[i] > 0 and is_prime(lst[i]) == True:
            num_pos.append(lst[i])
            position_num.append(i)
    return 'số dương và là số nguyên tố: ' + str(num_pos) + '\n' + 'vị trí của các số đó: ' + str(position_num)


lst = [2,4,5,7,3,8,9,11,13,14,15,12]

print(is_postive_and_prime_position(lst))


