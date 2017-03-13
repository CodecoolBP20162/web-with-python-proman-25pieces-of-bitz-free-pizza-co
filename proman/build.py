from models import *
from datetime import date
import datetime


class Build():

    @staticmethod
    def connect_build():
        db.connect()
        db.drop_tables([Applicant, School, City, Mentor,
                        InterviewSlot, Interview, Question, Email], True, True)
        db.create_tables([Applicant, School, City, Mentor,
                          InterviewSlot, Interview, Question, Email], safe=True)
