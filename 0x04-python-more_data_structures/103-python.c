#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - Prints basic info about a Python list.
 * @p: Pointer to a Python object (assumed to be a list).
 */
void print_python_list(PyObject *p) {
    if (PyList_Check(p)) {
        Py_ssize_t size = PyList_Size(p);
        Py_ssize_t i;

        printf("[*] Python list info\n");
        printf("[*] Size of the Python List = %ld\n", size);
        printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
        for (i = 0; i < size; i++) {
            PyObject *item = PyList_GetItem(p, i);
            const char *typeName = Py_TYPE(item)->tp_name;
            printf("Element %ld: %s\n", i, typeName);
        }
    }
}

/**
 * print_python_bytes - Prints basic info about a Python bytes object.
 * @p: Pointer to a Python object (assumed to be a bytes object).
 */
void print_python_bytes(PyObject *p) {
    if (PyBytes_Check(p)) {
        Py_ssize_t size = PyBytes_Size(p);
        Py_ssize_t i;

        printf("[.] bytes object info\n");
        printf("  size: %ld\n", size);
        printf("  trying string: %s\n", PyBytes_AsString(p));
        printf("  first %ld bytes: ", size + 1);
        if (size + 1 >= 10)
            size = 10;
        for (i = 0; i < size + 1; i++)
            printf("%02x%c",
                   (unsigned char)PyBytes_AsString(p)[i],
                   i < size ? ' ' : '\n');
    } else {
        printf("[ERROR] Invalid Bytes Object\n");
    }
}
