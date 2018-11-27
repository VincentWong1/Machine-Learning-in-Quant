#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import numpy as np

"""
__author__ = 'Administrator'
__mtime__ = '2018/2/2'
"""

data = np.array([[[1, 5], [2], [3], [4]],
                 [[1], [3], [4], [3, 5]],
                 [[1], [2], [3], [4]],
                 [[1], [3], [5]],
                 [[4], [5]]])


def get_all_fr(data, i, ret=dict()):
    if i == len(data):
        return ret
    row = data[i]
    tmp_ret = get_row_fr(row)
    for key in tmp_ret.keys():
        if key in ret:
            ret[key] += tmp_ret[key]
        else:
            ret[key] = tmp_ret[key]

    return get_all_fr(data, i + 1, ret)


def get_row_fr(row):
    ret = {}
    for i in range(len(row)):
        for j in range(i + 1, len(row)):
            for k in range(len(row[i])):
                for l in range(len(row[j])):
                    if row[i][k] == row[j][l]:
                        continue
                    key = '%s->%s' % (row[i][k], row[j][l])
                    print key
                    ret[key] = 1
    return ret


if __name__ == '__main__':
    ret = dict()
    all_ret = get_all_fr(data, 0, {})

    for key in all_ret.keys():
        if all_ret[key] >= 2:
            ret.update({key: all_ret[key]})

    print ret
