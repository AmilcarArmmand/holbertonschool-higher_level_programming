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
	listint_t *current, *rev;

	current = *head;
	rev = NULL;

	if (head == NULL)
		return (0);

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	rev = reverse_list(&current);
	while (current)
	{
		if (current->n != rev->n)
		{
			free(rev);
			return (0);
		}
		current = current->next;
		rev = rev->next;
	}
	free(rev);

	return (1);
}
