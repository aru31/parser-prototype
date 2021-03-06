import ast_generator
import method_parsing

from itertools import cycle


def pygccxml_text_parser(filename):
    """
    Parsing the abstract representation generated by pygccxml
    : class_name a bit hardcoded so namespace specified explicitly
    """
    # Need to implement a function to store the output in form of txt file
    with open('pygccxml_ast.txt', 'r') as file_object:
        lines = file_object.readlines()

    namespace_name = []
    namespace_index = []
    for line in lines:
        if 'namespace_t' in line:
            namespace_name.append(line.split(": ")[1].strip().replace("'", ""))
            namespace_index.append(lines.index(line))

    if namespace_name[0] == 'sample_namespace':
        lines = lines[0:]
    else:
        raise Exception('Wrongly specified namespace!')

    class_name = []
    class_index = []
    for line in lines:
        if 'class_t' in line:
            class_name.append(line.split(": ")[1].strip().replace("'", ""))
            class_index.append(lines.index(line))
    class_index.append(len(lines))

    classes = []
    running = True
    licycle = cycle(class_index)
    nextelem = next(licycle)
    while running:
        thiselem, nextelem = nextelem, next(licycle)
        classes.append(lines[thiselem:nextelem])
        if nextelem == class_index[0]:
            running = False
    classes.pop()

    # Parisng of public constructor only
    getter_index = []
    public_constructor = []
    for line in lines:
        if 'public' in line:
            getter_index.append(lines.index(line))
        if 'protected' in line:
            getter_index.append(lines.index(line))
        if 'private' in line:
            getter_index.append(lines.index(line))

    public_constructor = lines[getter_index[0]: getter_index[1]]
    public_member_function_index = []
    public_member_function = []

    for line in public_constructor:
        if 'member_function_t' in line:
            public_member_function_index.append(public_constructor.index(line))

    """
    member_function_t is the leaf node of the whole tree, so we precisly
    know the length taken by the member_function_t because of the way helper
    function is defined
    : Size of member_function_t is 16 lines
    """
    for i in public_member_function_index:
        public_member_function.append(public_constructor[i: i+16])

    name, return_type, is_virtual, is_static, arguments = method_parsing.function_parsing(
        public_member_function)
    parsed_data = list(
        zip(name, return_type, is_virtual, is_static, arguments))
    return parsed_data
