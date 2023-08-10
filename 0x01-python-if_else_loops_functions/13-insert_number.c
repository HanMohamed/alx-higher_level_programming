#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: pointer to pointer of first node of listint_t list
 * @number: integer to be included in new node
 *
 * Return: address of the new element or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current;
	listint_t *prev;
	listint_t *new_node;

	current = *head;

	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL)
	{
		*head = new_node;
		return (new_node);
	}

	prev = current;
	while (current)
	{
		if (current->n > number)
		{
			new_node->next = current;
			prev->next = new_node;
			return (new_node);
		}
		prev = current;
		current = current->next;
	}

	prev->next = new_node;
	return (new_node);
}
