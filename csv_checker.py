import csv
# Importing or_version_check to run proper header_values checks
from or_version_check import *

version_check = FileChecker()

class CsvChecker:

    #Checking Orgs

    def orgs_header_checker(self):
        try:
            with open('./roster/orgs.csv', 'r') as file:
                incorrect_first_row = [x for x in csv.reader(file, delimiter=',', quotechar="'")]

                lower_incorrect_first_row = [[word.lower() for word in x] for x in incorrect_first_row]

                header_values_v1 = [x.lower() for x in ['sourcedid','name','type','status','dateLastModified','identifier','metadata.classification','metadata.gender','metadata.boarding','parentSourcedId']]
                header_values_v1_1 = [x.lower() for x in ['sourcedid','status','dateLastModified','name','type','identifier','parentSourcedId']]

                if or_v1 == True:
                    for a in lower_incorrect_first_row[0]:
                        if a in header_values_v1:
                            header_values_v1.remove(a)

                    if len(header_values_v1) == 0:
                        pass
                    else:
                        print('\n')
                        print('orgs.csv errors:')
                        for b in header_values_v1:
                            print('Header row value missing: {} '.format(b))

                if or_v1_1 == True:
                    for a in lower_incorrect_first_row[0]:
                        if a in header_values_v1_1:
                            header_values_v1_1.remove(a)

                    if len(header_values_v1_1) == 0:
                        pass
                    else:
                        print('\n')
                        print('orgs.csv errors:')
                        for b in header_values_v1_1:
                            print('Header row value missing: {} '.format(b))

        except FileNotFoundError:
                print('\n')
                print('No orgs.csv file found')

    #Checking Users

    def users_header_checker(self):
        try:
            with open('./roster/users.csv', 'r') as file:
                incorrect_first_row = [x for x in csv.reader(file, delimiter=',', quotechar="'")]

                lower_incorrect_first_row = [[word.lower() for word in x] for x in incorrect_first_row]

                header_values_v1 = [x.lower() for x in ['sourcedid','orgSourcedIds','username','givenName','familyName','status','dateLastModified','role','userId','identifier','email','sms','phone','agents']]
                header_values_v1_1 = [x.lower() for x in ['sourcedid','status','dateLastModified','enabledUser','orgSourcedIds','role','username','userIds','givenName','familyName','middleName','identifier','email','sms','phone','agentSourcedIds','grades','password']]

                if or_v1 == True:
                    for a in lower_incorrect_first_row[0]:
                        if a in header_values_v1:
                            header_values_v1.remove(a)

                    if len(header_values_v1) == 0:
                        pass
                    else:
                        print('\n')
                        print('users.csv errors:')
                        for b in header_values_v1:
                            print('Header row value missing: {} '.format(b))

                if or_v1_1 == True:
                    for a in lower_incorrect_first_row[0]:
                        if a in header_values_v1_1:
                            header_values_v1_1.remove(a)

                    if len(header_values_v1_1) == 0:
                        pass
                    else:
                        print('\n')
                        print('users.csv errors:')
                        for b in header_values_v1_1:
                            print('Header row value missing: {} '.format(b))

        except FileNotFoundError:
                print('\n')
                print('No users.csv file found')

    #Checking Courses

    def courses_header_checker(self):
        try:
            with open('./roster/courses.csv', 'r') as file:
                incorrect_first_row = [x for x in csv.reader(file, delimiter=',', quotechar="'")]

                lower_incorrect_first_row = [[word.lower() for word in x] for x in incorrect_first_row]

                header_values_v1 = [x.lower() for x in ['sourcedid','title','status','dateLastModified','schoolYearId','metadata.duration','courseCode','grade','orgSourcedId','subject']]
                header_values_v1_1 = [x.lower() for x in ['sourcedid','status','dateLastModified','schoolYearId','title','courseCode','grades','orgSourcedId','subjects','subjectCodes']]

                if or_v1 == True:
                    for a in lower_incorrect_first_row[0]:
                        if a in header_values_v1:
                            header_values_v1.remove(a)

                    if len(header_values_v1) == 0:
                        pass
                    else:
                        print('\n')
                        print('courses.csv errors:')
                        for b in header_values_v1:
                            print('Header row value missing: {} '.format(b))

                if or_v1_1 == True:
                    for a in lower_incorrect_first_row[0]:
                        if a in header_values_v1_1:
                            header_values_v1_1.remove(a)

                    if len(header_values_v1_1) == 0:
                        pass
                    else:
                        print('\n')
                        print('courses.csv errors:')
                        for b in header_values_v1_1:
                            print('Header row value missing: {} '.format(b))

        except FileNotFoundError:
                print('\n')
                print('No courses.csv file found')

    #Checking Classes

    def classes_header_checker(self):
        try:
            with open('./roster/classes.csv', 'r') as file:
                incorrect_first_row = [x for x in csv.reader(file, delimiter=',', quotechar="'")]

                lower_incorrect_first_row = [[word.lower() for word in x] for x in incorrect_first_row]

                header_values_v1 = [x.lower() for x in ['sourcedid','title','classType','schoolSourcedId','termSourcedId','status','dateLastModified','grade','courseSourcedId','classCode','classCode','location','subjects']]
                header_values_v1_1 = [x.lower() for x in ['sourcedid','status','dateLastModified','title','grades','courseSourcedId','classCode','classCode','classType','location','schoolSourcedId','termSourcedIds','subjects','subjectCodes','periods']]

                if or_v1 == True:
                    for a in lower_incorrect_first_row[0]:
                        if a in header_values_v1:
                            header_values_v1.remove(a)

                    if len(header_values_v1) == 0:
                        pass
                    else:
                        print('\n')
                        print('classes.csv errors:')
                        for b in header_values_v1:
                            print('Header row value missing: {} '.format(b))

                if or_v1_1 == True:
                    for a in lower_incorrect_first_row[0]:
                        if a in header_values_v1_1:
                            header_values_v1_1.remove(a)

                    if len(header_values_v1_1) == 0:
                        pass
                    else:
                        print('\n')
                        print('classes.csv errors:')
                        for b in header_values_v1_1:
                            print('Header row value missing: {} '.format(b))

        except FileNotFoundError:
                print('\n')
                print('No classes.csv file found')

    #Checking Enrollments

    def enrollments_header_checker(self):
        try:
            with open('./roster/enrollments.csv', 'r') as file:
                incorrect_first_row = [x for x in csv.reader(file, delimiter=',', quotechar="'")]

                lower_incorrect_first_row = [[word.lower() for word in x] for x in incorrect_first_row]

                header_values_v1 = [x.lower() for x in ['sourcedid','classSourcedId','schoolSourcedId','userSourcedId','role','status','dateLastModified','primary']]
                header_values_v1_1 = [x.lower() for x in ['sourcedid','status','dateLastModified','classSourcedId','schoolSourcedId','userSourcedId','role','primary','beginDate','endDate']]

                if or_v1 == True:
                    for a in lower_incorrect_first_row[0]:
                        if a in header_values_v1:
                            header_values_v1.remove(a)

                    if len(header_values_v1) == 0:
                        pass
                    else:
                        print('\n')
                        print('enrollments.csv errors:')
                        for b in header_values_v1:
                            print('Header row value missing: {} '.format(b))

                if or_v1_1 == True:
                    for a in lower_incorrect_first_row[0]:
                        if a in header_values_v1_1:
                            header_values_v1_1.remove(a)

                    if len(header_values_v1_1) == 0:
                        pass
                    else:
                        print('\n')
                        print('enrollments.csv errors:')
                        for b in header_values_v1_1:
                            print('Header row value missing: {} '.format(b))

        except FileNotFoundError:
                print('\n')
                print('No enrollments.csv file found')

    #Checking AcademicSessions

    def academic_sessions_header_checker(self):
        try:
            with open('./roster/academicSessions.csv', 'r') as file:
                incorrect_first_row = [x for x in csv.reader(file, delimiter=',', quotechar="'")]

                lower_incorrect_first_row = [[word.lower() for word in x] for x in incorrect_first_row]

                header_values_v1 = [x.lower() for x in ['sourcedid','status','dateLastModified','title','type','startDate','endDate','parentSourcedId']]
                header_values_v1_1 = [x.lower() for x in ['sourcedid','status','dateLastModified','title','type','startDate','endDate','parentSourcedId','schoolYear']]

                if or_v1 == True:
                    for a in lower_incorrect_first_row[0]:
                        if a in header_values_v1:
                            header_values_v1.remove(a)

                    if len(header_values_v1) == 0:
                        pass
                    else:
                        print('\n')
                        print('academicSessions.csv errors:')
                        for b in header_values_v1:
                            print('Header row value missing: {} '.format(b))

                if or_v1_1 == True:
                    for a in lower_incorrect_first_row[0]:
                        if a in header_values_v1_1:
                            header_values_v1_1.remove(a)

                    if len(header_values_v1_1) == 0:
                        pass
                    else:
                        print('\n')
                        print('academicSessions.csv errors:')
                        for b in header_values_v1_1:
                            print('Header row value missing: {} '.format(b))

        except FileNotFoundError:
                print('\n')
                print('No academicSessions.csv file found')

    #Checking AcademicSessions

    def demographics_header_checker(self):
        try:
            with open('./roster/demographics.csv', 'r') as file:
                incorrect_first_row = [x for x in csv.reader(file, delimiter=',', quotechar="'")]

                lower_incorrect_first_row = [[word.lower() for word in x] for x in incorrect_first_row]

                header_values_v1 = [x.lower() for x in ['userSourcedId','status','dateLastModified','birthDate','sex','americanIndianOrAlaskaNative','asian','blackOrAfricanAmerican','nativeHawaiianOrOtherPacificIslander','white','demographicRaceTwoOrMoreRaces','hispanicOrLatinoEthnicity','countryOfBirthCode','stateOfBirthAbbreviation','cityOfBirth','publicSchoolResidenceStatus']]
                header_values_v1_1 = [x.lower() for x in ['sourcedid','status','dateLastModified','birthDate','sex','americanIndianOrAlaskaNative','asian','blackOrAfricanAmerican','nativeHawaiianOrOtherPacificIslander','white','demographicRaceTwoOrMoreRaces','hispanicOrLatinoEthnicity','countryOfBirthCode','stateOfBirthAbbreviation','cityOfBirth','publicSchoolResidenceStatus']]

                if or_v1 == True:
                    for a in lower_incorrect_first_row[0]:
                        if a in header_values_v1:
                            header_values_v1.remove(a)

                    if len(header_values_v1) == 0:
                        pass
                    else:
                        print('\n')
                        print('demographics.csv errors:')
                        for b in header_values_v1:
                            print('Header row value missing: {} '.format(b))

                if or_v1_1 == True:
                    for a in lower_incorrect_first_row[0]:
                        if a in header_values_v1_1:
                            header_values_v1_1.remove(a)

                    if len(header_values_v1_1) == 0:
                        pass
                    else:
                        print('\n')
                        print('demographics.csv errors:')
                        for b in header_values_v1_1:
                            print('Header row value missing: {} '.format(b))

        except FileNotFoundError:
                print('\n')
                print('No demographics.csv file found')

    #Checking Manifest
    if or_v1_1 == True:
        try:
            def manifest_header_checker(self):
                with open('./roster/manifest.csv', 'r') as file:
                    incorrect_first_row = [x for x in csv.reader(file, delimiter=',', quotechar="'")]

                    lower_incorrect_first_row = [[word.lower() for word in x] for x in incorrect_first_row]

                    header_values_v1_1 = [x.lower() for x in ['manifest.version','oneroster.version','file.academicSessions','file.categories','file.classes','file.classResources','file.courses','file.courseResources','file.demographics','file.enrollments','file.lineItems','file.orgs','file.resources','file.results','file.users','source.systemName','source.systemCode']]

                    if or_v1_1 == True:
                        for a in lower_incorrect_first_row[0]:
                            if a in header_values_v1_1:
                                header_values_v1_1.remove(a)

                        if len(header_values_v1_1) == 0:
                            pass
                        else:
                            print('\n')
                            print('manifest.csv errors:') 
                            for b in header_values_v1_1:
                                print('Header row value missing: {} '.format(b))

        except FileNotFoundError:
                print('\n')
                print('No manifest.csv file found')
