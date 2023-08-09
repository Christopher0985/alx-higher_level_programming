#include "lists.h"

/**
 * check_cycle - Determines whether a linked list contains a cycle
 * @head: Pointer to the beginning of the linked list
 *
 * Returns: 1 if a cycle is present in the list, 0 if no cycle.
 * A cycle is a repeating pattern of nodes that connect back to a previous node
 */
int check_cycle(listint_t *head)
{
	listint_t *turtle = head;
	listint_t *hare = head;

	if (!head)
		return (0);

	while (turtle && hare && hare->next)
	{
		turtle = turtle->next;
		hare = hare->next->next;
		if (turtle == hare)
			return (1);
	}

	return (0);
}
