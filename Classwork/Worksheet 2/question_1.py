# Initial list L
L = [11, 12, 13, 14]

# (i) Add 50 and 60 to L
L.append(50)
L.append(60)
print("After adding 50 and 60:", L)

# (ii) Remove 11 and 13 from L
L.remove(11)
L.remove(13)
print("After removing 11 and 13:", L)

# (iii) Sort L in ascending order
L.sort()
print("List in ascending order:", L)

# (iv) Sort L in descending order
L.sort(reverse=True)
print("List in descending order:", L)

# (v) Search for 13 in L
if 13 in L:
    print("13 is found in the list.")
else:
    print("13 is not found in the list.")

# (vi) Count the number of elements in L
count = len(L)
print("Number of elements in L:", count)

# (vii) Sum all the elements in L
total = sum(L)
print("Sum of all elements in L:", total)

# (viii) Sum all ODD numbers in L
odd_sum = sum([x for x in L if x % 2 != 0])
print("Sum of all odd numbers in L:", odd_sum)

# (ix) Sum all EVEN numbers in L
even_sum = sum([x for x in L if x % 2 == 0])
print("Sum of all even numbers in L:", even_sum)

# (x) Sum all PRIME numbers in L
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

prime_sum = sum([x for x in L if is_prime(x)])
print("Sum of all prime numbers in L:", prime_sum)

# (xi) Clear all the elements in L
L.clear()
print("List after clearing all elements:", L)

# (xii) Delete L
del L
print("L is deleted.")