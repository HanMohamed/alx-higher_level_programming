#include <stdio.h>
#include <Python.h>

void print_python_list_info(PyObject *p)
{
	int len_list, i;

	for (len_list = 0; p; len_list++)
		;
	printf("[*] Size of the Python List = %d\n", len_list);
	printf("[*] Allocated = %d\n", len_list);
	for (i = 0; p; i++)
		printf("Element %d: %s\n", i, Py_TYPE(p));
}
