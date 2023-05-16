#include <stdio.h>
#include <Python.h>
/**
 * print_python_list_info - Prints basic info about Python lists
 * @p: PyObject list
*/
void print_python_list_info(PyObject *p)
{
	long int size, i;
	PyListObject *list;
	PyObject *obj;

	size = Py_SIZE(p);
	list = (PyListObject *)p;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocaated = %ld\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		obj = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(obj)->tp_name);
	}
}

