
def binary_search(array, element, left, right):
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует
    middle = (left + right) // 2  # находим середину
    if array[middle] == element:
        array.remove(element)
        return middle, middle + 1  # возвращаем этот индекс
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array, element, middle + 1, right)


numbers = [int(x) for x in input("Введите целые числа в любом порядке, через пробел: ").split()]
number = int(input("Введите целое число: "))
numbers.sort()
print(numbers)
while numbers[0] > number or number > numbers[-1]:
    print("Условия не удовлетворяются")
    number = int(input("Введите целое число: "))


numbers.append(number)
numbers.sort()
print(numbers)

print(binary_search(numbers, number, 0, len(numbers)))
print(numbers)