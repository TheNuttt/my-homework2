friends = { 
    'Я': [ 'Ramina', 'Diana' ],
    'Ramina': [ 'Я', 'Diana' ],
    'Diana': [ 'Я', 'Safida', 'Aelita'],
    'Safida': [ 'Diana'],
    'Aelita': ['Ramina']
}

target = 'Diana'

queue = ['Я']
visited = ['Я']

found = False

while len(queue) > 0 and not found:
    p = queue.pop(0)

    print("Проверяем знакомого:", p)

    if p == target:
        print("Ура, Нашли друга:", p)
        found = True
    else:
        for f in friends[p]:
            if f not in visited:
                visited.append(f)
                queue.append(f)    