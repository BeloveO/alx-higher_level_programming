# 0x01. Python - if/else, loops, functions

## Tasks
### 0. Positive anything is better than negative nothing
This program will assign a random signed number to the variable `number` each time it is executed. Complete the source code in order to print whether the number stored in the variable `number` is positive or negative.

- You can find the source code [here](https://github.com/holbertonschool/0x01.py/blob/1af74da637024c59aab34027d5758b83eb1764e1/0-positive_or_negative_py)
- The variable `number` will store a different value every time you will run this program
- You don’t have to understand what `import`, `random. randint` do. Please do not touch this code
- The output of the program should be:
  - The number, followed by
  - if the number is greater than 0: `is positive`
  - if the number is 0: `is zero`
  - if the number is less than 0: `is negative`
followed by a new line

- **File**: [0-positive_or_negative.py]()

### 1. The last digit
This program will assign a random signed number to the variable `number` each time it is executed. Complete the source code in order to print the last digit of the number stored in the variable `number`.

- You can find the source code [here](https://github.com/holbertonschool/0x01.py/blob/1af74da637024c59aab34027d5758b83eb1764e1/1-last_digit_py)
- The variable `number` will store a different value every time you will run this program
- You don’t have to understand what `import`, `random.randint` do. Please do not touch this code. This line should not change: `number = random.randint(-10000, 10000)`
- The output of the program should be:
  - The string `Last digit of`, followed by
  - the number, followed by
  - the string `is`, followed by the last digit of `number`, followed by
    - if the last digit is greater than 5: the string `and is greater than 5`
    - if the last digit is 0: the string `and is 0`
    - if the last digit is less than 6 and not 0: the string `and is less than 6 and not 0`
  - followed by a new line
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of 4205 is 5 and is less than 6 and not 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of -626 is -6 and is less than 6 and not 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of 1144 is 4 and is less than 6 and not 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of -9200 is 0 and is 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of 5247 is 7 and is greater than 5
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of -9318 is -8 and is less than 6 and not 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of 3369 is 9 and is greater than 5
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of -5224 is -4 and is less than 6 and not 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of -4485 is -5 and is less than 6 and not 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of 3850 is 0 and is 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of 5169 is 9 and is greater than 5
guillaume@ubuntu:~/0x01$ 
Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x01-python-if_else_loops_functions
- **File:** [1-last_digit.py]()
    
### 2. I sometimes suffer from insomnia. And when I can't fall asleep, I play what I call the alphabet game
Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.

- You can only use one `print` function with string format
- You can only use one loop in your code
- You are not allowed to store characters in a variable
- You are not allowed to import any module

- **File:** [2-print_alphabet.py]()
    
### 3. When I was having that alphabet soup, I never thought that it would pay off
Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.

- Print all the letters except `q` and `e`
- You can only use one `print` function with string format
- You can only use one loop in your code
- You are not allowed to store characters in a variable
- You are not allowed to import any module

- **File:** [3-print_alphabt.py]()
    
### 4. Hexadecimal printing
Write a program that prints all numbers from `0` to `98` in decimal and in hexadecimal

- You can only use one `print` function with string format
- You can only use one loop in your code
- You are not allowed to store numbers or strings in a variable
- You are not allowed to import any module

- **File:** [4-print_hexa.py]()
    
### 5. 00...99
Write a program that prints numbers from `0` to `99`.

- Numbers must be separated by `,`, followed by a space
- Numbers should be printed in ascending order, with two digits
- The last number should be followed by a new line
- You can only use no more than 2 `print` functions with string format
- You can only use one loop in your code
- You are not allowed to store numbers or strings in a variable
- You are not allowed to import any module

- **File:** [5-print_comb2.py]()
    
### 6. Inventing is a combination of brains and materials. The more brains you use, the less material you need
Write a program that prints all possible different combinations of two digits.

- Numbers must be separated by `,`, followed by a space
- The two digits must be different
- `01` and `10` are considered the same combination of the two digits `0` and `1`
- Print only the smallest combination of two digits
- Numbers should be printed in ascending order, with two digits
- The last number should be followed by a new line
- You can only use no more than 3 `print` functions with string format
- You can only use no more than 2 loops in your code
- You are not allowed to store numbers or strings in a variable
- You are not allowed to import any module
guillaume@ubuntu:~/0x01$ ./6-print_comb3.py
01, 02, 03, 04, 05, 06, 07, 08, 09, 12, 13, 14, 15, 16, 17, 18, 19, 23, 24, 25, 26, 27, 28, 29, 34, 35, 36, 37, 38, 39, 45, 46, 47, 48, 49, 56, 57, 58, 59, 67, 68, 69, 78, 79, 89
guillaume@ubuntu:~/0x01$ 
Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x01-python-if_else_loops_functions
- **File:** [6-print_comb3.py]()
    
### 7. islower
mandatory
Score: 100.0% (Checks completed: 100.0%)
Write a function that checks for lowercase character.

- Prototype: `def islower(c):`
- Returns `True` if `c` is lowercase
- Returns `False` otherwise
- You are not allowed to import any module
- You are not allowed to use `str.upper()` and `str.isupper()`
- [Tips: ord()](https://docs.python.org/3.4/library/functions.html?highlight=ord#ord)
You don’t need to understand `__import__`

- **File:** [7-islower.py]()
    
### 8. To uppercase
Write a function that prints a string in uppercase followed by a new line.

- Prototype: `def uppercase(str):`
- You can only use no more than 2 `print` functions with string format
- You can only use one loop in your code
- You are not allowed to import any module
- You are not allowed to use `str.upper()` and `str.isupper()`
- [Tips: ord()](https://docs.python.org/3.4/library/functions.html?highlight=ord#ord)
You don’t need to understand `__import__`

- **File:** [8-uppercase.py]()
    
### 9. There are only 3 colors, 10 digits, and 7 notes; it's what we do with them that's important
Write a function that prints the last digit of a number.

- Prototype: `def print_last_digit(number):`
- Returns the value of the last digit
- You are not allowed to import any module
You don’t need to understand `__import__`

- **File:** [9-print_last_digit.py]()
    
### 10. a + b
Write a function that adds two integers and returns the result.

- Prototype: `def add(a, b):`
- Returns the value of `a + b`
- You are not allowed to import any module
You don’t need to understand `__import__`

- **File:** [10-add.py]()
    
### 11. a ^ b
Write a function that computes a to the power of b and return the value.

- Prototype: `def pow(a, b):`
- Returns the value of `a ^ b`
- You are not allowed to import any module
You don’t need to understand `__import__`

guillaume@ubuntu:~/0x01$ cat 11-main.py
#!/usr/bin/env python3
pow = __import__('11-pow').pow

print(pow(2, 2))
print(pow(98, 2))
print(pow(98, 0))
print(pow(100, -2))
print(pow(-4, 5))

guillaume@ubuntu:~/0x01$ ./11-main.py
4
9604
1
0.0001
-1024
guillaume@ubuntu:~/0x01$ 
Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x01-python-if_else_loops_functions
- **File:** [11-pow.py]()
    
### 12. Fizz Buzz
Write a function that prints the numbers from 1 to 100 separated by a space.

- For multiples of three print `Fizz` instead of the number and for multiples of five print `Buzz`.
- For numbers which are multiples of both `three` and five print `FizzBuzz`.
- Prototype: `def fizzbuzz():`
- Each element should be followed by a space
- You are not allowed to import any module
You don’t need to understand `__import__`

- **File:** [12-fizzbuzz.py]()
    
### 13. Insert in sorted linked list
Technical interview preparation:

- You are not allowed to google anything
- Whiteboard first
Write a function in C that inserts a number into a sorted singly linked list.

- Prototype: `listint_t *insert_node(listint_t **head, int number);`
- Return: the address of the new node, or `NULL` if it failed
```
**cat lists.h**
#ifndef LISTS_H
#define LISTS_H

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 *
 */
typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int n);
void free_listint(listint_t *head);

listint_t *insert_node(listint_t **head, int number);

#endif /* LISTS_H */
```
```
**cat linked_lists.c**
#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * print_listint - prints all elements of a listint_t list
 * @h: pointer to head of list
 * Return: number of nodes
 */
size_t print_listint(const listint_t *h)
{
    const listint_t *current;
    unsigned int n; /* number of nodes */

    current = h;
    n = 0;
    while (current != NULL)
    {
        printf("%i\n", current->n);
        current = current->next;
        n++;
    }

    return (n);
}

/**
 * add_nodeint_end - adds a new node at the end of a listint_t list
 * @head: pointer to pointer of first node of listint_t list
 * @n: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */
listint_t *add_nodeint_end(listint_t **head, const int n)
{
    listint_t *new;
    listint_t *current;

    current = *head;

    new = malloc(sizeof(listint_t));
    if (new == NULL)
        return (NULL);

    new->n = n;
    new->next = NULL;

    if (*head == NULL)
        *head = new;
    else
    {
        while (current->next != NULL)
            current = current->next;
        current->next = new;
    }

    return (new);
}

/**
 * free_listint - frees a listint_t list
 * @head: pointer to list to be freed
 * Return: void
 */
void free_listint(listint_t *head)
{
    listint_t *current;

    while (head != NULL)
    {
        current = head;
        head = head->next;
        free(current);
    }
}
```

- **File:** [13-insert_number.c](), [lists.h]()
    
### 14. Smile in the mirror
Write a program that prints the ASCII alphabet, in reverse order, alternating lowercase and uppercase (`z` in lowercase and `Y` in uppercase) , not followed by a new line.

- You can only use one `print` function with string format
- You can only use one loop in your code
- You are not allowed to store characters in a variable
- You are not allowed to import any module

- **File:** [100-print_tebahpla.py]()
    
### 15. Remove at position
Write a function that creates a copy of the string, removing the character at the position `n` (not the Python way, the “C array index”).

- Prototype: `def remove_char_at(str, n):`
- You are not allowed to import any module
You don’t need to understand `__import__`

- **File:** [101-remove_char_at.py]()
    
### 16. ByteCode -> Python #2
Write the Python function `def magic_calculation(a, b, c):` that does exactly the same as the following Python bytecode:

  3           0 LOAD_FAST                0 (a)
              3 LOAD_FAST                1 (b)
              6 COMPARE_OP               0 (<)
              9 POP_JUMP_IF_FALSE       16

  4          12 LOAD_FAST                2 (c)
             15 RETURN_VALUE

  5     >>   16 LOAD_FAST                2 (c)
             19 LOAD_FAST                1 (b)
             22 COMPARE_OP               4 (>)
             25 POP_JUMP_IF_FALSE       36

  6          28 LOAD_FAST                0 (a)
             31 LOAD_FAST                1 (b)
             34 BINARY_ADD
             35 RETURN_VALUE

  7     >>   36 LOAD_FAST                0 (a)
             39 LOAD_FAST                1 (b)
             42 BINARY_MULTIPLY
             43 LOAD_FAST                2 (c)
             46 BINARY_SUBTRACT
             47 RETURN_VALUE
[tips - ByteCode](https://docs.python.org/3.4/library/dis.html)

- **File:** [102-magic_calculation.py]()
    