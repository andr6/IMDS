import sqlite3
import sys

def ReadConn(in_filepath, in_cid):
    try:
        connection = sqlite3.connect(in_filepath)
        c = connection.cursor()
        t = (in_cid, )
        c.execute("SELECT * FROM conn WHERE uid=?", t);
        out_conn = c.fetchone()
        return out_conn
    except:
        print "Error in readConn: " + str(sys.exc_info()[0])
    connection.close()

def ReadFile(in_filepath, in_fid):
    try:
        connection = sqlite3.connect(in_filepath)
        c = connection.cursor()
        t = (in_fid, )
        c.execute("SELECT * FROM file WHERE fuid=?", t)
        out_file = c.fetchone()
        return out_file
    except:
        print "Error in readFile: " + str(sys.exc_info()[0])
    connection.close()

def ReadPE(in_filepath, in_fid):
    try:
        connection = sqlite3.connect(in_filepath)
        c = connection.cursor()
        t = (in_fid, )
        c.execute("SELECT * FROM pe WHERE id=?", t)
        out_pe = c.fetchone()
        return out_pe
    except:
        print "Error in readPE: " + str(sys.exc_info()[0])
    connection.close()

