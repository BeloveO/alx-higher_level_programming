#include "lists.h"
#include <stdlib.h>
/**
 * check_cycle - To check if a singly linked list has a cycle in it
 * @list: singly linked list
 * Return: 0 for no cycle and 1 if otherwise
*/

int check_cycle(listint_t *list)
{
	listint_t *a, *b;
	
	a = list;
	b = list;

	while (list && a && a->next)
	{
		list = list->next;
		a = a->next->next;
		if (list == a)
		{
			list = b;
			b = a;
			while (1)
			{
				a = b;
				while (a->next != list && a != b)
				{
					a = a->next;
				}
				if (a->next == list)
					break;
				list = list->next;
			}
			
			return (1);
		}
	}

	return (0);
	
}
