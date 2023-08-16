#include <stdio.h>
#include <Python.h>

/**
 * print_python_list - Prints basic information about Python lists.
 *
 * @p: Pointer to a Python object (assumed to be a list).
 */
void print_python_list(PyObject *p)
{
    Py_ssize_t size, i;
    PyObject *element;

    if (!PyList_Check(p))
    {
        printf("  [ERROR] Invalid List Object\n");
        return;
    }

    size = PyList_Size(p);

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);

    for (i = 0; i < size; i++)
    {
        element = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(element)->tp_name);
    }
}

/**
 * print_python_bytes - Prints basic information about Python bytes objects.
 *
 * @p: Pointer to a Python object (assumed to be a bytes object).
 */
void print_python_bytes(PyObject *p)
{
    Py_ssize_t size, i, limit;
    char *string;

    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_GET_SIZE(p);
    string = PyBytes_AsString(p);

    printf("[.] bytes object info\n");
    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", string);

    limit = (size > 10) ? 10 : size;

    printf("  first %ld bytes:", limit);

    for (i = 0; i < limit; i++)
        printf(" %02x", (unsigned char)string[i]);

    printf("\n");
}

int main(void)
{
    PyObject *list;
    PyObject *bytes;

    Py_Initialize();

    list = PyList_New(0);  // Create an empty list
    print_python_list(list);
    Py_DECREF(list);

    bytes = PyBytes_FromString("Hello, Python");
    print_python_bytes(bytes);
    Py_DECREF(bytes);

    Py_Finalize();

    return 0;
}
