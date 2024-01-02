#include "lists.h"

/**
  *check_cycle - checks list for a cycle
  *@list: list to check for cycle
  *Return: 1 if list has cycle, 0 not
  */
int check_cycle(listint_t *list)
{
	listint_t *list_check_s = list;
	listint_t *list_check_f = list;

	if (list == NULL)
	{
		return (0);
	}

	while (list_check_s && list_check_f && list_check_f->next)\
	{
		list_check_s = list_check_s->next;
		list_check_f = list_check_f->next->next;

		if (list_check_s == list_check_f)
		{
			return (1);
		}
	}

	return (0);
}
