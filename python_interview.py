def list_str(input_str) -> [str]:   # returns only strings and digits <= 5
    new = []
    for inputs in input_str:
        if inputs == ' ' or (inputs.isdigit() and int(inputs) > 5):
            continue
        new.append(inputs)
    return new


text = list_str("My string56")
print(text)


def vowel_count(input_str):     # returns count of vowels in the given string
    vowel = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for vo in input_str:
        if vo in vowel:
            count += 1
        continue
    return count


count_vow = vowel_count("veera Marni")
print(count_vow)

def fibonacci(n: int):      # fibonacci series using iterative method
    num_0 = 0
    num_1 = 1
    series_list = []
    if n > num_0:
        if n > num_1:
            for integer in range(n):
                series_list.append(num_0)
                nth = num_0+num_1
                num_0 = num_1
                num_1 = nth
            return series_list
        return [num_0]
    return "Enter positive number"


print(fibonacci(5))


def fibonacci_rec(num):        # fibonacci series using recursive method
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci_rec(num-1) + fibonacci_rec(num-2)


number = int(input("Enter the number: "))
for i in range(0, number):
    print(fibonacci_rec(i))


def max_num(num_list: []) -> str:       # return max number in the given list
    maxi = num_list[0]
    for num in num_list:
        if maxi < num:      # for minimum number change the less than to greater than.
            maxi = num
    return maxi


print(max_num([1, 5, 16, 18, 9]))


def str_list(input_list: []) -> str:    # Converts list of strings into a string
    out_str = ''
    for character in input_list:
        out_str += character
    return out_str


print(str_list(['p', 'y', 't', 'h', 'o', 'n']))


def reverse_num(num: int):      # reverse number iterative method
    rev = 0
    while num != 0:
        rev = rev*10 + num % 10
        num = num//10
    return rev


print(reverse_num(5249))


def palindrome_num(nump: int):       # palindrome iterative method
    r = 0
    numi = nump
    while nump != 0:
        r = r*10 + nump % 10
        nump = nump//10

    if r == numi:
        return f"{numi} is palindrome"
    else:
        return f"{numi} is not palindrome"


print(palindrome_num(151))

num1 = int(input("Enter the number for recursive palindrome:"))     # Palindrome recursive number

def reverse(num):
    if num < 10:
        return num
    else:
        return int(str(num % 10) + str(reverse(num//10)))

def palindrome_rec(num):
    if num == reverse(num):
        return f"{num} is palindrome"
    return f"{num} is not palindrome"


print(palindrome_rec(num1))


def armstrong_num(num: int):        # Armstrong number
    tot = 0
    input_num = num
    while num != 0:
        temp = num % 10
        tot += temp ** 3
        num = num//10

    if tot == input_num:
        return "Given number is armstrong number"
    return "Given number is not armstrong number"


print(armstrong_num(152))


def prime_num(num: int):        # Prime number
    p = 1
    if num == 1:
        return "1 is not a prime or composite number"
    while p <= num:
        if p in [1, num]:
            p += 1
        elif num % p == 0:
            return f"{num} is not a prime number"
        else:
            p += 1
    return f"{num} is a prime number"


print(prime_num(1))


def greatest_3(num_1: int, num_2: int, num_3: int):
    great_num = num_1
    if great_num < num_2:
        if num_2 < num_3:
            great_num = num_3
            return great_num
        great_num = num_2
        return great_num
    return great_num


print(greatest_3(14, 15, 19))


def factorial_rec(num: int):        # factorial using recursion
    if num == 1:
        return 1
    else:
        return num*factorial_rec(num-1)


print(factorial_rec(5))


def power_val(base: int, power: int):       # calculates the power of base number value without using pow method
    if base == 0:
        return 0
    elif power == 0:
        return 1
    elif power > 0:
        return base * power_val(base, power-1)


print(power_val(2, 3))


def prime_till_n(n: int):       # prime numbers till given  integer
    prime_list = []
    if n <= 0 or n == 1:
        return "Enter the number greate than 1"
    else:
        pr = 2
        pr_num = 2
        while pr_num in range(2, n-1):
            if pr < pr_num and pr_num % pr == 0:
                pr_num += 1
            prime_list.append(pr_num)
            pr_num += 1
        return prime_list


print(prime_till_n(5))


def missing_num_array(size: int, num_array: []):    # missing number in the given series of natural numbers array
    actual_sum = int(size*(size+1)/2)
    result_sum = 0
    for i, num in enumerate(num_array):
        result_sum += num
    missing_num = actual_sum - result_sum
    return missing_num


print(missing_num_array(10, [1, 4, 5, 3, 6, 7, 8, 9, 10]))


def duplicate_num_array(num_array: []):      # count of duplicate numbers in the given array
    out_list = {}
    for num in num_array:
        if num in out_list.keys():
            out_list[num] = out_list[num]+1
        else:
            out_list[num] = 1
    for key, value in out_list.items():
        if int(out_list[key]) > 1:
            print(f"Number {key} repeated {value} times")


duplicate_num_array([1, 5, 4, 6, 7, 8, 2, 1, 5, 4])
