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

# https://www.eq-3.de/Downloads/eq3/download%20bereich/hm_web_ui_doku/HM_XmlRpc_API.pdf
# http://www.eq-3.de/Downloads/Software/HM-CCU2-Firmware_Updates/Tutorials/hm_devices_Endkunden.pdf
# https://sites.google.com/site/homematicplayground/api/json-rpc

# Add Python 3.x behaviour to 2.7
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import pmatic
# Uncomment to enable debug logging of pmatic messages to stderr
# pmatic.logging(pmatic.DEBUG)

import ccudata

ccu = pmatic.CCU(
    address         = ccudata.address,
    credentials     = ccudata.credentials,
    connect_timeout = ccudata.connect_timeout,
)

print("Low battery: ")
some_low = False
for device in ccu.devices:
    print("  %s: %s" % (device.name, device.summary_state))
    if device.is_battery_low:
        print("  %s: %s" % (device.name, device.summary_state))
        some_low = True
    if hasattr(device,"battery_state"):
        batt = device.battery_state.value
        if batt <= 2.4:
            print("  %s Batt %0.1f V : %s" % (device.name, batt, device.summary_state,))
            some_low = True

if not some_low:
    print("  All battery powered devices are fine.")
