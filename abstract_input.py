import sys
import yaml_generator


def AbstractASTGenerator(parser, filename):
    """
    Abstract parser implementation
    """
    try:
        if parser.lower() == 'pygccxml':
            yaml_generator.convert_yaml(filename)
    except Exception:
        pass


def InitailParserInput():
    """
    Parser Type Input
    """
    parser_list = [
        'pygccxml',
    ]
    parser = input('Parser type(' + '/'.join(parser_list) + '): ')
    if parser.lower() in parser_list:
        AbstractASTGenerator(parser.lower(), sys.argv[1])
    else:
        raise Exception('Please specify a valid parser name!')


def main():
    InitailParserInput()


if __name__ == '__main__':
    if len(sys.argv) == 2:
        main()
    else:
        raise Exception('Please input only one header file!')
