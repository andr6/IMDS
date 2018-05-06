import config
import nfscopy
import rabbitpush
import sqliteread
import pyinotify
import os
import time
import cPickle as pickle

class FileHandler(pyinotify.ProcessEvent):
    def process_IN_CREATE(self, event):
        print "Creating:", event.pathname

    def process_IN_CLOSE_WRITE(self, event):
        print "Finished Writing:", event.pathname

        print "Waiting for bro to finish its work..."
        time.sleep(5)

        print "Writing File To NFS..."
        nfscopy.CopyToNFS(event.pathname, os.path.basename(event.pathname))

        print "Deleting File..."
        os.remove(event.pathname);

        print "Reading File Data From SQLite..."
        fid = os.path.basename(event.pathname).split('.')[0]
        fil = sqliteread.ReadFile(config.IMDS_EXTRACTOR_INSTALL_PATH + "file.sqlite", fid)
        pe = sqliteread.ReadPE(config.IMDS_EXTRACTOR_INSTALL_PATH + 'pe.sqlite', fid)
        connid = fil[4]
        conn = sqliteread.ReadConn(config.IMDS_EXTRACTOR_INSTALL_PATH + "conn.sqlite", connid)

        print 'Pushing to Work Queue...'
        msg = (os.path.basename(event.pathname), fil, pe, conn)
        pick = pickle.dumps(msg)
        rabbitpush.Enqueue(pick)

        print 'Done.'
