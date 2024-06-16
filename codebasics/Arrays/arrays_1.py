expenses = [2200, 2350, 2600, 2130, 2190]

# 1
print(f"1. {expenses[1] - expenses[0]}")
# 2
print(f"2. {sum(expenses[:3])}")
# 3
print(f"3. {True if 2000 in expenses else False}")
# 4
expenses.append(1980)
print(f"4. {expenses}")
# 5
expenses[3] -= 200
print(f"5. {expenses[3]}")