#!/usr/bin/python3
import datetime

import cx_Oracle

import log
from environment import *
from scr.dao import ran_baseline_oracle
from scr.parser import main_baseline_parser_debug
from scr.util import parser_db

TIME_START_SCRIPT = datetime.datetime.now()
log.i(" ", HUAWEI_VENDOR, "5G")
log.i(" ", HUAWEI_VENDOR, "5G")
log.i("           ", HUAWEI_VENDOR, "5G")
log.i("Start Script : " + HUAWEI_VENDOR, HUAWEI_VENDOR, "5G")


def close_connection(connection, cur):
    cur.close()
    connection.close()


def open_connection():
    dsn_tns = cx_Oracle.makedsn(ORACLE_HOST, ORACLE_PORT, ORACLE_SID)
    connection = cx_Oracle.connect(ORACLE_USERNAME, ORACLE_PASSWORD, dsn_tns)
    cur = connection.cursor()
    return connection, cur

parser_db.update_status(HUAWEI_VENDOR, '5G', parser_db.STATUS_OPEN)

main_baseline_parser_debug.run(HUAWEI_VENDOR, "5G")

TIME_END_SCRIPT = datetime.datetime.now()
log.i("Time : " + str(TIME_END_SCRIPT - TIME_START_SCRIPT), HUAWEI_VENDOR, "5G")
log.i("--------------------------------", HUAWEI_VENDOR, "5G")
log.i("--------------------------------", HUAWEI_VENDOR, "5G")
log.count()
log.i("--------------------------------", HUAWEI_VENDOR, "5G")
log.i("--------------------------------", HUAWEI_VENDOR, "5G")
log.i("Done all : " + HUAWEI_VENDOR + " 5G", HUAWEI_VENDOR, "5G")
parser_db.update_status(HUAWEI_VENDOR, '5G', parser_db.STATUS_CLOSE)


log.i("           ", HUAWEI_VENDOR, "5G")
log.i("           ", HUAWEI_VENDOR, "5G")
log.i("           ", HUAWEI_VENDOR, "5G")
log.i("           ", HUAWEI_VENDOR, "5G")
log.i("           ", HUAWEI_VENDOR, "5G")
log.i("           ", HUAWEI_VENDOR, "5G")
