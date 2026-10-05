import random
import time

correct_answers = 0
total_time = 0.0
n = int(input("Введите количество примеров: "))

for i in range(1, n + 1):
    num1 = random.randint(2, 9)
    num2 = random.randint(2, 9)
    correct_result = num1 * num2
    print(f"Вопрос {i}/{n}")
    start_time = time.time()

    user_input = input(f"{num1} x {num2} = ")
    user_answer = int(user_input)
    elapsed_time = time.time() - start_time
    total_time += elapsed_time

    if user_answer == correct_result:
        print(f"Верно! (Время: {elapsed_time:.1f} сек)")
        correct_answers += 1
    else:
        print(f"Неверно! Правильно: {correct_result} (Время: {elapsed_time:.1f} сек)")

average_time = total_time / n
percentage_correct = (correct_answers / n) * 100

print("=========================================")
print("СТАТИСТИКА:")
print("=========================================")
print(f"Общее время: {total_time:.1f} секунд")
print(f"Среднее время на вопрос: {average_time:.1f} сек")
print(f"Правильных ответов: {correct_answers}/{n}")
print(f"Процент правильных: {percentage_correct:.1f}%")
