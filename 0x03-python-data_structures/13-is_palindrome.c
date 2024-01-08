#include "lists.h"

/**
  *reverse_l - Reverses linked list.
  *@head: Double pointer to the head of the list.
  *Return: Pointer to new head of reversed list
  */

listint_t *reverse_l(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *active = *head;
	listint_t *next;

	while (active != NULL)
	{
		next = active->next;
		active->next = prev;
		prev = active;
		active = next;
	}

	*head = prev;
	return (*head);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to the head of the list
 * Return: 1 if palindrome, 0 otherwise
 */

int is_palindrome(listint_t **head)
{
listint_t *slug = *head, *rapid = *head;
listint_t *prev_slow_ptr = *head, *middle = NULL;
int is_palindrome = 1;

if (*head == NULL || (*head)->next == NULL)
	return (is_palindrome);
while (rapid != NULL && rapid->next != NULL)
{
	rapid = rapid->next->next;
	prev_slow_ptr = slug;
	slug = slug->next;
}
if (rapid != NULL)
{
	middle = slug;
	slug = slug->next;
}
prev_slow_ptr->next = NULL;
reverse_l(&slug);
listint_t *l_1 = *head;
listint_t *l_2 = slug;
while (l_1 != NULL && l_2 != NULL)
{
	if (l_1->n != l_2->n)
	{
		is_palindrome = 0;
		break;
	}
	l_1 = l_1->next;
	l_2 = l_2->next;
}
reverse_l(&slug);
if (middle != NULL)
{
	prev_slow_ptr->next = middle;
	middle->next = slug;
}
else
prev_slow_ptr->next = slug;
return (is_palindrome);
}
