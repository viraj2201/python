if __name__=='__main__':
    N = int(input())
    ARR = map(int, input().split())
    print(sorted(list(set(ARR)))[-2])