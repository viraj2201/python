N = int(input())
KEY = map(int, input().split())
KEY = sorted(KEY)
for i in range (len (KEY)):
    if(i != len(KEY)-1):
        if(KEY[i]!=KEY[i-1] and KEY[i]!=KEY[i+1]):
            print(KEY[i])
            break;
    else:
         print(KEY[i])