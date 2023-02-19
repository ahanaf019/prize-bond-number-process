
filename = 'test.txt'
with open(FILENAME, mode='r') as file:
    
    lines = file.readlines()
    # print(lines)
    sum = 0
    for line in lines:
        
        first = line.split(' ')
        second = first[1]
        first = first[0]
        # print(first, int(second))
        
        start = int(first)
        end = start + int(second) - 1
        sum += int(second)
        end = str(end)
        
        start = str(start)
        n = len(first) - len(start)
        start = '0'*n + start
        end = '0'*n + end
        
        if int(second) == 1:
            print(f'{start},', end='')
        else:
            print(f'{start}~{end},', end='')
            
    print()
    print()
    print(f'Total: {sum}, {sum*100}')
