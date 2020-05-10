#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to pointer of structs in a singly linked list
 * @number: data to insert into new node
 *
 * Return: the address of the new node or NULL if (failure)
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;

/* if the list is empty or number > list.numbers */
	if (head == NULL || *head == NULL)
		return (add_nodeint_end(head, number));

	current = *head;

	while (current != NULL)
	{
		if ((number >= current->n) && current->next == NULL)
			return (add_nodeint_end(head, number));

		if (number <= (current->next)->n)
			break;
		current = (current->next);
	}

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;

	new->next = current->next;
	current->next = new;


	return (new);
}
