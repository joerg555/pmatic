#!/usr/bin/env python
# encoding: utf-8
#
# pmatic - Python API for Homematic. Easy to use.
# Copyright (C) 2016 Lars Michelsen <lm@larsmichelsen.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

import pmatic

# Open up a remote connection via HTTP to the CCU and login as admin. When the connection
# can not be established within 5 seconds it raises an exception.
import ccudata

ccu = pmatic.CCU(
    address         = ccudata.address,
    credentials     = ccudata.credentials,
    connect_timeout = ccudata.connect_timeout,
)

# There might be multiple devices with equal names. Even when we know there is
# only one device using this name, we get a list back from the API. But we can
# skip all other theoretical results when we are sure there is only one

device = list(ccu.devices.query(device_name=u"Büro-Lampe"))[0]
if device.switch_on():
    print("success!")
else:
    print("failed!")
