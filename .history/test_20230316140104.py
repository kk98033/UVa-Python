def solve(n, ans):
    # 'kuti' (10000000), 'lakh' (100000), 'hajar' (1000), 'shata' (100) 
    if n >= 10000000:
        ans += f'{solve(n // 10000000, "")} kuti '
        n = n % 10000000
    if n >= 100000:
        ans += f'{solve(n // 100000, "")} lakh '
        n = n % 100000
    if n >= 1000:
        ans += f'{solve(n // 1000, "")} hajar '
        n = n % 1000
    if n >= 100:
        ans += f'{solve(n // 100, "")} shata '
        n = n % 100
    if n != 0:
        ans += str(n)
    else: 
        ans = ans[:-2]

    return ans

count = 1
while True:
    try:
        n = int(input())
        print(f'   {count}. {solve(n, "")}')
        count += 1
    except EOFError:
        break