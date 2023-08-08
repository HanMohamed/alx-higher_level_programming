#include "lists.h"

/**
 * check_cycle -  checks if a singly linked list has a cycle in it.
 * @list: head of list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
    listint_t *fast;
    listint_t *slow;

    if (!list || !list->next)
        return (0);
    
    slow = list;
    fast = list->next->next;
    
    while (fast && slow && fast->next)
    {
        if (fast == slow)
            return (1);
        fast = fast->next->next;
        slow = slow->next;
    }
    return (0);
}
