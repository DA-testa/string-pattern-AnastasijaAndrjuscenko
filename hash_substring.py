# python3
def read_input():
    L = input()
    if L == 'I':
        pattern, text = input().split('\n')
    elif L == 'F':
        with open("/home/runner/work/string-pattern-AnastasijaAndrjuscenko/string-pattern-AnastasijaAndrjuscenko/tests/06", 'r') as file:
            pattern = file.readline().rstrip()
            text = file.readline().rstrip()
    return pattern, text

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    m = 10**9 + 9 
    p = 31
    n = len(text)
    m = len(pattern)

    p_powers = [1]
    for i in range(1, n):
        p_powers.append((p_powers[-1] * p) % m)


    pattern_hash = 0
    window_hash = 0
    for i in range(m):
        pattern_hash = (pattern_hash * p + ord(pattern[i])) % m
        window_hash = (window_hash * p + ord(text[i])) % m

    occurrences = []
    for i in range(n - m + 1):
        if pattern_hash == window_hash:
            if pattern == text[i:i+m]:
                occurrences.append(i)
        if i < n - m:
            window_hash = ((window_hash - p_powers[m-1] * ord(text[i])) * p + ord(text[i+m])) % m
            window_hash = (window_hash + m) % m 

    return occurrences

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
