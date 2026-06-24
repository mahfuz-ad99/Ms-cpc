import sys

def solve():
   
    s = sys.stdin.read().strip()
    
    
    if upper_count > lower_count:
        print(s.upper())
    else:
        print(s.lower())

if __name__ == '__main__':
    solve()
