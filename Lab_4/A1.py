import random
import time

N = int(input("Введите количество примеров: "))
counter = 0
total_time = 0

for i in range(N):
    print(f"Вопрос {i+1}/{N}")
    a = random.randint(2, 9)
    b = random.randint(2, 9)

    start_time = time.time()

    while True: 
        try:
            answer = int(input(f"{a} × {b} = ")) 
            break 
        except ValueError: 
            print("Пожалуйста, введите целое число!")

    time_spend = time.time() - start_time
    total_time += time_spend
    if answer == a*b:
        print(f"Верно! (Время: {time_spend} сек)")
        counter += 1
    else:
        print(f"Неверно! Правильно: {a*b} (Время: {time_spend} сек)")
print("=================================================")
print("СТАТИСТИКА:")
print("=================================================")
print(f"Общее время: {total_time} секунд")
print(f"Среднее время на вопрос: {total_time/N} сек")
print(f"Правильных ответов: {counter}/{N}")
print(f"Процент правильных: {float(counter/N*100)}%")
