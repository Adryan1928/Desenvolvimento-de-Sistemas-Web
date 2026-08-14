names = ["Ana", "Bruno", "Carlos", "Ana", "Bruno", "Ana"]

def count_names(names):
    name_count = {}
    for name in names:
        if name in name_count:
            name_count[name] += 1
        else:
            name_count[name] = 1

    name_list = [name for name, count in name_count.items() if count > 1]
    return {
        'name_count': name_count,
        'name_list': name_list
    }


print(count_names(names))