"""Стабильная сортировка пузырьком; исходная последовательность сохраняется."""


def bubble_sort(values):
    result = list(values)
    for end in range(len(result) - 1, 0, -1):
        changed = False
        for i in range(end):
            if result[i] > result[i + 1]:
                result[i], result[i + 1] = result[i + 1], result[i]
                changed = True
        if not changed:
            break
    return result
