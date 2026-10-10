change = int(input("Введите сумму сдачи: "))
coins = [50, 10, 5, 2, 1]
print("Сдача выдана монетами:")

for coin in coins:
    count = change // coin
    if count > 0:
        print(f"Монета {coin}: {count} шт. ")
    change = change % coin    