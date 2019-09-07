#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    unmanic.settings.py
 
    Written by:               Josh.5 <jsunnex@gmail.com>
    Date:                     22 Jun 2019, (1:43 PM)
 
    Copyright:
           Copyright (C) Josh Sunnex - All Rights Reserved
 
           Permission is hereby granted, free of charge, to any person obtaining a copy
           of this software and associated documentation files (the "Software"), to deal
           in the Software without restriction, including without limitation the rights
           to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
           copies of the Software, and to permit persons to whom the Software is
           furnished to do so, subject to the following conditions:
  
           The above copyright notice and this permission notice shall be included in all
           copies or substantial portions of the Software.
  
           THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
           EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
           MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
           IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
           DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
           OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
           OR OTHER DEALINGS IN THE SOFTWARE.

"""

import os
from peewee import *
from lib.unmodels.basemodel import BaseModel

HOME_DIR = os.path.expanduser("~")


class Settings(BaseModel):
    """
    Settings

    All application settings
    """
    audio_codec = TextField(null=False, default='aac')
    audio_stereo_stream_bitrate = TextField(null=False, default='128k')
    cache_path = TextField(null=False, default='/tmp/unmanic')
    config_path = TextField(null=False, default=os.path.join(HOME_DIR, '.unmanic', 'config'))
    debugging = BooleanField(null=False, default=False)
    enable_audio_encoding = BooleanField(null=False, default=True)
    enable_inotify = BooleanField(null=False, default=True)
    enable_video_encoding = BooleanField(null=False, default=True)
    library_path = TextField(null=False, default='/library')
    log_path = TextField(null=False, default=os.path.join(HOME_DIR, '.unmanic', 'logs'))
    number_of_workers = IntegerField(null=False, default=3)
    out_container = TextField(null=False, default='mkv')
    remove_subtitle_streams = BooleanField(null=False, default=True)
    run_full_scan_on_start = BooleanField(null=False, default=False)
    schedule_full_scan_minutes = IntegerField(null=False, default=60)
    search_extensions = TextField(null=False, default='mkv,avi,mov,ts,rmvb,mp4,')
    video_codec = TextField(null=False, default='hevc')
