def finding_gcd(a,b):
    'implements the greatest common divider algorithm'
    result, i = 0, 1
    while (i <= a):
        if (a % i == 0) & (b % i == 0):
            result = i
        i += 1
    return result
