from pygccxml import utils
from pygccxml import declarations
from pygccxml import parser


def pygccxml_parser(filename):
    """
    Implementation of pygccxml parser
    """
    generator_path, generator_name = utils.find_xml_generator()

    # Configure the xml generator
    xml_generator_config = parser.xml_generator_configuration_t(
        xml_generator_path=generator_path,
        xml_generator=generator_name)
    filename = filename
    decls = parser.parse([filename], xml_generator_config)

    global_namespace = declarations.get_global_namespace(decls)
    ns = global_namespace.namespace("sample_namespace")
    return declarations.print_declarations(ns)
