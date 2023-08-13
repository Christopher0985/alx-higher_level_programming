#include "lists.h"

/**
 * reverse_listint - Reverses a singly-linked list of integers.
 * @head: A pointer to the starting node of the list to be reversed.
 *
 * Return: A pointer to the head of the reversed list.
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *current = *head, *next, *previous = NULL;

	while (current)
	{
		next = current->next;
		current->next = previous;
		previous = current;
		current = next;
	}

	*head = previous;
	return (*head);
}

/**
 * is_palindrome - Determines if a singly linked list is a palindrome.
 * @head: A pointer to the head of the linked list.
 *
 * Return: 1 if the linked list is a palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp, *reversed, *middle;
	size_t list_size = 0, i;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	temp = *head;
	while (temp)
	{
		list_size++;
		temp = temp->next;
	}

	temp = *head;
	for (i = 0; i < (list_size / 2) - 1; i++)
		temp = temp->next;

	if ((list_size % 2) == 0 && temp->n != temp->next->n)
		return (0);

	temp = temp->next->next;
	reversed = reverse_listint(&temp);
	middle = reversed;

	temp = *head;
	while (reversed)
	{
		if (temp->n != reversed->n)
			return (0);
		temp = temp->next;
		reversed = reversed->next;
	}
	reverse_listint(&middle);

	return (1);
}
