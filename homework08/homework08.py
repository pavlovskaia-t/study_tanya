items = ['1,2,3,4', '1,2,3,4,50', 'minor74,8,9', 'John', '78,89,9,7,0']

def count_numbers(items):
    results = []
    for s in items:
        try:
            parts = s.split(',')
            total = 0
            for i in parts:
                num = int(i)
                total += num
            results.append(total)
        except ValueError:
            results.append('Нецифрове значення')
    return results

print(count_numbers(items))
