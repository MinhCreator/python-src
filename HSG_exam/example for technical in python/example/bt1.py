def mutiple(a,b):
    
    tmp = [str(num) for num in range(2000, 3201) if num % a == 0 and num % b != 0]

    return ", ".join(tmp)

print(mutiple(7, 5))