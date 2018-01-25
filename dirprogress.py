#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import time
import progressbar


def watch_directory(inp, outp):
    n_input_files = len(os.listdir(inp))
    with progressbar.ProgressBar(max_value=n_input_files,
                                widgets=[
                                progressbar.Percentage(), ' (',
                                progressbar.SimpleProgress(), ') ',
                                progressbar.Bar(), ' ', 
                                progressbar.Timer(format='Time: %(elapsed)s'),
                                ' ', progressbar.AdaptiveETA()]) as bar:
        while True:
            n_output_files = len(os.listdir(outp))
            bar.update(n_output_files - 1)
            time.sleep(1.0)


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print >>sys.stderr, "usage: {} <input directory> <output directory>".format(sys.argv[0])
        sys.exit(1)

    watch_directory(sys.argv[1], sys.argv[2])
