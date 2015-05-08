#BVARENAME
commandline tool to rename BrainVision data and header files

##About:

Sometimes one has to rename BrainVision Recorder output files (eg. if subject coding changes, or you entered the wrong filename, etc.). This involves changing the actual filenames and rewriting the header (.vhdr) and marker (.vmrk) files. Doing this manually is clearly too error-prone. I had to do this and thus wrote a very simple Python script to take care of that. Maybe you can use that too.

**Important note: This function works in-place!**

###Requirements:

Python - it first ran on 2.6 so 2.7 should be fine. Python3 could work too.

###Example:

Download the script and make it executable. Also add it to $PATH so it can be called from anywhere

```sh
# make executable
chmod u+x bvaRename.py
# add path (in Bash and the likes)
export PATH=$PATH:/path/to/bvaRename.py
# add path (in CSH)
setenv PATH "${PATH}:/path/to/bvaRename.py
```

Now for the actual renaming. Imagine you ran 4 experiments (motor, visual, emotional and cognitive) and the subject code was XYZ_0001. Now it turns out, the code was supposed to be subject02.

```sh
user@host~/temp$ ls
XYZ_0001cognitive.eeg   XYZ_0001visual.vhdr
XYZ_0001cognitive.vhdr  XYZ_0001visual.vmrk
XYZ_0001cognitive.vmrk  XYZ_0001motor.eeg
XYZ_0001emotional.eeg   XYZ_0001motor.vhdr
XYZ_0001emotional.vhdr  XYZ_0001motor.vmrk
XYZ_0001emotional.vmrk
XYZ_0001visual.eeg
```

Now rename everyting

```sh
user@host~/temp$ bvaRename.py XYZ_0001 subject02

Rewriting XYZ_0001cognitive.vhdr to subject02cognitive.vhdr
Rewriting XYZ_0001cognitive.vmrk to subject02cognitive.vmrk
Renaming XYZ_0001cognitive.eeg to subject02cognitive.eeg
Rewriting XYZ_0001emotional.vhdr to subject02emotional.vhdr
Rewriting XYZ_0001emotional.vmrk to subject02emotional.vmrk
Renaming XYZ_0001emotional.eeg to subject02emotional.eeg
Rewriting XYZ_0001visual.vhdr to subject02visual.vhdr
Rewriting XYZ_0001visual.vmrk to subject02visual.vmrk
Renaming XYZ_0001visual.eeg to subject02visual.eeg
Rewriting XYZ_0001motor.vhdr to subject02motor.vhdr
Rewriting XYZ_0001motor.vmrk to subject02motor.vmrk
Renaming XYZ_0001motor.eeg to subject02motor.eeg
All done. Have a nice day
```

The data files are now renamed and the reference in the header/marker files is set accordingly.

```sh
user@host~/temp$ ls
subject02cognitive.eeg      subject02visual.vhdr
subject02cognitive.vhdr     subject02visual.vmrk
subject02cognitive.vmrk     subject02motor.eeg
subject02emotional.eeg      subject02motor.vhdr
subject02emotional.vhdr     subject02motor.vmrk
subject02emotional.vmrk
subject02visual.eeg
```

In the same manner one could have changed visual to motor, motor to cognitive and so on.
