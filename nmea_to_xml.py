"""
    Copyright (C) 2014 Richard Laugesen, richard@tinyrock.com

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along
    with this program; if not, write to the Free Software Foundation, Inc.,
    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
"""

import os
import sys

def convert(input_dir, output_dir, output_formats):
    for format in output_formats:
        for input in os.listdir(input_dir):
            if '.log' in input:
                print format, input

                cmd = 'gpsbabel \
                -i nmea \
                -f "' + input_dir + input + '" \
                -o ' + format + ' \
                -F ' + output_dir + input[0:-4] + '.' + format

                os.system(cmd)

if __name__ == "__main__":
    print 'Converts NMEA log files from a GPS unit (Navman MY450LMT) to KML and GPX'

    if len(sys.argv) == 3:
        convert(sys.argv[1], sys.argv[2], ['gpx', 'kml'])
    else:
        print 'python nmea_to_xml.py input_dir output_dir'
