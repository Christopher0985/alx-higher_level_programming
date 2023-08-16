#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - Prints information about Python bytes objects
 *
 * @p: Python Object
 * Return: No return value
 */
void print_python_bytes(PyObject *p)
{
	char *str;
	long int size, idx, limit;

	printf("[.] Bytes object information\n");
	if (!PyBytes_Check(p))
	{
		printf("	[ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)(p))->ob_size;
	str = ((PyBytesObject *)p)->ob_sval;

	printf("	Size: %ld\n", size);
	printf("	Data string: %s\n", str);

	if (size >= 10)
		limit = 10;
	else
		limit = size + 1;

	printf("	First %ld bytes:", limit);

	for (idx = 0; idx < limit; idx++)
		if (str[idx] >= 0)
			printf(" %02x", str[idx]);
		else
			printf(" %02x", 0x100 + str[idx]);

	printf("\n");
}

/**
 * print_python_list - Prints information about Python lists
 *
 * @p: Python Object
 * Return: No return value
 */
void print_python_list(PyObject *p)
{
	long int size, i;
	PyListObject *list;
	PyObject *obj;

	size = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;

	printf("[*] Python list information\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		obj = ((PyListObject *)p)->ob_item[i];
		printf("Element %ld: Type = %s\n", i, ((obj)->ob_type)->tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);
	}
}
