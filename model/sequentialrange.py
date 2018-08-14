#! /usr/bin/env python
# This free software incorporates by reference the text of the WTFPL, Version 2

"""
This is where your module level help string goes.

.. module:: `sequentialrange`
   :platform: Unix, Windows
   :synopsis: Put a synopsis of what this module does here.

.. moduleauthor:: Michael Dinitz
"""

# IMPORT STANDARD MODULES
# import standard modules here

# IMPORT LOCAL MODULES
from terminallogger import get_terminal_logger

LOGGER = get_terminal_logger(__name__)

class SequentialRange(set):
    def __init__(self, iterable):
        super(SequentialRange, self).__init__(iterable)
    # end __init__
    
    def __repr__(self):
        """
        If the record does is not logging.INFO, return True
        """
        return ", ".join([str(i) for i in sorted(self)])
        pass
    # end __repr__
# end SequentialRange

def get_sequential_range(iterable):
    """
    Help string that describes my_dummy_function
    
    :arg somearg: describe what somearg is
    :type somearg: type of somearg
    :returns: what this function returns
    :rtype: type of the returned object
    """
    return SequentialRange(iterable)
# end my_dummy_function

def main():
    """
    Simply run help if called directly.
    """ 
    print(get_sequential_range(range(1,24,2)))
    
# end main

__all__ = ['MyDummyClass', 'my_dummy_function']

if __name__ == '__main__':
    main()
    
