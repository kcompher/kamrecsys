#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from __future__ import unicode_literals

from numpy.testing import (assert_array_equal, assert_array_less,
                           assert_allclose, assert_array_max_ulp,
                           assert_array_almost_equal_nulp)
import unittest

##### Test Classes #####

class TestBaseData(unittest.TestCase):

    def test_class(self):
        from ...datasets import load_pci_sample

        data = load_pci_sample()

        self.assertEqual(data.to_iid(0, 'Mick LaSalle'), 5)
        with self.assertRaises(ValueError):
            x = data.to_iid(0, 'Dr. X')
        self.assertEqual(data.to_eid(1, 4), 'The Night Listener')
        with self.assertRaises(ValueError):
            x = data.to_eid(1, 100)

##### Main routine #####
if __name__ == '__main__':
    unittest.main()