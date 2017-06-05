# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import sqlite3 as lite

con = lite.connect("lapistadb.db") # db connection


class StoreInDBPipeline(object):
    def __init__(self):
        self.setupDBCon()
        self.dropCrawlingTable()
        self.createCrawlingTable()

    def process_item(self, item, spider):
        self.storeInDb(item)
        return item

    def storeInDb(self, item):
        self.cur.execute("INSERT INTO crawldata(\
        SCH_COST, \
        AIR_INFO, \
        R_ORIGIN, \
        DEP_T, \
        DEP_DATE, \
        R_DEST, \
        ARR_T, \
        ARR_DATE, \
        L_LO \
        ) \
        VALUES( ?, ?, ?, ?, ?, ?, ?, ?, ? )",
          (
            item["SCH_COST"],
            item["AIR_INFO"] ,
            item["R_ORIGIN"] ,
            item["DEP_T"] ,
            item["DEP_DATE"],
            item["R_DEST"] ,
            item["ARR_T"] ,
            item["ARR_DATE"],
            item["L_LO"]
            ))
        self.con.commit()




    def setupDBCon(self):
        self.con = lite.connect('lapistadb.db')
        self.cur = self.con.cursor()

    def __del__(self):
        self.closeDB()

    def createCrawlingTable(self):
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS
                crawldata
                (SCH_COST TEXT PRIMARY KEY NOT NULL,
                 AIR_INFO TEXT,
                 R_ORIGIN TEXT,
                 DEP_T TEXT,
                 DEP_DATE TEXT,
                 R_DEST TEXT,
                 ARR_T Text,
                 ARR_DATE TEXT,
                 L_LO TEXT)
        """)

    def dropCrawlingTable(self):
        self.cur.execute("DROP TABLE IF EXISTS crawldata")

    def closeDB(self):
        self.con.close()