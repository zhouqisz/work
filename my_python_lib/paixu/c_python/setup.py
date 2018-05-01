from distutils.core import setup
from Cython.Build import cythonize
#from Cython.Compiler import OPtions

setup(ext_modules = cythonize("foo.pyx"))
