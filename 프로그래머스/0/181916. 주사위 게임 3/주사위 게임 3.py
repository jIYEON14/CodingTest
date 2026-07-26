def solution(a, b, c, d):
    a, b, c, d = sorted([a,b,c,d])
    if a == d: #4개 같음
        return 1111*a
    if a == c: #앞 3개 같음
        return (10 * a + d) ** 2
    if b == d: #뒤 3개 같음
        return (10 * b + a) ** 2
    if a == b and c == d: #2개씩 같음
        return (a + c) * abs(a - c)
    if a == b: #앞 2개만 같음
        return c * d
    if b == c: #가운데 2개마 같음
        return a * d
    if c == d: #뒤 2개만 같음
        return a * b
    return a #모두 다름