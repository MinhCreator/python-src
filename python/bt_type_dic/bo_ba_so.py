"""<<<<<<<<<<<<<<  ✨ Codeium Command 🌟 >>>>>>>>>>>>>>>>"""

def tmp(lst: list):

    """init and defind variable"""
    maxs = 0
    f = [0] * (len(lst)+ 1)
    p = [0] * (len(lst) + 1)

    """process"""
    for i in range(1, len(lst)):

        f[i] = max(f[i - 1], lst[i - 1])
        # print(f[i])
        
    for i in range(len(lst) - 2, 1, -1):

        p[i] = max(p[i + 1], lst[i + 1])
        # print(p[i])

    for i in range(2, len(lst) - 1):
        maxs = max(maxs, (2 * f[i]) - (3 * lst[i]) + (5 * p[i]))
        # print(maxs)
    
    return maxs

""" part made test case for function"""
# import unittest
# 
# 
# class TestTmp(unittest.TestCase):
    # def test_tmp(self):
        # self.assertEqual(tmp([3, 5, 2, 6, 4, 5 ,7]), 39)
        # self.assertEqual(tmp([3, 5, 2, 6, 4]), 12)
        # self.assertEqual(tmp([3, 5, 2, 6, 4, 5, 7, 8, 9]), 33)
# 
# if __name__ == '__main__':
    # unittest.main()

# print(tmp([3, 5, 2, 6, 4, 5 ,7]))
print(tmp([3, 5, 2, 6]))
