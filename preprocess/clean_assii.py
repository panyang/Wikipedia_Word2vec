#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Pan Yang (panyangnlp@gmail.com)
# Copyright 2017

import string
from sys import stdin

printable = set(string.printable)

for line in stdin:
    filter_line = filter(lambda x: x not in printable, line).strip()
    if filter_line != "":
        print filter_line
