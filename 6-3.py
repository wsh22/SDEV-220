guess_me = 5
start = 1

for number in range(10):         
    print(number) 
    if start < guess_me:
        print('too low')
    elif start == guess_me:
        print ('found it!')
    elif start > guess_me:
        print ('oops')
        break
    start += 1