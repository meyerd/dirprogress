Dirprogress
===========

Monitor two directories, where directory A contains the source files
to be processed by some program and directory B contains the generated
files of this program, where the assumption is that for every source
file one output file is generated. Then dirprogress counts the number of
files in both directories and estimates the time to finish and percentage
of work done based on how many output files exist.

`usage: dirprogress <input directory> <output directory>`

Exit with `<ctrl-c>`.

This project uses [progressbar](https://github.com/WoLpH/python-progressbar)
and [python-utils](https://github.com/WoLpH/python-utils)
