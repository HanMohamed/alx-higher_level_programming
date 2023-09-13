#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: a pointer to a singly linked list
 *
 * An empty list is considered a palindrome
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *current, *tail;
	int len, half, i, j;

	if (!head || !*head)
		return (1);
	tail = *head;

	for (len = 0; tail; len++)
		tail = tail->next;

	half = len / 2;
	current = *head;
	for (i = 0; i < half; i++)
	{
		tail = *head;
		for (j = 1; j < (len - i); j++)
			tail = tail->next;
		if (current->n != tail->n)
			return (0);
		current = current->next;
	}
	return (1);
}
