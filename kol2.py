#
# Class diary  
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
# The default interface for interaction should be python interpreter.
# Please, use your imagination and create more functionalities. 
# Your project should be able to handle entire school.
# If you have enough courage and time, try storing (reading/writing) 
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface.

import json

class Diary(object):
    
    def __init__(self):
        super(Diary, self).__init__()
        self.cont=0
        self.subjects={}

    def course(self, subject):
        self.subjects[subject]={}

    def enrroll_std_in_subject(self, subject, stdname, stdsurname):
        self.subjects[subject][stdname]=[stdsurname,0,[]]

    def addgrade(self,subject,stdname,grade ):
        self.subjects[subject][stdname][2].append(grade)

    def attendence(self,subject,stdname):
        self.subjects[subject][stdname][1]+=1

    def subject_average(self, subject):
        sum=0
        for std in self.subjects[subject]:
            sum=sum+self.get_std_average_grade_in_subject(subject, std)
        return sum/len(self.subjects[subject])

    def std_average_grade_in_subject(self,subjet, std):
        sum=0
        self.cont+=1
        for grade in self.subjects[subjet][std][2]:
            sum= sum+grade
        sum=sum/len(self.subjects[subjet][std][2])
        return sum
    def stds_total_average(self):
        sum=0
        for sbjt in self.subjects:
            sum=sum+ self.subject_average(sbjt)
        return sum/len(self.subjects)
    def std_average_in_total(self,std):
        sum=0;
        self.cont=0
        for sbjt in self.subjects:
            sum=sum+self.std_average_grade_in_subject(sbjt,std)
        sum=sum/self.cont
        return sum
    def get_json(self):
        with open('output_file.json','w') as fp:
            json.dump(self.subjects,fp)
    def init_from_json(self):
        with open('output_file.json') as data_file:
            self.subjects=json.load(data_file)
        pass
print('build')
diary= Diary()
diary.course('python')
diary.enrroll_std_in_subject('python','Burcu','Gülşahin')
diary.attendence('python','Burcu')
diary.get_json()
print(diary.subjects)
print(diary.stds_total_average())
print(diary.std_average_in_total('Burcu'))
diary.subjects={}
diary.init_from_json()
print(diary.subjects)
