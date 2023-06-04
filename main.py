
def binary_search(array, element, left, right):
    if left > right:
        return False
    middle = (left + right) // 2
    if array[middle] == element:
        array.remove(element)
        return middle, middle + 1
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)


numbers = [int(x) for x in input("Введите целые числа в любом порядке, через пробел: ").split()]
number = int(input("Введите целое число: "))
numbers.sort()

while numbers[0] > number or number > numbers[-1]:
    print("Условия не удовлетворяются")
    number = int(input("Введите целое число: "))


numbers.append(number)
numbers.sort()


print(binary_search(numbers, number, 0, len(numbers)))
print(numbers)