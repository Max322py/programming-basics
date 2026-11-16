packets = str(input())
count = 0
max_count = 0

if not all(char in '01' for char in packets):
    print("Неверный ввод. Используйте только символы '0' и '1'!")
for packet in packets:
    if packet == '0':
        count += 1
        max_count = count
    else:
        count = 0

percent = packets.count('0')/len(packets)*100

if 0 <= percent <= 1:
    quality = "отличное"
elif 1 < percent <= 5:
    quality = "хорошее"
elif 5 < percent <= 10:
    quality = "удовлетворительное"
elif 10 < percent <= 20:
    quality = "плохое"
elif percent > 20:
    quality = "критическое состояние сети"

print(f"Общее количество пакетов: {len(packets)}")
print(f"Количество потерянных пакетов: {packets.count('0')}")
print(f"Длина самой длинной последовательности потерянных пакетов: {max_count}")
print(f"Процент потерь: {percent}%")
print(f"Качество связи: {quality}")