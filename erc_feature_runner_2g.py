#!/usr/bin/python3
import datetime

import log
from environment import ERICSSON_FEATURE_VENDOR
from scr.parser import main_baseline_parser
from scr.util import parser_db

TIME_START_SCRIPT = datetime.datetime.now()
log.i(" ", ERICSSON_FEATURE_VENDOR, "2G")
log.i(" ", ERICSSON_FEATURE_VENDOR, "2G")
log.i("           ", ERICSSON_FEATURE_VENDOR)
log.i("Start Script : " + ERICSSON_FEATURE_VENDOR, ERICSSON_FEATURE_VENDOR, "2G")

parser_db.update_status(ERICSSON_FEATURE_VENDOR, '2G', parser_db.STATUS_OPEN)

main_baseline_parser.run(ERICSSON_FEATURE_VENDOR, "2G")

TIME_END_SCRIPT = datetime.datetime.now()
log.i("Time : " + str(TIME_END_SCRIPT - TIME_START_SCRIPT), ERICSSON_FEATURE_VENDOR, "2G")

log.i("--------------------------------", ERICSSON_FEATURE_VENDOR, "2G")
log.i("--------------------------------", ERICSSON_FEATURE_VENDOR, "2G")
log.count()
log.i("--------------------------------", ERICSSON_FEATURE_VENDOR, "2G")
log.i("--------------------------------", ERICSSON_FEATURE_VENDOR, "2G")

log.i("Done all : " + ERICSSON_FEATURE_VENDOR + " 2G", ERICSSON_FEATURE_VENDOR, "2G")

parser_db.update_status(ERICSSON_FEATURE_VENDOR, '2G', parser_db.STATUS_CLOSE)

log.i("           ", ERICSSON_FEATURE_VENDOR)
log.i("           ", ERICSSON_FEATURE_VENDOR)
log.i("           ", ERICSSON_FEATURE_VENDOR)
log.i("           ", ERICSSON_FEATURE_VENDOR)
log.i("           ", ERICSSON_FEATURE_VENDOR)
log.i("           ", ERICSSON_FEATURE_VENDOR)
