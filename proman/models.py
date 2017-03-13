from connectdatabase import *
from peewee import *
import datetime
from datetime import date
from random import choice
# imap imports
from email.header import decode_header
import sys
import imaplib
import getpass
import email
import datetime
# SMTP imports
import smtplib
from smtplib import SMTP


class BaseModel(Model):
    """A base model that will use our Postgresql database"""

    class Meta:
        database = ConnectDatabase.db


class School(BaseModel):
    school_name = CharField()


class City(BaseModel):
    city_name = CharField()
    assigned_school = ForeignKeyField(School)


class Person(BaseModel):
    first_name = CharField()
    last_name = CharField()
    year_of_birth = DateField()
    email = CharField()
    gender = CharField()
    school = CharField(null=True)
    city = CharField()
    city_connection = ForeignKeyField(City, null=True)


class Applicant(Person):
    """Applicant table based on Applicant model."""
    application_code = CharField(null=True, unique=True)
    application_status = CharField(default="new")


class Mentor(Person):
    nickname = CharField()
    usercode = CharField()


class InterviewSlot(BaseModel):
    mentor = ForeignKeyField(Mentor)
    start = DateTimeField()
    end = DateTimeField()
    reserved = BooleanField(default=False)


class Interview(BaseModel):
    interview_slot = ForeignKeyField(InterviewSlot, related_name="slot")
    applicant = ForeignKeyField(Applicant, related_name="applicant_interview")

    @classmethod
    def find_applicant_without_interview(cls):
        applicant_list = Applicant.select().join(
            Interview, JOIN.LEFT_OUTER).where(Interview.applicant == None)
        return applicant_list

    @classmethod
    def find_free_slots(cls, applicant):
        available_slot = InterviewSlot.select(InterviewSlot, Mentor).join(
            Mentor).where((InterviewSlot.reserved == False) & (Mentor.school == applicant.school))
        return available_slot

    @classmethod
    def reserve_slots(cls):
        applicant_without_interview = cls.find_applicant_without_interview()
        for applicant in applicant_without_interview:
            free_slot = cls.find_free_slots(applicant)
            app_slot = choice(free_slot)
            app_slot.reserved = True
            app_slot.save()
            Interview.create(interview_slot=app_slot, applicant=applicant)


class Question(BaseModel):
    applicant_id = ForeignKeyField(Applicant)
    mentor_assigned = ForeignKeyField(Mentor)
    question_time = DateTimeField(default=datetime.datetime.now)
    question = CharField()
    question_status = CharField(default="waiting for answer")


class Answer(BaseModel):
    pass


class Email(BaseModel):
    subject = CharField()
    first_140_char = CharField()
    email_type = CharField(default="One-to-One")
    date = CharField()
    full_name = CharField()
    email_address = CharField()

    @staticmethod
    def email_to_applicant(applicant_email, applicant_name, applicant_city, application_code, subject):
        to = applicant_email
        gmail_user = 'codecool.b1ts.pls@gmail.com'
        gmail_pwd = 'mergeconflict'
        smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
        smtpserver.ehlo()
        smtpserver.starttls()
        smtpserver.ehlo()
        smtpserver.login(gmail_user, gmail_pwd)
        header = 'To:' + to + '\n' + \
            'From: ' + gmail_user + '\n' + \
            'Subject:' + subject + '\n'
        msg = str(header + "\nHello" + " " + "{}".format(applicant_name) + ",""\n\n\
You received this email because you applied to Codecool \
" + "{}".format(applicant_city) + "'s next course,\
 which starts this autumn.\n\
\n\
We gladly announce that the application has been started, \
and you'll find all the information in this email to start the process. \
The official written communication language is English at Codecool. \
Therefore the whole process is in English, so you can start practicing it, \
if you don't use it on a daily basis. \n\
\n\
The application starts with an online process of 4 steps about the following topics: \n\
- Introduction questions related to Codecool's concept, which measures if you understand \
all of the conditions (approx. 10 minutes) \n\
- English reading comprehension, to try out learning technological stuff based on \
materials in English (approx. 30 minutes)\n\
- Logical test, to measure your competence in the abstraction, problem solving and \
pattern recognition fields (approx. 60 minutes)\n\
- Motivation questions, introduction video, to get to know you better(approx. 1 - 2 hours)\n\
\n\
As you can see, the time needed to pass a step increases, \
so you have to be enduring to complete all the steps. We are sure \
that you have all the motivation, to do that!: -)\
It's important that you have exactly one week to finish all the 4 steps. \
The timer starts after you submit the first survey. You don't have to do \
all the 4 steps at once, take breaks, even days between them, \
and don't leave it for the last hours. The most important thing is \
to be relaxed through the whole process.\n\
\n\
Your Application Code is the following:" + " " + "{}".format(application_code) + " " + " \n\
\n\
We wish you a successful application! \n\
The Codecool Team\n\n")
        smtpserver.sendmail(gmail_user, to, msg)
        smtpserver.quit()

    @staticmethod
    def save_email():

        mailbox = imaplib.IMAP4_SSL('imap.gmail.com')
        mailbox.login("codecool.b1ts.pls@gmail.com", "mergeconflict")
        mailbox.select('"[Gmail]/Sent Mail"')

        result, data = mailbox.search(None, "ALL")
        ids = data[0]  # data is a list.
        id_list = ids.split()  # ids is a space separated string
        # WHERE ALL THE MAGIC HAPPENS
        for mail in id_list:
            # SUBJECT
            result, data = mailbox.fetch(mail, "(BODY[HEADER.FIELDS (SUBJECT)])")
            raw_subject = data[0][1]
            subject_string = raw_subject.decode("utf-8")
            subject = subject_string[9:]
            # MESSAGE
            result, data = mailbox.fetch(mail, "(UID BODY[TEXT])")
            raw_text = data[0][1]
            text = raw_text.decode("utf-8")
            first_140_char = text[:140]
            # DATE
            result, data = mailbox.fetch(mail, "(UID FLAGS BODY.PEEK[HEADER.FIELDS (Date)])")
            raw_date = data[0][1]
            date_string = raw_date.decode("utf-8")
            date = date_string[6:]
            # FULL NAME
            result, data = mailbox.fetch(mail, "(UID BODY[TEXT])")
            raw_text = data[0][1]
            name_without_hello_with_comma = str(raw_text)[8:]
            full_name = name_without_hello_with_comma.partition(',')[0]
            # TO
            result, data = mailbox.fetch(mail, "(UID FLAGS BODY.PEEK[HEADER.FIELDS (To)])")
            raw_to = data[0][1]
            to_string = raw_to.decode("utf-8")
            to = to_string[4:]
            # SAVE #
            Email.create(subject=subject,
                         first_140_char=first_140_char,
                         date=date,
                         full_name=full_name,
                         email_address=to)
