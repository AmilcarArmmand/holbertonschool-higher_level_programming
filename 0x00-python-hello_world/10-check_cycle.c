#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks for a cycle in a linked list
 * @list: pointer to elements of a linked list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *tortoise;
	listint_t *hare;

/* check if list exists and has more than 1 element */
	if (list == NULL || list->next == NULL)
		return (0);

	tortoise = list;
	hare = list->next;

	while (tortoise && hare && hare->next)
	{
		if (tortoise == hare)
			return (1);

/* slow pointer moves 1 step forward while fast pointer moves 2 steps */
		tortoise = tortoise->next;
		hare = (hare->next)->next;
	}

	return (0);
}
