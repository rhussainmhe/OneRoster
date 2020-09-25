import os.path

or_files = ['orgs.csv','users.csv','courses.csv','classes.csv','enrollments.csv','academicSessions.csv','demographics.csv','manifest.csv']
files = []
or_v1 = False
or_v1_1 = False


#Double check if this makes sense.. (the elif)

class FileChecker:

    def version_checker(self):
        global or_files
        global files

        for file_name in or_files:
            if os.path.exists('./roster/' + file_name):
                files.append(file_name)


    def manifest_check(self):
        global files
        global or_v1
        global or_v1_1
        global or_files

        if 'manifest.csv' in files:
            or_v1_1 = True
        elif 'manifest.csv' not in files:
            or_v1 = True
            or_files.remove('manifest.csv')


file_check = FileChecker()
file_check.version_checker()
file_check.manifest_check()
#print statement of version here?

if or_v1 == True:
    print('One Roster v1.0 files found')
elif or_v1_1 == True:
    print('One Roster v1.1 files found')
else:
    pass
