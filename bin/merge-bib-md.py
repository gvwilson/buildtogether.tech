#!/usr/bin/env python

'''Merge Markdown bibliographies.'''

import sys
import yaml

import utils


KEY_ORDER = [
    'key',
    'type',
    'author',
    'title',
    'edition',
    'booktitle',
    'editor',
    'journal',
    'volume',
    'number',
    'month',
    'year',
    'doi',
    'isbn',
    'publisher',
    'url',
    'note'
]


def merge_bib_md(options):
    '''Main driver.'''
    merged = merge_inputs(options)
    ordered = [merged[key] for key in sorted(merged.keys())]
    cleaned = [cleanup(entry) for entry in ordered]
    raw = yaml.dump(cleaned, sort_keys=False, width=utils.YAML_INFINITE)
    cooked = utils.cook_yaml(raw)
    print(cooked)


def merge_inputs(options):
    '''Read all files, merging inputs.'''
    result = {}
    for fn in options.sources:
        temp = utils.read_yaml(fn)
        for entry in temp:
            assert 'key' in entry, f'Entry {entry} from {fn} lacks key'
            if options.verbose and (entry['key'] in result):
                print(f'duplicate key {entry["key"]} in {fn}', file=sys.stderr)
            result[entry['key']] = entry
    return result


def cleanup(entry):
    '''Create new dict for entry with keys in desired order.'''
    return {key:utils.strip_nested(entry[key])
            for key in KEY_ORDER
            if key in entry}


if __name__ == '__main__':
    options = utils.get_options(
        ['--sources', True, 'List of input files'],
        ['--verbose', None, 'Report duplicate keys?']
    )
    merge_bib_md(options)
