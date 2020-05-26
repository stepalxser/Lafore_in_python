def triange(n: int) -> int:
    if n == 1:
        return n
    else:
        return triange(n-1) + n


def factorial(n: int) -> int:
    if n == 0:
        return 1
    else:
        return factorial(n-1) * n


# programming project 5.1
def mult(a:int ,b: int) -> int:
    if b == 1:
        return a
    else:
        return mult(a, b-1) + a


# programming project 5.2
def print_binary_tree(left: int = 0, right: int = 16) -> None:
    pass


# programming project 5.3
def power(a: int, b: int):
    if b == 1:
        return a
    else:
        return power(a*a, b//2)


if __name__ == '__main__':
    print(triange(int(input('Print a number for triangle: '))))

    print(factorial(int(input('Print a number for factorial: '))))

    print(mult(9, 6))

    print(power(3, 18))


