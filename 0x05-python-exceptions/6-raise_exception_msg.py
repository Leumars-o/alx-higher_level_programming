#!/usr/bin/python3
"""A function that raises a name exception with a message.

Parameter:
    @message: Name exception message to be raised
Return:
    - None
Description:
    - No modules should be imported
"""


def raise_exception_msg(message=""):
    try:
        raise NameError
    except NameError:
        print("{}".format(message))
