heroes = ['spider man', 'thor', 'hulk', 'iron man', 'captain america']

# 1
print(f"1. {len(heroes)}")
# 2
heroes.append("black panther")
print(f"2. {heroes[-1]}")
# 3
mistake = heroes.pop()
heroes.insert(2, mistake)
print(f"3. {heroes}")
# 4 -
heroes[1:4]=['doctor strange']
print(f"4. {heroes}")
# 5
heroes.sort()
print(f"5. {heroes}")