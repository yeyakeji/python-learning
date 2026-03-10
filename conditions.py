# Python 条件语句
# 根据不同条件执行不同的代码

# 1. if 语句
print("=== if 语句 ===")
age = 18
if age >= 18:
    print("你已经成年了")

# 2. if-else 语句
print("\n=== if-else 语句 ===")
score = 60
if score >= 60:
    print("及格了")
else:
    print("没及格")

# 3. if-elif-else 语句
print("\n=== if-elif-else 语句 ===")
grade = 75
if grade >= 90:
    print("成绩等级：A")
elif grade >= 80:
    print("成绩等级：B")
elif grade >= 70:
    print("成绩等级：C")
else:
    print("成绩等级：D")

# 4. 逻辑运算符 - and
print("\n=== and 运算符 ===")
age = 25
income = 5000
if age >= 18 and income >= 3000:
    print("符合申请条件")
else:
    print("不符合申请条件")

# 5. 逻辑运算符 - or
print("\n=== or 运算符 ===")
has_ticket = True
has_vip_card = False
if has_ticket or has_vip_card:
    print("可以进入")
else:
    print("不可以进入")

# 6. 逻辑运算符 - not
print("\n=== not 运算符 ===")
is_raining = False
if not is_raining:
    print("天气晴朗，可以出去玩")
else:
    print("下雨了，不能出去玩")

# 7. 比较运算符
print("\n=== 比较运算符 ===")
a = 10
b = 20
print(f"a == b: {a == b}")
print(f"a != b: {a != b}")
print(f"a > b: {a > b}")
print(f"a < b: {a < b}")
print(f"a >= b: {a >= b}")
print(f"a <= b: {a <= b}")