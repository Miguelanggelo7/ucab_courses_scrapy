# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from courses.database import db_connect, create_table, Course
from sqlalchemy.orm import sessionmaker


class CoursesPipeline:
    def __init__(self):
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        session = self.Session()

        newCourse = Course(**item)

        session.add(newCourse)
        session.commit()
        return item
