import sys
import os
import pathlib


def process(filename: str):

    with open(filename, mode='r') as file:
        
        with open('out.txt', mode="w") as wfile:
            lines = file.readlines()
            # print(lines)
            sum = 0
            try:
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
                        wfile.write(f'{start},')
                        print(f'{start},', end='')
                    else:
                        wfile.write(f'{start}~{end},')
                        print(f'{start}~{end},', end='')
                        
                print()
                print()
                print(f'Total: {sum}, {sum*100}')
            
            except Exception as e:
                print_usage("INVALID FILE CONTENTS")


def print_usage(err: str):
    msg = f'''{err}
    
Usage:
        python3 {sys.argv[0]} FILENAME.txt
    '''
    print(msg)


def main():
    if(len(sys.argv) != 2):
        print_usage('INVALID ARGUMENTS!')
        return
    
    filename = sys.argv[1]
    
    if filename.split('.')[1] != 'txt':
        print_usage('INVALID FILETYPE. ".txt" file required.')
        return
    
    path = pathlib.Path(filename)
    if path.is_file():
        process(filename)
        
    else:
        print_usage("NO FILE FOUND OR INVALID FILE.")
    



if __name__ == "__main__":   
        main()