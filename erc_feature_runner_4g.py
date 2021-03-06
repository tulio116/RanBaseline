#!/usr/bin/python3
import datetime
import os
import log
from environment import ERICSSON_FEATURE_VENDOR
from scr.parser import main_baseline_parser
from scr.util import parser_db

TIME_START_SCRIPT = datetime.datetime.now()
log.i(" ", ERICSSON_FEATURE_VENDOR, "4G")
log.i(" ", ERICSSON_FEATURE_VENDOR, "4G")
log.i("           ", ERICSSON_FEATURE_VENDOR)
log.i("Start Script : " + ERICSSON_FEATURE_VENDOR, ERICSSON_FEATURE_VENDOR, "4G")


parser_db.update_status(ERICSSON_FEATURE_VENDOR, '4G', parser_db.STATUS_OPEN)

main_baseline_parser.run(ERICSSON_FEATURE_VENDOR, "4G")

TIME_END_SCRIPT = datetime.datetime.now()
log.i("Time : " + str(TIME_END_SCRIPT - TIME_START_SCRIPT), ERICSSON_FEATURE_VENDOR, "4G")

log.i("--------------------------------", ERICSSON_FEATURE_VENDOR, "4G")
log.i("--------------------------------", ERICSSON_FEATURE_VENDOR, "4G")
log.count()
log.i("--------------------------------", ERICSSON_FEATURE_VENDOR, "4G")
log.i("--------------------------------", ERICSSON_FEATURE_VENDOR, "4G")

log.i("Done all : " + ERICSSON_FEATURE_VENDOR + " 4G", ERICSSON_FEATURE_VENDOR, "4G")

parser_db.update_status(ERICSSON_FEATURE_VENDOR, '4G', parser_db.STATUS_CLOSE)

log.i("           ", ERICSSON_FEATURE_VENDOR)
log.i("           ", ERICSSON_FEATURE_VENDOR)
log.i("           ", ERICSSON_FEATURE_VENDOR)
log.i("           ", ERICSSON_FEATURE_VENDOR)
log.i("           ", ERICSSON_FEATURE_VENDOR)
log.i("           ", ERICSSON_FEATURE_VENDOR)

log.i("Start Command Report", ERICSSON_FEATURE_VENDOR)
os.system("/home/ngoss/RANBaseLine/ERC_Feature_4G.sh")
log.i("Done Command Report", ERICSSON_FEATURE_VENDOR)