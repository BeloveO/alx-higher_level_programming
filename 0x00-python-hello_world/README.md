# 0x00. Python - Hello, World
## Tasks

### 0. Run Python file
Write a Shell script that runs a Python script.
- The Python file name will be saved in the environment variable $PYFILE

- **File:** [0-run]

### 1. Run inline
Write a Shell script that runs Python code.

The Python code will be saved in the environment variable `$PYCODE`

- **File:** [1-run_inline]()
    
### 2. Hello, print
Write a Python script that prints exactly `"Programming is like building a multilingual puzzle`, followed by a new line.

- Use the function `print`

- **File:** [2-print.py]()
    
### 3. Print integer
Complete this source code in order to print the integer stored in the variable `number`, followed by `Battery street`, followed by a new line.

- You can find the source code [here](https://github.com/holbertonschool/0x00.py/blob/e1849362fbf39651bc4e641ba198e3d5fa5688e9/3-print_number.py)
- The output of the script should be:
  - the number, followed by `Battery street`,
  - followed by a new line
- You are not allowed to cast the variable `number` into a string
- Your code must be 3 lines long
- You have to use f-strings [tips](https://realpython.com/python-f-strings/)

- **File:** [3-print_number.py]()
    
### 4. Print float
Complete the source code in order to print the float stored in the variable `number` with a precision of 2 digits.

- You can find the source code [here](https://github.com/holbertonschool/0x00.py/blob/e1849362fbf39651bc4e641ba198e3d5fa5688e9/4-print_float.py)
- The output of the program should be:
  - `Float:`, followed by the float with only 2 digits
  - followed by a new line
- You are not allowed to cast `number` to string
- You have to use f-strings

- **File:** [4-print_float.py]()
    
### 5. Print string
Complete this source code in order to print 3 times a string stored in the variable str, followed by its first 9 characters.

- You can find the source code [here](https://github.com/holbertonschool/0x00.py/blob/e1849362fbf39651bc4e641ba198e3d5fa5688e9/5-print_string.py)
- The output of the program should be:
  - 3 times the value of `str`
  - followed by a new line
  - followed by the 9 first characters of `str`
  - followed by a new line
- You are not allowed to use any loops or conditional statement
- Your program should be maximum 5 lines long

- **File:** 5-print_string.py
    
### 6. Play with strings
Complete this source code to print Welcome to Holberton School!

You can find the source code [here](https://github.com/holbertonschool/0x00.py/blob/e1849362fbf39651bc4e641ba198e3d5fa5688e9/6-concat.py)
- You are not allowed to use any loops or conditional statements.
- You have to use the variables `str1` and `str2` in your new line of code
- Your program should be exactly 5 lines long

- **File:** [6-concat.py]()
    
### 7. Copy - Cut - Paste
Complete this source code

- You can find the source code [here](https://github.com/holbertonschool/0x00.py/blob/e1849362fbf39651bc4e641ba198e3d5fa5688e9/7-edges.py)
- You are not allowed to use any loops or conditional statements
- Your program should be exactly 8 lines long
- `word_first_3` should contain the first 3 letters of the variable `word`
- `word_last_2` should contain the last `2` letters of the variable `word`
- `middle_word` should contain the value of the variable `word` without the first and last letters

- **File:** [7-edges.py]()
    
### 8. Create a new sentence
Complete this source code to print object-oriented programming with Python, followed by a new line.

- You can find the source code here
- You are not allowed to use any loops or conditional statements
- Your program should be exactly 5 lines long
- You are not allowed to create new variables
- You are not allowed to use string literals

- **File:** [8-concat_edges.py]()
    
### 9. Easter Egg
Write a Python script that prints “The Zen of Python”, by TimPeters, followed by a new line.

  - Your script should be maximum 98 characters long (please check with `wc -m 9-easter_egg.py`)
```
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```
- **File:** [9-easter_egg.py]()
    
### 10. Linked list cycle
Technical interview preparation:

  - You are not allowed to google anything
  - Whiteboard first
  - This task and all future technical interview prep tasks will include checks for the efficiency of your solution, i.e. is your solution’s runtime fast enough, does your solution require extra memory usage / mallocs, etc.
- Write a function in C that checks if a singly linked list has a cycle in it.

  - Prototype: `int check_cycle(listint_t *list);`
  - Return: `0` if there is no cycle, `1` if there is a cycle
- Requirements:

  - Only these functions are allowed: `write`, `printf`, `putchar`, `puts`, `malloc`, `free`
```
**cat lists.h**

#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

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
listint_t *add_nodeint(listint_t **head, const int n);
void free_listint(listint_t *head);
int check_cycle(listint_t *list);

#endif /* LISTS_H */

**cat 10-linked_lists.c**

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
 * add_nodeint - adds a new node at the beginning of a listint_t list
 * @head: pointer to a pointer of the start of the list
 * @n: integer to be included in node
 * Return: address of the new element or NULL if it fails
 */
listint_t *add_nodeint(listint_t **head, const int n)
{
    listint_t *new;

    new = malloc(sizeof(listint_t));
    if (new == NULL)
        return (NULL);

    new->n = n;
    new->next = *head;
    *head = new;

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
- **File:** [10-check_cycle.c](), [lists.h]()
    
### 11. Hello, write
Write a Python script that prints exactly `and that piece of art is useful - Dora Korpar, 2015-10-19`, followed by a new line.

- Use the function write from the `sys` module
- You are not allowed to use `print`
- Your script should print to `stderr`
- Your script should exit with the status code `1`

- **File:** [100-write.py]()
    
### 12. Compile
Write a script that compiles a Python script file.

The Python file name will be stored in the environment variable `$PYFILE`

The output filename has to be `$PYFILEc` (ex: `export PYFILE=my_main.py` => output filename: `my_main.pyc`)

- **File:** [101-compile]()
    
### 13. ByteCode -> Python #1
Write the Python function `def magic_calculation(a, b):` that does exactly the same as the following Python bytecode:
```

  3           0 LOAD_CONST               1 (98)
              3 LOAD_FAST                0 (a)
              6 LOAD_FAST                1 (b)
              9 BINARY_POWER
             10 BINARY_ADD
             11 RETURN_VALUE
```
- Tip: [Python bytecode](https://docs.python.org/3.4/library/dis.html)
- **File:** [102-magic_calculation.py]()
