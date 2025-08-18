#fruits1 = ["apple", "banana", "cherry"]
#fruits2 = ["orange", "kiwi", "melon"]
#fruits3 = ["grape", "pear", "peach"]
#fruits4 = ["mango", "papaya", "pineapple"]
#fruit = zip(fruits1, fruits2, fruits3, fruits4)
#print(*fruit)

nums = [1, 2, 3, 4, 5]
new_num = [num * 10 for num in nums]
print(new_num)

print("-----" * 10)
mas = [1, 2, 3, 4, 5]
new_mas = []
for i in mas:
    new_mas.append(i * 10)
print(new_mas)

print("-----" * 10)
results = [num for num in range(11)]
print(results)
print("-----" * 10)
pairs = []
for i in range(0,2):
    for j in range (6,8):
        pairs.extend([(i,j)])
print(pairs)

pairs = [(i,j) for i in range(0,2) for j in range(6,8)]
print(pairs)

matrix = [[col for col in range(5)] for row in range(5)]
for row in matrix:
    print(row)

numa = [ num ** 2 for num in range(10) if num % 2 == 0]
print(numa)

numa_neg = {num:- num for num in range(10)}
print(numa_neg)

fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

new_fellowship = [ member for member in fellowship if len(member) > 6]
print(new_fellowship)

print("-----" * 10)

new_fellowship1 = []
for member in fellowship:
    if len(member) > 6:
        new_fellowship1.extend([member])
print(new_fellowship1)

print("-----" * 10)
new_fellowship2 = {member: len(member) for member in fellowship if len(member) > 6}
print(new_fellowship2)

print("-----" * 10)
print("-----" * 10)
print("-----" * 10)


def num_sequence(n):
    i = 0
    while i < n:
        yield i
        i += 1
    return
print(list(num_sequence(10)))

print("-----" * 10)

s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}

print(s1.union(s2))  # Union
print(s1.intersection(s2))  # Intersection
print(s1.difference(s2))  # Difference
print(s2.difference(s1))
print(s1.symmetric_difference(s2))  # Symmetric Difference

print("-----" * 10)

child_ages = ['5', '6', '7', '8', '9']

print(', '.join(child_ages))  # This will raise an error because child_ages is a list of strings
print(f"The children are ages {', '.join(child_ages[0:4])} and {', '.join(child_ages[-1:])}.")  # Correct usage with slicing


names = ['John', 'kim', 'Smith']
print([name for name in names if name.startswith('J') and name.endswith('n')])  # List comprehension to filter names starting with 'J'


print("-----" * 10)

apples = 2
if apples > 0:
    print("We have apples.")

print("-" * 10 )

my_story = """Every morning, the little restaurant on the corner opened its doors at exactly 8 o’clock.
The owner, Mr. Karim, would greet every customer with the same warm smile and say,
"Welcome! Please, take a seat."
The waiter, Ali, would bring menus to the tables, just as he did every morning.
He would ask each guest, "Would you like tea or coffee to start?"
No matter how many times he asked, the smile on his face never faded.

In the kitchen, Chef Lina prepared the same signature dishes over and over —
fresh bread, sizzling kebabs, and her famous lentil soup.
The aroma filled the air again and again, drawing more people inside.

By noon, the restaurant was always full.
Ali would repeat his routine: take the orders, bring the drinks, and serve the meals."""

from collections import Counter

word_count = Counter(my_story)
print(word_count['the'])  # Count occurrences of the word 'the'