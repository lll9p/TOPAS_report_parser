#!/usr/bin/env python
# -*- coding: utf-8 -*-
def try_float(s):
    try:
        r = float(s)
    except:
        r = s
    return r
