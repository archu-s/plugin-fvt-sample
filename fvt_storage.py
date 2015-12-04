#!/usr/bin/python
# Project Kimchi
#
# Copyright IBM, Corp. 2015
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301USA



#from lib.utils import storage_utils, remote_utils
#from wok.tests.utils import utils, constants
from tests.fvt.fvt_base import TestBase, APIRequestError

import unittest


class TestStorage(TestBase):
    """
    Common storage test cases
    """

    @classmethod
    def setUpClass(cls):
        super(TestStorage, cls).setUpClass()
        cls.logging = cls.session.logging

    def test_F001_activate_incorrect_storagepool(self):
        """
        Test to Activate a storage pool that doesn't exists
        """
        self.logging.info('--> TestStorage.test_F001_activate_incorrect_storage_pool() ')
        self.logging.info('<-- TestStorage.test_F001_activate_incorrect_storage_pool() ')
