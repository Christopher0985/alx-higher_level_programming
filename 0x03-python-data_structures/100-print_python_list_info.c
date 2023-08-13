#include <Python.h>

/**
 * print_python_list_info - Display basic information about Python lists.
 * @p: Pointer to a PyObject representing a list.
 */
void print_python_list_info(PyObject *p)
{
    int size, allocated, i;
    PyObject *item;

    size = Py_SIZE(p);
    allocated = ((PyListObject *)p)->allocated;

    printf("[*] Size of the Python List = %d\n", size);
    printf("[*] Allocated = %d\n", allocated);

    for (i = 0; i < size; i++)
    {
        printf("Element %d: ", i);

        item = PyList_GetItem(p, i);
        printf("%s\n", Py_TYPE(item)->tp_name);
    }
}
