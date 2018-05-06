import sys
import os
import config

def RunBro():
    print os.popen('mkdir -p ' + config.IMDS_EXTRACTOR_INSTALL_PATH).read()

    print os.popen('cp '
            + os.path.dirname(os.path.abspath(__file__))
            + '/extract-all.bro '
            + config.IMDS_EXTRACTOR_INSTALL_PATH).read()

    os.chdir(config.IMDS_EXTRACTOR_INSTALL_PATH)

    os.popen(config.BRO_BIN_PATH
            + ' -C'
            + ' -i '
            + config.BRO_INTERFACE_TO_MONITOR
            + ' '
            + config.IMDS_EXTRACTOR_INSTALL_PATH
            + '/extract-all.bro &')
