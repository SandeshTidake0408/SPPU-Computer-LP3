
def fibNumberI(n):
    step_count = 0

    if (n < 0):
        return -1, 1

    if (n == 0):
        return n, 1

    prev, curr = 0, 1

    for i in range(2, n+1):
        step_count += 1
        prev, curr = curr, prev+curr

    return curr, step_count


def fibNumberR(n, step_count):
    step_count[0] += 1

    if n <= 1:
        return n
    else:
        return fibNumberR(n-1, step_count) + fibNumberR(n-2, step_count)


if __name__ == '__main__':
    n = int(input("Enter a number : "))

    print("Iterative : ", fibNumberI(n))

    step_count = [0]
    print("Recursive : ", fibNumberR(n, step_count), step_count)
