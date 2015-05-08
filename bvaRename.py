#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Purpose:
        A thin wrapper for renaming EEG data from BrainVision
        Analyser and rewriting .vhdr and .vrmk files.
        It simply replaces a given subjectCode with a
        new subject code. Oh, and it works in-place, so have your
        RCS up and running. Just in case :o)

    Requirements:
        none

    * Copyright (c) 2012-2015, Stefan Schinkel <mail@dreeg.org>


"""

__version__ = "0.01"

#Imports
import sys,os,re,glob


##########################
##      Functions       ##
##########################
def getInput():
    try:
        oldCode = sys.argv[1]
        newCode = sys.argv[2]

    except IndexError:
            print "This is bvarenamer Version: %s" % __version__
            print "ERROR: No/not enough codes given!"
            print "Calling convention: bvarenamer oldCode newCode"
            print "And by the way, I work in-place :o)"
            exit(-1)

    return(oldCode,newCode)

def getHeaderFiles(codeOld):

    """
    get all BVA headers matching the old code,
    simply is: ls `*oldCode*.vhdr`
    """
    pattern = '*'+codeOld + '*.vhdr'
    headerFiles = glob.glob(pattern)

    if len(headerFiles) == 0:
        print "No matches found. Goodbye"
        sys.exit(0)

    return headerFiles

def rewriteFile(fileOld,fileNew,strOld,strNew):

    """
    Infile, inline string replacement
    """

    print "Rewriting %s to %s " % (fileOld,fileNew)
    o = open(fileNew,"w")
    data = open(fileOld).read()
    o.write( re.sub(strOld,strNew,data)  )
    o.close()

    # explicit removal is required
    os.remove(fileOld)

##########################
##  Implementation      ##
##########################

if __name__ == '__main__':


    codes = getInput()
    oldCode = codes[0]; newCode = codes[1];

    # get all headerFiles that match the old code
    headerFiles = getHeaderFiles(oldCode)

    for hdr in headerFiles:

        # rewrite headerfiles
        rewriteFile(hdr,hdr.replace(oldCode,newCode),oldCode,newCode);

        # rewrite markerfiles
        mrk = hdr[:-4] + 'vmrk'
        rewriteFile(mrk,mrk.replace(oldCode,newCode),oldCode,newCode);

        # rewrite markerfiles
        eeg = hdr[:-4] + 'eeg'
        print "Renaming %s to %s" % (eeg,eeg.replace(oldCode,newCode))
        os.rename(eeg,eeg.replace(oldCode,newCode))

    # say goodbye
    print "All done. Have a nice day"


