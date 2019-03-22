import os


def function_parsing(members):
    """
    parsing all the public member functions of the header file
    param: functions is a list of all the methods
    """
    name = []
    return_type = []
    is_virtual = []
    is_static = []
    arguments = []
    for member in members:
        name.append(member[0].split(": ")[1].strip().replace("'", ""))
        return_type.append(member[6].split(": ")[1].strip())
        is_virtual.append(member[10].split(": ")[1].strip())
        is_static.append(member[14].split(": ")[1].strip())
        arguments.append(member[7].split(": ")[1].strip())

    return name, return_type, is_virtual, is_static, arguments
