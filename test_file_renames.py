'''
Given a filename of format with the following sections separated by a space,

1. A two digit number : ID
2. A dash : ID Separator
3. The word Tape followed by a number : Tape number
4. The word Side followed by a number : Side ID
5. A dash : Title Separator
6. A Title (which could have a space) ***** : Title
7. A single or two digit number : Chapter number
8. The file type

'30 - Tape30 Side2 - L. Ron Hubbard 1.mp3'

Write a function which returns a dictionary of the individual parts except the separators.
'''

from file_renamer import title_parser, filenamer

VALID = True 
INVALID = False 

correct_title_names = [
    (VALID,
    '30 - Tape30 Side2 - L. Ron Hubbard 1.mp3',
    {   'title_id': '30',
        'tape_number': '30',
        'side_id': '_2_',
        'title': 'L. Ron Hubbard',
        'sub_chapter': '01',
        'file_type': 'mp3'
    },
    '30_2_01_L. Ron Hubbard.mp3'
    ),
    (VALID,
    '17 - Tape10 Side1 - Battlefield Earth 20.mp4a',
    {   'title_id': '17',
        'tape_number': '10',
        'side_id': '_1_',
        'title': 'Battlefield Earth',
        'sub_chapter': '20',
        'file_type': 'mp4a'
    },
    '10_1_20_Battlefield Earth.mp4a'
    ),
    (VALID,
    '12 - Tape1 Side1 - Battlefield Earth 3.flac',
    {   'title_id': '12',
        'tape_number': '01',
        'side_id': '_1_',
        'title': 'Battlefield Earth',
        'sub_chapter': '03',
        'file_type': 'flac'
    },
    '01_1_03_Battlefield Earth.flac'
    ),
    (VALID,
    '1 - Tape01 Side1 - Battlefield Earth 3.flac',
    {   'title_id': '01',
        'tape_number': '01',
        'side_id': '_1_',
        'title': 'Battlefield Earth',
        'sub_chapter': '03',
        'file_type': 'flac'
    },
    '01_1_03_Battlefield Earth.flac'
    ),
    (INVALID,
    '33 - Tape01Side2 - Battlefield Earth 3.ogg',
    {   'title_id': '33',
        'tape_number': '01',
        'side_id': '_1_',
        'title': 'Battlefield Earth',
        'sub_chapter': '03',
        'file_type': 'ogg'
    },
    '1_3_3_Battlefield Earth.ogg'
    ),
]


def test_title_parser_returns_a_dictionary():
    for truthy, original, parsed, formatted in correct_title_names:
        if truthy:
            assert isinstance(title_parser(original), dict)
        else:
            #not a meaningful test
            pass


def test_title_parser_returns_a_six_item_dictionary():
    for truthy, original, parsed, formatted in correct_title_names:
        if truthy:
            assert len(title_parser(original)) == 6
        else:
            #not a meaningful test
            pass

def test_title_parser_converts_title_to_dict():
    for truthy, original, parsed, formatted in correct_title_names:
        if truthy:
            assert title_parser(original) == parsed
        else:
            try:
                assert title_parser(original) != parsed
            except:
                print 'Expected error converting mal-formed filename.'


def test_filenamer_formats_filename_correctly():
    for truthy, original, parsed, formatted in correct_title_names:
        if truthy:
            assert filenamer(parsed) == formatted
        else:
            assert filenamer(parsed) != formatted
