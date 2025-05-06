class Note:
    def __init__(self, first, last):
        self.first = first
        self.last = last

def main():
    n = int(input())
    A = []
    F = []

    def Enter():
        nonlocal A
        for i in range(n):
            first, last = map(int, input().split())
            A.append(Note(first, last))

    def mergeSort(arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = mergeSort(arr[:mid])
        right = mergeSort(arr[mid:])
        return merge(left, right)

    def merge(left, right):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i].last < right[j].last:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def dynamicProgramming():
        nonlocal F
        F = [1] * n

        for i in range(1, n):
            for j in range(i):
                if A[j].last < A[i].first and F[i] < F[j] + 1:
                    F[i] = F[j] + 1

    def printMaxNonOverlappingNotes():
        print(max(F))

    Enter()
    A = mergeSort(A)
    dynamicProgramming()
    printMaxNonOverlappingNotes()

if __name__ == "__main__":
    main()