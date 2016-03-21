# Copyright (c) 2015-2016, Activision Publishing, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
# list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation
# and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its contributors
# may be used to endorse or promote products derived from this software without
# specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR
# ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
# ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import sys
import collections

from assertpy import assert_that,fail

class TestCollection(object):

    def test_is_iterable(self):
        assert_that(['a','b','c']).is_iterable()
        assert_that((1,2,3)).is_iterable()
        assert_that('foo').is_iterable()
        assert_that({ 'a':1,'b':2,'c':3 }.keys()).is_iterable()
        assert_that({ 'a':1,'b':2,'c':3 }.values()).is_iterable()
        assert_that({ 'a':1,'b':2,'c':3 }.items()).is_iterable()

    def test_is_iterable_failure(self):
        try:
            assert_that(123).is_iterable()
            fail('should have raised error')
        except AssertionError as ex:
            assert_that(str(ex)).is_equal_to('Expected iterable, but was not.')

    def test_is_not_iterable(self):
        assert_that(123).is_not_iterable()
        assert_that({ 'a':1,'b':2,'c':3 }).is_iterable()

    def test_is_not_iterable_failure(self):
        try:
            assert_that(['a','b','c']).is_not_iterable()
            fail('should have raised error')
        except AssertionError as ex:
            assert_that(str(ex)).is_equal_to('Expected not iterable, but was.')

    def test_chaining(self):
        assert_that(['a','b','c']).is_iterable().is_type_of(list).is_length(3)

