import sys
import os

dirname = __path__[0]
__path__.insert(0,os.path.join(dirname,'subfolder1'))
print(__path__)
__all__ = ['echo']