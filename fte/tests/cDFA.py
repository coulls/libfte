#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of fteproxy.
#
# fteproxy is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# fteproxy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with fteproxy.  If not, see <http://www.gnu.org/licenses/>.


import os
import unittest

import fte.conf
import fte.cDFA


class TestcDFA(unittest.TestCase):

    def testMakeDFA(self):
        base_dir = fte.conf.getValue('general.base_dir')
        for i in range(1, 6):
            regex_file = os.path.join(
                base_dir, 'fte/tests/dfas/test' + str(i) + '.regex')
            with open(regex_file) as fh:
                regex = fh.read()

            dfa_file = os.path.join(
                base_dir, 'fte/tests/dfas/test' + str(i) + '.dfa')
            with open(dfa_file) as fh:
                expected_fst = fh.read()

            actual_fst = fte.dfa._attFstFromRegex(regex)
            actual_fst = fte.dfa._attFstMinimize(actual_fst)

            self.assertEquals(actual_fst, expected_fst)

if __name__ == '__main__':
    unittest.main()
