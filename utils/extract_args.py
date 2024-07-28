import sys

def is_float(element):
    if element is None:
        return False
    try:
        float(element)
        return True
    except ValueError:
        return False


def extract_args():
    args = {}

    if not isinstance(sys.argv, list):
        return args

    for i in range(len(sys.argv)):
        # start of argument
        if (sys.argv[i].startswith('-')):
            key = sys.argv[i][1:]
            value = sys.argv[i + 1]

            # integer
            if value.isdigit():
                args[key] = int(value)

            # float
            elif is_float(value):
                args[key] = float(value)

            # boolean
            elif value.lower() in ["true", "false"]:
                args[key] = value.lower() == "true"

            # string
            else:
                args[key] = value

    return args


if __name__ == "__main__":
    print(extract_args())
