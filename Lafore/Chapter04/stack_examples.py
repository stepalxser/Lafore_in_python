from Lafore.Chapter04.stack import Stack

# chapter 4 listing code 4.2
if __name__ == '__main__':
    data = input()
    stack = Stack(len(data))

    for char in data:
        stack.push(char)

    print(''.join(stack.pop()for _ in range(len(data))))
