# You can control the flow of loops using:
# break: Exits the loop prematurely.
# continue: Skips the current iteration and moves to the next one.
# else: a block that executes after the loop completes normally(not when break is used).
# 

for num in range(10):
    if num == 5:
        break # Exit the loop when num is 5
    if num % 2 == 0:
        continue # Skip even numbers 
    print(num)

    # 