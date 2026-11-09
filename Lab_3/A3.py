previous = int(input())
current = int(input())

if current >= previous:
    gas = current - previous
else:
    gas = 10000 - previous + current

if gas <= 300:
    pay = 21
elif gas <= 600:
    pay = 21 + (gas - 300) * 0.06
elif gas <= 800:
    pay = 21 + 300 * 0.06 + (gas - 600) * 0.04
else:
    pay = 21 + 300 * 0.06 + 200 * 0.04 + (gas - 800) * 0.025
average = pay / gas if gas != 0 else 0

print("Предыдущее:", previous)
print("Текущее:", current)
print("Использовано:", gas)
print("К оплате: {:.2f}".format(pay))
print("Средняя цена: {:.2f}".format(average))