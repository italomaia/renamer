#! /usr/bin/env python
# -*- coding:utf-8 -*-

#
# Author: italo maia
# Date: 17/10/2012
# Based in code from pyrenamer project
#

import os
import re
import shutil
import glob
import argparse


def convert_pattern(pattern):
    pattern = pattern.replace('.','\.')
    pattern = pattern.replace('[','\[')
    pattern = pattern.replace(']','\]')
    pattern = pattern.replace('(','\(')
    pattern = pattern.replace(')','\)')
    pattern = pattern.replace('?','\?')
    pattern = pattern.replace('{#}', '([0-9]+)')
    pattern = pattern.replace('{L}', '([a-zA-Z]+)')
    pattern = pattern.replace('{C}', '([\S]+)')
    pattern = pattern.replace('{X}', '([\S\s]+)')
    pattern = pattern.replace('{@}', '(.+)')
    return pattern


def main(input_pattern, output_pattern, case_insensitive=False,
         to_lower=False, to_upper=False, file_only=False, dir_only=False, print_only=True):
    working_dir = os.path.abspath(os.path.dirname(input_pattern))
    pattern = convert_pattern(input_pattern)

    flags = re.UNICODE
    if case_insensitive:
        flags = flags | re.IGNORECASE

    repattern = re.compile(pattern, flags)

    for filename in glob.iglob(os.path.join(working_dir, '*')):
        basename = os.path.basename(filename)
        match = repattern.search(basename)

        if match:
            groups = match.groups()
            newname = output_pattern

            for i in range(len(groups)):
                newname = newname.replace('{'+ `i+1` +'}', groups[i])

            if to_lower:
                newname = newname.lower()

            if to_upper:
                newname = newname.upper()

            if print_only:
                print basename, '->', newname
            else:
                shutil.move(filename, os.path.join(working_dir, newname))


def get_arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_pattern', type=str, help='Input pattern')
    parser.add_argument('output_pattern', type=str, help='Output pattern')
    parser.add_argument('-i', '--case-insensitive', dest='case_insensitive', action='store_true')
    parser.add_argument('-l', '--lower', dest='to_lower_case', action='store_true')
    parser.add_argument('-u', '--upper', dest='to_upper_case', action='store_true')
    parser.add_argument('-f', '--file-only', dest='file_only', action='store_true')
    parser.add_argument('-d', '--dir-only', dest='dir_only', action='store_true')
    parser.add_argument('-p', '--parse', dest='print_only', action='store_false')
    return parser


if __name__ == '__main__':
    args = get_arg_parser().parse_args()
    main(args.input_pattern, args.output_pattern,
        case_insensitive=args.case_insensitive,
        to_lower=args.to_lower_case,
        to_upper=args.to_upper_case,
        file_only=args.file_only,
        dir_only=args.dir_only,
        print_only=args.print_only)

