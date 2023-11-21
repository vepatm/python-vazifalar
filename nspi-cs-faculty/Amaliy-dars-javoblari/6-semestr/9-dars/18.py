n = int(input('n='))
sum_digits = 0
count_digits = 0

while n > 0:

    digit = n % 10
    
    sum_digits += digit
    

    n //= 10

    count_digits += 1

print(count_digits)
print(sum_digits)