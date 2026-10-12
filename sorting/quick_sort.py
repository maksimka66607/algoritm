"""Итеративная быстрая сортировка с трехчастным разбиением."""


def quick_sort(values):
    result = list(values)
    stack = [(0, len(result) - 1)]
    while stack:
        low, high = stack.pop()
        if low >= high:
            continue
        pivot = result[(low + high) // 2]
        left = current = low
        right = high
        while current <= right:
            if result[current] < pivot:
                result[left], result[current] = result[current], result[left]
                left += 1
                current += 1
            elif result[current] > pivot:
                result[current], result[right] = result[right], result[current]
                right -= 1
            else:
                current += 1
        stack.append((low, left - 1))
        stack.append((right + 1, high))
    return result
