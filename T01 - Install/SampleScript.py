# -*- coding: utf-8 -*-
"""
Spyder Editor

This file is a diagnostic test to check if OpenSeesPy is installed.
 
"""

import openseespy.opensees as op

op.model('basic', '-ndm', 2, '-ndf', 3)
op.node(1, 0.,0)
op.wipe()
