Psiturk Parser parses the trialdata file that's created by psiTurk so that is can be read easily by Excel and other programs.

Specifically, the JSON data object is put into csv form along side the rest of the data.

This script is meant to be used from the command line. To do this, you'll have to make it executable.
The simplest way to do this is to add it to your /usr/local/bin/ directory (on OS X).
Alternatively, you can put it anywhere and manually add it to your $PATH.

This script should work with both python 2 and 3.

The most straightforward way of using Psiturk Parser is to call `download_datafiles` normally, `quit` psiTurk,
and enter `psiturkParser.py`. This will create a new parsed file named fixedtrialdata.csv.

Alternatively, the script will take 2 arguments: the input filename/filepath (`-f`|`--filepath`) and the new filename/filepath (`-n`|`--newfile`).
If only a filename is given the current directory will be searched.

Files will not be overwritten unless the overwrite flag (`-o`|`--overwrite`) is provided as an argument.


