#include "lists.h"

/**
 * reverse_list - function reverses a singly linked list
 *
 * @head: pointer the the head of a singly linked list to reverse
 * Return: pointer to the new singly linked list
 */
listint_t *reverse_list(listint_t **head)
{
	listint_t *current = NULL;
	listint_t *next = NULL;
	listint_t *prev = NULL;

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
	listint_t *current = NULL;
	listint_t *reversed = NULL;
	listint_t *temp = NULL;
	int len = 0, i = 0, flag;

	current = *head;
	temp = *head;
	flag = 1;

	if (head == NULL)
		return (0);
	if (*head == NULL || (*head)->next == NULL)
		return (1);
	for (; temp; len++)
		temp = temp->next;
	printf("There are %d nodes in this list\nI am the captain now!\n", len);
	for (i = 0; i < len / 2; i++, current = current->next)
	{
		add_nodeint_end(&reversed, current->n);
		printf("Inside for loop: current list %d\t", current->n);
		printf("Inside for loop: reversed list %d\n", reversed->n);
	}
	current = *head;
	for (; current; current = current->next, reversed = reversed->next)
	{
		printf("While loop list: %d\t", current->n);
		printf("Reversed list: %d\n", reversed->n);
		current = current->next;
		reversed = reversed->next;
		/*if (current->n != reversed->n)*/
		{
/*			flag = 0;*/
/*			break;*/
		}
		printf("Hot\n");
	}
	printf("Sandwich\n");
	free_listint(reversed);

	return (flag);
}
