array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def statistics(arr):
    total = sum(arr)
    count = len(arr)
    avarage = total / count
    minimum = min(arr)
    maximum = max(arr)
    
    return {
        'avarage': avarage,
        'min': minimum,
        'max': maximum
    }

print(statistics(array))