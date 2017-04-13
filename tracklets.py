# The MIT License (MIT)
#
# Copyright 2017 Artem Artemev, im@artemav.com
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software
# and associated documentation files (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge, publish, distribute,
# sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all copies or
# substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING
# BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import xml.etree.ElementTree as et
import pandas as pd

class Tracklets():
    _tracklet_common = ['frame', 'objectType', 'finished', 'h', 'w', 'l']
    _tracklet_pose = ['tx', 'ty', 'tz', 'rx', 'ry', 'rz', 'state', 'occlusion',
            'occlusion_kf', 'truncation', 'amt_occlusion', 'amt_occlusion_kf',
            'amt_border_l', 'amt_border_r', 'amt_border_kf']
    _int_columns = ['frame', 'finished', 'state', 'state', 'occlusion',
            'occlusion_kf', 'truncation', 'amt_occlusion', 'amt_occlusion_kf',
            'amt_border_l', 'amt_border_r', 'amt_border_kf']
    _columns = _tracklet_common + _tracklet_pose + ['source']

    def __init__(self):
        raise Exception("Tracklets object creation prohibited")

    @classmethod
    def load(cls, files):
        """Loads tracletlet files into pandas DataFrame
        Args:
            files: List of file paths to XML tracklets
        Return:
            DataFrame with tracklet objects
        """
        if type(files) is not list:
            files = [files]
        dt = pd.DataFrame(columns=cls._columns)
        for f in files:
            dt = dt.append(cls._load(f))
        return dt

    @classmethod
    def _load(cls, filename):
        dt = pd.DataFrame(columns=cls._columns)
        xml = et.parse(filename)
        tracklet_items = xml.find('tracklets').findall('item')
        k = 0
        for i, it in enumerate(tracklet_items):
            objtype = it.find('objectType').text
            shape = list(map(float, [it.find(key).text for key in ['h', 'w', 'l']]))
            frame, finished = map(int, [it.find(key).text for key in ['first_frame', 'finished']])
            poses = it.find('poses')
            num_poses = int(poses.find('count').text)
            poses_list = poses.findall('item')
            if len(poses_list) == 0:
                raise RuntimeError('Pose list can not be empty')
            if len(poses_list) != num_poses:
                raise RuntimeError('Broken tracklet element #{0}:'.format(i))
            for pose in poses_list:
                pose_fields = list(map(float, [pose.find(key).text for key in cls._tracklet_pose]))
                row = [frame, objtype, finished, *shape, *pose_fields, filename]
                dt.loc[k] = row
                frame += 1
                k += 1
        return dt
