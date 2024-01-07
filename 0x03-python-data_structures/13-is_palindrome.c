#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to the head of the list
 * Return: 1 if palindrome, 0 otherwise
 */

int is_palindrome(listint_t **head)
{
listint_t *reversed_list = NULL;
listint_t *current_head = *head;
listint_t *copied_list = NULL;
listint_t *copied_list_ptr = NULL;

if (*head == NULL || current_head->next == NULL)
	return (1);

while (current_head != NULL)
{
	listint_t *new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
	{
		free_listint(reversed_list);
		return (0);
	}
	new_node->n = current_head->n;
	new_node->next = reversed_list;
	reversed_list = new_node;

	add_nodeint_end(&copied_list, current_head->n);
	current_head = current_head->next;
	copied_list_ptr = copied_list;
}
while (*head != NULL && copied_list_ptr != NULL)
{
	if ((*head)->n != copied_list_ptr->n)
	{
		free_listint(reversed_list);
		free_listint(copied_list);
		return (0);
	}
*head = (*head)->next;
copied_list_ptr = copied_list_ptr->next;
}
free_listint(reversed_list);
free_listint(copied_list);
return (0);
}
