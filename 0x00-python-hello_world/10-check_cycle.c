#include "lists.h"
/**
 * check_cycle - To check if a singly linked list has a cycle in it
 * @list: singly linked list
 * Return: 0 for no cycle and 1 if otherwise
*/

int check_cycle(listint_t *list)
{
	listint_t *a, *b;

	if (list == NULL || list->next == NULL)
		return (0);
	
	a = list->next;
	b = list->next->next;

	while (a && b && b->next)
	{
		if (a == b)
			return (1);
		
		a = a->next;
		b ->next;
	}

	return (0);
	
}
