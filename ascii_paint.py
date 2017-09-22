import numpy as np
from skimage import io, transform
import sys


def convert_grey_to_ascii(grey):
    if grey > 0.8:
        return '  '
    if grey > 0.6:
        return '..'
    if grey > 0.5:
        return '--'
    if grey > 0.4:
        return 'OO'
    if grey > 0.2:
        return '**'
    else:
        return '##'


def main(argv):
    if len(argv) == 1:
        print '<usage> photo_name <optional>size_w size_h'
        return
    photo_name = argv[1]
    try:
        img = io.imread(photo_name, as_grey=True)
    except EOFError:
        print 'file not found'
        return

    output_size = (img.shape[0], img.shape[1])

    if len(argv) == 4:
        try:
            output_size = (int(argv[2]), int(argv[3]))
            img = transform.resize(img, output_size)
        except Exception:
            pass
    # print output_size
    output_format = ''
    for i in range(output_size[0]):
        output_format += 'puts("'
        for j in range(output_size[1]):
            output_format += convert_grey_to_ascii(img[i][j])
        output_format += '");\n'
    print output_format


if __name__ == '__main__':
    main(sys.argv)
