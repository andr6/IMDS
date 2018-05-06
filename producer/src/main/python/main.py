import pyinotify
import filehandler
import config
import bro
import os
import nfscopy

print "IMDS Producer Module",
print " by Masoud Mehrabi"

if os.geteuid() != 0:
    print "You must run this as root!"
    exit()

print "Setting Up Network File Server..."
nfscopy.InitMount()

print "Starting Network Analyzer..."
bro.RunBro()

print "Warming Up..."
wm = pyinotify.WatchManager()
mask = pyinotify.IN_CREATE | pyinotify.IN_CLOSE_WRITE
handler = filehandler.FileHandler()
notifier = pyinotify.Notifier(wm, handler)
wdd = wm.add_watch(config.IMDS_EXTRACTOR_INSTALL_PATH + "extract_files",
        mask,
        rec=True)

print "Starting to monitor extracted files..."
notifier.loop()
