#include <stdio.h>
#include <Python.h>

/**
 * byte_info - Displays information about bytes
 *
 * @python_obj: Python object
 * Return: No return value
 */
void byte_info(PyObject *python_obj)
{
    char *str;
    long int size, i, limit;

    printf("[.] bytes object information\n");
    if (!PyBytes_Check(python_obj))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = ((PyVarObject *)(python_obj))->ob_size;
    str = ((PyBytesObject *)python_obj)->ob_sval;

    printf("  size: %ld\n", size);
    printf("  attempting string: %s\n", str);

    if (size >= 10)
        limit = 10;
    else
        limit = size + 1;

    printf("  first %ld bytes:", limit);

    for (i = 0; i < limit; i++)
        if (str[i] >= 0)
            printf(" %02x", str[i]);
        else
            printf(" %02x", 256 + str[i]);

    printf("\n");
}

/**
 * list_info - Displays information about a list
 *
 * @python_obj: Python object
 * Return: No return value
 */
void list_info(PyObject *python_obj)
{
    long int size, i;
    PyListObject *lst;
    PyObject *object;

    size = ((PyVarObject *)(python_obj))->ob_size;
    lst = (PyListObject *)python_obj;

    printf("[*] Python list information\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", lst->allocated);

    for (i = 0; i < size; i++)
    {
        object = ((PyListObject *)python_obj)->ob_item[i];
        printf("Element %ld: %s\n", i, ((object)->ob_type)->tp_name);
        if (PyBytes_Check(object))
            byte_info(object);
    }
}

