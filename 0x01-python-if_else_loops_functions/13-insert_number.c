#include "lists.h"

/**
  *insert_node - inserts a number into a list
  *@head: beginning of list
  *@number: number to be added to list
  *Return: address of the new node, or NULL if it failed
  */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *nav = *head;
	listint_t *new_val;

	new_val = malloc(sizeof(listint_t));
	if (!new_val)
	{
		return (NULL);
	}
	new_val->n = number;
	new_val->next = NULL;
	
	if (nav->n >= number || nav == NULL)
	{
		new_val->next = nav;
		*head = new_val;
		return (new_val);
	}

	while (nav && nav->next && nav->next->n < number)
	{
		nav = nav->next;
	}
	new_val->next = nav->next;
	nav->next = new_val;

	return(new_val);
}
