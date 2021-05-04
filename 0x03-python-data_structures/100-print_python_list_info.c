#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <ctype.h>
#include <stdarg.h>

/**
 * print_python_list_info - function that prints CPython reference info
 *
 * @p: pointer to a PyObject datatype structure
 * Return: No return value
 */
void print_python_list_info(PyObject *p)
{
	/* elements in the PyObjectlist */
	Py_ssize_t list_size = NULL;

typedef Py_ssize_t (*lenfunc)(PyObject *);
typedef PyObject *(*ssizeargfunc)(PyObject *, Py_ssize_t);
typedef PyObject *(*ssizessizeargfunc)(PyObject *, Py_ssize_t, Py_ssize_t);
typedef PyObject *(*ssizessizeargfunc)(PyObject *, Py_ssize_t, Py_ssize_t);
typedef int(*ssizeobjargproc)(PyObject *, Py_ssize_t, PyObject *);
typedef int(*ssizessizeobjargproc)(PyObject *, Py_ssize_t, Py_ssize_t, PyObject *);
typedef int(*ssizessizeobjargproc)(PyObject *, Py_ssize_t, Py_ssize_t, PyObject *);


	/* initialize */
	list_size = PyList_Size(p);
	/* what does this do */

	printf("[*] Size of the Python List = %d\n", (int)list_size);
/*	printf("[*] Allocated = %d\n", nodes_allocated_maybe_size_t); */
/*	while (p)  */
/*	{ loop through the elements in p that are not NULL  */
	/*	printf("Element %d: %s\n", p->element[i], p->type);  */
/*	}  */
}
