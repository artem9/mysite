import os


def read_key(filename):
    key = None
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    key_file = os.path.join(cur_dir, filename)

    try:
        with open(key_file, 'r') as f:
            key = f.readline()
    except:
        raise IOError('key file not found')

    return key


if __name__ == "__main__":
    print(read_key('gmail.key'))
