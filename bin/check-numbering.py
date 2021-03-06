#!/usr/bin/env python

'''Check that internal cross-references resolve.'''

import argparse
import re
import sys

import utils


# Chapter and appendix cross-references use '<span x="key"></span>'.
CROSS_REF = re.compile(r'<span\s+?x="(.+?)">\s*?</span>', re.DOTALL)

# Figure and table cross-references.
FIGURE_REF = re.compile(r'<span\s+?f="(.+?)">\s*?</span>', re.DOTALL)
TABLE_REF = re.compile(r'<span\s+?t="(.+?)">\s*?</span>', re.DOTALL)

def check_numbering(options):
    '''Main driver.'''
    numbering = utils.read_yaml(options.numbering)
    check_cross_references(numbering, options.sources)
    check_self_references(numbering)
    check_figures(numbering, options.sources)
    check_tables(numbering, options.sources)


def check_cross_references(numbering, filenames):
    '''Check that chapter/appendix references resolve.'''
    defined = set([entry['slug'] for entry in numbering['entries']])
    referenced = utils.get_all_matches(CROSS_REF, filenames)
    utils.report('cross-references', checkOnlyRight=False, referenced=referenced, defined=defined)


def check_self_references(numbering):
    '''Make sure chapters don't refer to themselves.'''
    problems = set()
    for entry in numbering['entries']:
        referenced = utils.get_matches(CROSS_REF, entry['file'])
        if entry['slug'] in referenced:
            problems.add(entry['file'])
    if problems:
        print('- self-references')
        for filename in sorted(problems):
            print(f'  - {filename}')


def check_figures(numbering, filenames):
    '''Check that figure references resolve.'''
    defined = set(numbering['figures'].keys())
    referenced = utils.get_all_matches(FIGURE_REF, filenames)
    utils.report('figure references', referenced=referenced, defined=defined)


def check_tables(numbering, filenames):
    '''Check that table references resolve.'''
    defined = set(numbering['tables'].keys())
    referenced = utils.get_all_matches(TABLE_REF, filenames)
    utils.report('table references', referenced=referenced, defined=defined)


if __name__ == '__main__':
    options = utils.get_options(
        ['--numbering', False, 'Path to YAML numbering file'],
        ['--sources', True, 'List of input files']
    )
    check_numbering(options)
