from math import sqrt, floor

# check if a number is prime
def prime(n) -> bool:
    if n == 2 or n == 3: 
        return True

    elif n == 1 or n % 2 == 0 or n % 3 == 0: 
        return False
        
    elif n == 0: return False
    
    else:
        k = 5
        t = sqrt(n)
        tmp = floor(t)
        
        while k <= tmp:
            if n % k == 0 or n % (k + 2) == 0:
                return False
            k += 6
                
    return True

# check if a number is super prime
def super_prime(n) -> bool:
    
    if not prime(n): 
        return False
        
    elif prime(n) == True:
        digits = [int(s) for s in str(n)]
        
    for digit in digits:
        
        if prime(digit) == True:
            return True

        elif not prime(digit):
            return False

# chuyển số la mã thành số nguyên
def covert_roman_to_int(s: str) -> int:
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0

    for i in range(len(s) - 1):

        if roman[s[i]] < roman[s[i + 1]]:
            result -= roman[s[i]]
        else:
            result += roman[s[i]]

    return result + roman[s[-1]]
    
# tìm một char trong str
def find_funique_char(text: str) -> int:
    for index, char in enumerate(text):
        if text.count(char) == 1:
            return index
    return -1

# kiểm tra số đối xứng 
def isPalindrome(x: int) -> bool: 

    x_to_str = str(x)

    if x_to_str == x_to_str[::-1]:
        return True
    else:
        return False
    
# xóa các số trùng lặp trong list
def remove_duplicate(nums: list[int]) -> int:
    store = 0

    for num in range(1, len(nums)):

        if nums[store] != nums[num]:
            store += 1

            nums[store] = nums[num]

    return store + 1 

# xóa element được chỉ định trong list
def remove_ele( nums: list[int], val: int) -> int:

    # var để theo dõi số lượng phần tử không bằng  val
    k = 0

    for inter in range(len(nums)):
        if nums[inter] != val:
            # nếu num hiện tại không bằng val
            # di chuyển phần tử hiện tại đến pos tiếp theo
            nums[k] = nums[inter]
            k += 1
            
    return k

# tìm số được chỉ định trong list
def search_insert(nums: list[int], target: int) -> int:
    left, right = 0 , len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
            
        elif nums[mid] < target:
            left = mid + 1
            
        else:
            right = mid - 1
            
    return left

# kiểm tra các bracket hợp lệ trong str
def isValid(store: str) -> bool:

    stack = []
    bracket = {'(': ')', '[': ']', '{': '}'}

    for char in store:
        
        if char in bracket.keys():
            stack.append(char)
            
        elif char in bracket.values():

            if not stack or bracket[stack.pop()] != char:
                return False
                
        else:
            return False
        
    return len(stack) == 0

# kiểm tra số đối xứng
def is_perfect_num(n: int) -> bool:

    sums = 0

    for num in range(1, n//2 + 1):

        if n & num == 0:
            sums += num

    if sums == n:
        return True

    return False

# check time running code
import time 
def run_code():
    start = time.time()

    for i in range(1000000):
        pass

    end = time.time()

    return 'time running file: ' + str(round(end - start,1))

    