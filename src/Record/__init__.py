##############################################################################
#
# Copyright (c) 2003 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################


class Record(object):
    """Simple Record Types"""

    __record_schema__ = None
    __slots__ = ('_data', '_schema')

    def __init__(self, data=None, parent=None):
        cls_schema = type(self).__record_schema__
        if cls_schema is None:
            cls_schema = {}
        self._schema = schema = cls_schema
        len_schema = len(schema)
        if data is not None:
            if isinstance(data, dict):
                self._data = (None, ) * len_schema
                for k, v in data.items():
                    if k in schema:
                        self[k] = v
            elif len(data) == len_schema:
                self._data = tuple(data)
            else:
                self._data = (None, ) * len_schema
                maxlength = min(len(data), len_schema)
                for i in xrange(maxlength):
                    self[i] = data[i]
        else:
            self._data = (None, ) * len(schema)

    def __getstate__(self):
        return self._data

    def __setstate__(self, state):
        self.__init__(state)

    def __getitem__(self, key):
        if isinstance(key, int):
            pos = key
        else:
            pos = self._schema[key]
        return self._data[pos]

    def __getattr__(self, key):
        if key in self.__slots__:
            return object.__getattribute__(self, key)
        try:
            return self.__getitem__(key)
        except KeyError:
            raise AttributeError(key)

    def __setitem__(self, key, value):
        if isinstance(key, int):
            pos = key
        else:
            try:
                pos = self._schema[key]
            except IndexError:
                raise TypeError('invalid record schema')
        old = self._data
        self._data = old[:pos] + (value, ) + old[pos + 1:]

    def __setattr__(self, key, value):
        if key in self.__slots__:
            object.__setattr__(self, key, value)
        else:
            try:
                self.__setitem__(key, value)
            except KeyError:
                raise AttributeError(key)

    def __delattr__(self, key):
        self[key] = None

    def __delitem__(self, key):
        if isinstance(key, int):
            raise TypeError('cannot delete record items')
        self[key] = None

    def __contains__(self, key):
        return key in self._schema

    def __getslice__(self, i, j):
        raise TypeError('Record objects do not support slicing')

    def __setslice__(self, i, j, sequence):
        raise TypeError('Record objects do not support slicing')

    def __delslice__(self, i, j):
        raise TypeError('Record objects do not support slicing')

    def __add__(self, other):
        raise TypeError('Record objects do not support concatenation')

    def __mul__(self, other):
        raise TypeError('Record objects do not support repetition')

    def __len__(self):
        return len(self._schema)

    def __cmp__(self, other):
        if isinstance(other, Record):
            return cmp(self._data, other._data)
        return cmp(id(self), id(other))
