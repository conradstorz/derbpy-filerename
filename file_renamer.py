import re
import os
import sys


TAPE_INFO_REGEX = re.compile(r'^Tape(\d+)\s+Side(\d)$')


class TitleRenameException(Exception):
    '''Throw when you mess up'''

def rename_files(directory):

    for file in os.listdir(directory):
        new_file_name = filenamer(title_parser(file))

        print 'Renaming', file, 'to',  new_file_name

        new_file_name = os.path.join(directory, new_file_name)
        old_file_name = os.path.join(directory, file)
        os.rename(old_file_name, new_file_name)

def filenamer(new_file):
    file_format = '{tape_number}{side_id}{sub_chapter}_{title}.{file_type}'
    return file_format.format(**new_file)

def title_parser(title):
    '''Takes a title and returns it's parts'''

    title_parts = {
        'title_id': None,
        'tape_number': None,
        'side_id': None,
        'title': None,
        'sub_chapter': None,
        'file_type': None
    }

    try:
        title_id, tape_info, title_ext = map(str.strip, title.split('-'))
    except ValueError, e:
        raise TitleRenameException('Improper file name format, invalid number of dashes.')
        #title_id, tape_info, title_ext = ('', '', '')

    try:
        tape_number, side_number = TAPE_INFO_REGEX.match(tape_info).groups()
    except (TypeError, AttributeError), e:
        raise TitleRenameException('Tape name and side number are not formated correctly')
        #tape_number, side_number = ('', '')

    try:
        title_subchapter, file_extension = os.path.splitext(title_ext)
    except:
        raise TitleRenameException('Problem splitting file subchapter from filetype.')

    last_space_index = title_subchapter.rfind(' ')

    if last_space_index == -1:
        raise TitleRenameException('Unable to find a sub chapter')

    sub_chapter = title_subchapter[last_space_index:].strip()

    two_digit_format = '{:02d}'

    def integerize(num):
        try:
            return int(num)
        except:
            raise TitleRenameException('Could not convert {} to Integer'.format(num))

    title_parts['title_id'] = two_digit_format.format(integerize(title_id))
    title_parts['tape_number'] = two_digit_format.format(integerize(tape_number))
    title_parts['title'] = title_subchapter[:last_space_index].strip()
    title_parts['sub_chapter'] = two_digit_format.format(integerize(sub_chapter))

    try:
        title_parts['side_id'] = ('_1_', '_2_')[integerize(side_number) - 1]
    except IndexError, e:
        raise TitleRenameException('The side number is not 1 or 2')

    title_parts['file_type'] = file_extension[1:]

    return title_parts

if __name__ == '__main__':
    path_to_files = '/Volumes/PENDRIVE/LRH_BE_normalized_Chapterized'
    sys.exit(rename_files(path_to_files))
