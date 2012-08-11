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

import pickle
import unittest

from Record import Record


class R(Record):
    __record_schema__ = {'a': 0, 'b': 1, 'c': 2}


class RecordTest(unittest.TestCase):

    def test_pickling(self):
        # We can create records from sequences
        r = R(('x', 42, 1.23))
        # We can pickle them
        r2 = pickle.loads(pickle.dumps(r))
        self.assertEqual(list(r), list(r2))
        self.assertEqual(r.__record_schema__, r2.__record_schema__)

    def test_no_dict(self):
        r = R()
        self.assertRaises(AttributeError, getattr, r, '__dict__')

    def test_attribute(self):
        r = R()
        self.assertTrue(r.a is None)
        self.assertTrue(r.b is None)
        self.assertTrue(r.c is None)
        r.a = 1
        self.assertEqual(r.a, 1)

    def test_mapping(self):
        r = R()
        r.a = 1
        self.assertEqual('%(a)s %(b)s %(c)s' % r, '1 None None')
        self.assertEqual(r['a'], 1)
        r['b'] = 42
        self.assertEqual(r['b'], 42)
        self.assertEqual(r.b, 42)

    def test_sequence(self):
        r = R()
        r.a = 1
        r.b = 42
        self.assertEqual(r[0], 1)
        self.assertEqual(r[1], 42)
        r[1] = 6
        self.assertEqual(r[1], 6)
        self.assertEqual(r.b, 6)
        r[2] = 7
        self.assertEqual(r[2], 7)
        self.assertEqual(r.c, 7)
        self.assertEqual(list(r), [1, 6, 7])
