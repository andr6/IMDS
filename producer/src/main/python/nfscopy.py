import os
import sys
import shutil
import config

def InitMount():
    try:
        os.popen('mkdir -p ' + config.NFS_LOCAL_PATH)
        os.popen('mount -t nfs  '
                + config.NFS_REMOTE_PATH
                + ' '
                + config.NFS_LOCAL_PATH)
    except:
        print 'Error in initMount: ' + sys.exc_info()[0]


def CopyToNFS(filepath, remotefilename):
    try:
        shutil.copy2(filepath,
            config.NFS_LOCAL_PATH
            + '/' +
            remotefilename)
    except:
        print 'Error in copyToNFS: ' + sys.exc_info()[0]

def CopyFromNFS(remotefilename, localfilepath):
    try:
        shutil.copy2(config.NFS_REMOTE_PATH
            + '/'
            + remotefilenme,
            localfilepath)
    except:
        print 'Error in copyFromNFS: ' + sys.exc_info()[0]
