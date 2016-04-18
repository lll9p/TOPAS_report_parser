#!/usr/bin/env python
# -*- coding: utf-8 -*-
def duplicates(lst, item):
    return [i for i, x in enumerate(lst) if x == item]
