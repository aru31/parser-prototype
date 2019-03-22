import sys
import text_parser


def AbstractASTGenerator(parser, filename):
    """
    Abstract parser implementation
    """
    try:
        if parser.lower() == 'clang':
            print('This is demo for pygccxml parser, :)')
        elif parser.lower() == 'pygccxml':
            text_parser.pygccxml_text_parser(filename)
    except Exception:
        pass


def InitailParserInput():
    """
    Parser Type Input
    """
    parser_list = [
        'clang',
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
