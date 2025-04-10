import random
import time

operator = ["+", "-", "*"]
minnum = 1
maxnum = 12
total = 10


def generate_problem():
    x1 = random.randint(minnum, maxnum)
    x2 = random.randint(minnum, maxnum)
    x3 = random.choice(operator)

    ex = str(x1) + " " + x3 + " " + str(x2)
    answer = eval(ex)
    return ex, answer

wrong = 0
input("กดปุ่ม Enter เพื่อเริ่ม")
print("---------------------------------")
start_time = time.time()

for i in range(total):
    ex, answer = generate_problem()
    while True:
        guess = input("Problem #" + str(i + 1) + " : " + ex + " = ")
        if guess == str(answer):
            break
        wrong += 1

end_time = time.time()
total_time = end_time - start_time

print("---------------------------------")
print("สุดยอด คุณทำครบทุกข้อแล้ว", total_time, "วินาที คุณทำผิดไปทั้งหมด", wrong, "ครั้งครับ")
