# -*- coding: utf-8 -*-

import uvclight
import os
from uvc.themes.btwidgets import IBootstrapRequest
import siguvtheme.resources


class IDGUVRequest(IBootstrapRequest):
    pass


def get_template(name):
    return uvclight.get_template(name, siguvtheme.resources.__file__)
