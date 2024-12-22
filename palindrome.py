n=151
temp=n
reverse = 0
while temp > 0:
    remainder = temp % 10   
    reverse = (reverse *10) +remainder
    temp = temp//10
print(reverse)
if n==reverse:
    print('palindrome')
else:
    print('not palindrome')