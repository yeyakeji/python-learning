# Python 循环
# 循环可以重复执行代码

# 1. for 循环 - 遍历列表
print("=== for 循环 ===")
fruits = ["苹果", "香蕉", "橙子", "葡萄"]
for fruit in fruits:
    print(f"我喜欢吃 {fruit}")

# 2. for 循环 - 使用 range()
print("\n=== for 循环和 range ===")
for i in range(1, 6):
    print(f"数字：{i}")

# 3. while 循环
print("\n=== while 循环 ===")
count = 1
while count <= 5:
    print(f"计数：{count}")
    count += 1

# 4. break 语句（退出循环）
print("\n=== break 语句 ===")
for i in range(1, 11):
    if i == 5:
        break
    print(f"数字：{i}")
print("循环已中断")

# 5. continue 语句（跳过本次循环）
print("\n=== continue 语句 ===")
for i in range(1, 6):
    if i == 3:
        continue
    print(f"数字：{i}")

# 6. 嵌套循环
print("\n=== 嵌套循环 ===")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"({i}, {j})", end=" ")
    print()  # 换行

# 7. 使用 enumerate() 获取索引
print("\n=== enumerate 循环 ===")
items = ["第一项", "第二项", "第三项"]
for index, item in enumerate(items):
    print(f"索引 {index}：{item}")
