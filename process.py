import sys
import os
import pathlib
import argparse
import pyperclip


def process(filename: str, file_output=None, clipboard_output=None):
    with open(filename, mode='r') as input_file:
        lines = input_file.readlines()

    sum = 0
    try:
        result = []
        for line in lines:
            first = line.split(' ')
            second = first[1]
            first = first[0]
            
            start = int(first)
            end = start + int(second) - 1
            sum += int(second)
            end = str(end)

            # Padding with leading zeros
            start = str(start)
            n = len(first) - len(start)
            start = '0'*n + start
            end = '0'*n + end
            
            if int(second) == 1:
                result.append(f'{start}')
            else:
                result.append(f'{start}~{end}')
        result = ','.join(result)
        print()
        print(f'Total Bonds: {sum} | Total Amount: {sum*100}')
        
    except Exception as e:
        print_error("INVALID FILE CONTENTS")
    
    if file_output is not None:
        with open(file_output, "w") as f:
            f.writelines(result)
        print(f'Write results to {file_output}.')
    if clipboard_output:
        pyperclip.copy(result)
        print('Coppied to clipboard!')


def print_error(err: str):
    msg = f'''ERROR: {err}'''
    print(msg)


def main():
    parser = argparse.ArgumentParser(description="Process prizebonds.")

    parser.add_argument("-i", "--infile", type=str, required=True, help="Input file to process")
    parser.add_argument("-o", "--outfile", type=str, required=False, help="Output to a txt file")
    parser.add_argument("-c", "--clipboard", action="store_true", required=False, help="Output to clipboard")

    args = vars(parser.parse_args())
    print(args)
    filename = args['infile']
    
    if filename.split('.')[1] != 'txt':
        print_error('INVALID FILETYPE. ".txt" file required.')
        return
    
    path = pathlib.Path(filename)
    if path.is_file():
        process(filename, file_output=args['outfile'], clipboard_output=args['clipboard'])
        
    else:
        print_error("NO FILE FOUND OR INVALID FILE.")
    



if __name__ == "__main__":   
        main()