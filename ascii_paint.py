# -*- coding:utf-8 -*-

from skimage import io, transform
import sys


class AsciiPaint:
    def __init__(self, photo_path):
        self.__img = io.imread(photo_path, as_grey=True)

    def get_QRcode(self, output_size=None, format_pre='', format_fin=''):
        if output_size is None:
            img = self.__img
        else:
            img = transform.resize(self.__img, output_size)

        output_format = ''
        for i in range(output_size[0]):
            output_format += format_pre
            for j in range(output_size[1]):
                output_format += (lambda x: '  ' if x > 0.8 else '██')(img[i][j])
            output_format += format_fin + '\n'
        return output_format

    def get_ascii_paint(self, output_size=None, format_pre='', format_fin=''):
        if output_size is None:
            img = self.__img
        else:
            img = transform.resize(self.__img, output_size)
        output_size = img.shape
        output_format = ''
        for i in range(output_size[0]):
            output_format += format_pre
            for j in range(output_size[1]):
                output_format += self._convert_grey_to_ascii(img[i][j])
            output_format += format_fin + '\n'
        return output_format

    @staticmethod
    def _convert_grey_to_ascii(grey):
        if grey > 0.8:
            return '  '
        # return '██'
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
    ap = AsciiPaint(photo_name)
    if len(argv) == 4:
        try:
            output_size = (int(argv[2]), int(argv[3]))
        except ValueError:
            print 'parse size error'
            return
        print ap.get_ascii_paint(output_size=output_size)
        return
    print ap.get_ascii_paint()


if __name__ == '__main__':
    main(sys.argv) 
