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
#pmatic.logging(pmatic.DEBUG)
import ccudata

ccu = pmatic.CCU(
    address         = ccudata.address,
    credentials     = ccudata.credentials,
    connect_timeout = ccudata.connect_timeout,
)

device = list(ccu.devices.query(device_name="Wohnzimmer"))[0]

print("%s: %s, Valve State: %s" % (device.name, device.summary_state, device.valve_state))
