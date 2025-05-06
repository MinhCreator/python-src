# Program Duplication
# This program is written in Pascal and it reads a list of notes, sorts them, and then calculates the maximum number of notes that can be played without overlapping.

# Define a record type Note with two fields: first and last
class Note:
    def __init__(self, first, last):
        self.first = first
        self.last = last

# Define the main function
def main():
    # Read the number of notes
    n = int(input())
    # Create an array A to store the notes
    A = [None] * 1000
    # Create an array F to store the maximum number of non-overlapping notes
    F = [0] * 1000

    # Define the Enter procedure to read the notes
    def Enter():
        for i in range(n):
            first, last = map(int, input().split())
            A[i] = Note(first, last)

    # Define the Sort procedure to sort the notes based on the last field
    def Sort(l, h):
        if l >= h:
            return
        i, j, k = l, h, A[(l + h) // 2].last
        while i <= j:
            while A[i].last < k:
                i += 1
            while A[j].last > k:
                j -= 1
            if i <= j:
                if i < j:
                    A[i], A[j] = A[j], A[i]
                i += 1
                j -= 1
        Sort(l, j)
        Sort(i, h)

    # Define the Greedy procedure to calculate the maximum number of non-overlapping notes
    def Greedy():
        F[0] = 1
        for i in range(1, n):
            F[i] = 0
            for j in range(i - 1, -1, -1):
                if A[j].last < A[i].first:
                    break
                if A[j].last == A[i].first and F[i] < F[j]:
                    F[i] = F[j]
            F[i] += 1

    # Define the Escape procedure to print the maximum number of non-overlapping notes
    def Escape():
        maxV = max(F)
        print(maxV)

    # Call the procedures in the correct order
    Enter()
    Sort(0, n - 1)
    Greedy()
    Escape()

# Call the main function
if __name__ == "__main__":
    main()
