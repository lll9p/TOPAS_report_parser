#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
from .duplicate import duplicates
parser_pattern = re.compile(
    r'[\s\S]*R-Values [\s\S]*Rwp : (\d+\.\d+)[\s\S]*?Rp[\s\S]*Quantitative Analysis - Rietveld ([\s\S]*)Background[\s\S]*', re.M)
parser_phase_pattern = re.compile(
    r' *Phase \d.*: (.*?) *?(\d+\.\d+) %.*')


def TOPAS_txt_parser(file):
    with open(file, 'r') as f:
        t = parser_pattern.match(f.read())
    file_id = os.path.splitext(os.path.split(file)[1])[0]
    #deal with duplicat phase names
    phase_list = [[item.strip('"_ \'\\\/?\t.') for item in i.groups()] for i in filter(
        None, (parser_phase_pattern.match(line) for line in t.groups()[1].splitlines()))]
    phase_name = tuple(phase[0] for phase in phase_list)
    for dt in set(phase_name):
        dups = duplicates(phase_name, dt)
        if len(dups) > 1:
            for j, k in enumerate(dups):
                phase_list[k][0] += '_' + str(j)
    temp = {'ID': file_id, 'Rwp': t.groups()[0]}
    temp.update(dict(phase_list))
    return temp

