# Unzipper:
from unzip import *
import os.path
import shutil

#Dont run if ./roster directory already exists

if not os.path.exists(file_path):

    #Extract roster.zip:

    extract = Unzipper()
    extract.roster_unzip()

    # Check the version of One Roster based on which files exist after unzipped
    from or_version_check import *

    # Import CSV file header checker file
    from csv_checker import *

    # check CSV file headers based on version
    check_csv_headers = CsvChecker()
    check_csv_headers.orgs_header_checker()
    check_csv_headers.users_header_checker()
    check_csv_headers.courses_header_checker()
    check_csv_headers.classes_header_checker()
    check_csv_headers.enrollments_header_checker()
    check_csv_headers.academic_sessions_header_checker()
    check_csv_headers.demographics_header_checker()

    # Run 1.1 checks if manifest.csv exists
    if or_v1_1 == True:
        check_csv_headers.manifest_header_checker()

    # Delete ./roster

        shutil.rmtree('./roster')

    else:
        pass


else:
    print('Err: "/roster/" folder already exists in directory!  Delete or rename folder before executing.')
