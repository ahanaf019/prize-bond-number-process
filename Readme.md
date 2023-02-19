# Prize Bond Number Processor
The program takes input from a .txt file in the format below:

```
<!-- input.txt -->
STARTING_1 NUMBER_OF_BONDS
STARTING_2 NUMBER_OF_BONDS
STARTING_3 NUMBER_OF_BONDS
STARTING_4 NUMBER_OF_BONDS
```

The input file is processed and a string is generated with the number ranges which is accepted by [Bangladesh Bank](https://www.bb.org.bd/en/index.php/investfacility/prizebond)'s Winning Bond Searching page. The program outputs to the console, in a file named `out.txt`, and copies it to clipboard.

# Usage
```
python3 process.py FILENAME.txt
```
