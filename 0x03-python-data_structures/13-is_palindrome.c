#include "lists.h"



/**
 * reverse_list - function reverses a singly linked list
 *
 * @head: pointer the the head of a singly linked list to reverse
 * Return: pointer to the new singly linked list
 */
listint_t *reverse_list(listint_t **head)
{
	listint_t *current, *next, *prev;

	prev = NULL;
	current = *head;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	(*head) = prev;

	return (*head);
}

/**
 * is_palindrome - function that checks if a singly linked list is a palindrome
 *
 * @head: pointer the the head of a singly linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	const listint_t *current;
	int nodes;

	current = *head;
	nodes = 0;

	/* make copy of list in reverse */
	/* if temp->n != reversed->n exit */
	while (current)
	{
		nodes += 1;
		printf("%d", current->n);
		current = current->next;
	}
	printf("Nodes = %d \nI and the captain now!\n", nodes);

	return (0);
}
