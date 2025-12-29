import argparse
import hashlib
import os

def get_path_to(name) -> str:
    return f'{os.path.dirname(os.path.realpath(__file__))}/{name}'

def main():
    parser = argparse.ArgumentParser(
        prog='SHIT (the Simple Hack for Incremental Tracking)',
        description='[track the current build number for a specific project]',
        epilog='see <https://github.com/racc0x2/SHIT>',
    )

    parser.add_argument('-o', '--output')
    parser.add_argument('-t', '--template')
    parser.add_argument('-i', '--identifier')

    args = parser.parse_args()

    if args.identifier is None:
        parser.print_help()
        exit(0)

    sha256 = hashlib.sha256(args.identifier.encode('utf-8')).hexdigest()
    file = get_path_to(sha256)

    if os.path.isfile(file):
        with open(file, 'r') as f:
            build_number = int(f.read()) + 1
    else:
        build_number = 1

    with open(file, 'w') as f:
        f.write(str(build_number))

    if args.template is None:
        output = build_number
    else:
        with open(args.template, 'r') as f:
            template = f.read()

        output = template.format(build_number)

    if args.output is None:
        print(output)
    else:
        with open(args.output, 'w') as f:
            f.write(output)

if __name__ == '__main__':
    main()