
import os
import csv
import datetime
import shutil

def is_gradebook(filename):
    if filename[0:9] == 'gradebook':
        return True
    else:
        return False

def is_correct_gradebook(filename, period):
    with open(filename) as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            if reader.line_num == 2:
                for key in keys_for_period_for_gradebooks:
                    if keys_for_period_for_gradebooks[key] == row[0] and key == period:
                        return True
                return False


if __name__ == '__main__':

    folder_path_gradebooks_and_score_templates = "/Users/christopherrogers/Desktop/Gradebooks and Score Templates"

    folder_path_cloud_downloads = "/Users/christopherrogers/OneDrive - Collierville Schools/Cloud Downloads"

    folder_path_schoology_gradebooks = "/Users/christopherrogers/Desktop/Work Programs/Schoology Gradebooks"

    folder_path_downloads = "/Users/christopherrogers/Downloads"

    folder_path_desktop = "/Users/christopherrogers/Desktop"

    now = datetime.datetime.now()
    print(now.date())

    #Clears folder and contents to make room for next set of gradebooks and score templates.
    if os.path.isdir(folder_path_gradebooks_and_score_templates):
        shutil.rmtree(folder_path_gradebooks_and_score_templates)

    list_of_paths_for_gradebooks_and_assignments = []

    # Check Cloud Downloads folder for most recent and relevant assignment score template files
    # Maybe timestamp the start of this program and instruct user to download assignment score templates and tell the program to
    # continue once all templates have been downlaoded. Then, check folder for files that were created after the starting timestamp
    # of this run of the program. Append file paths to list.

    print('In the actual implementation of this code, this is when the user, or me, is prompted to download the gradebook templates from the gradebook web applications for the corresponding assignments for which grades will be updated.')
    print('Download the Scores Templates for the assignments to which you want grades transferred.')

    # Waits for user to download the Score Templates for the assignments until user enters 'go' to proceed program.
    waiting = True
    while waiting:
        entry = input('Type \'go\' when you are ready to continue. ')
        if entry == 'go':
            waiting = False

    # Goes to download folder to which Score Templates are downloaded and looks for downloads that occured since the start of this program in order to find only those gradebooks that are to be worked with.
    os.chdir(folder_path_cloud_downloads)
    for filename in os.listdir(folder_path_cloud_downloads):
        if os.stat(filename)[8] > now.timestamp():
            list_of_paths_for_gradebooks_and_assignments.append(os.path.abspath(filename))

    #Goes to folder of Schoology gradebooks in order to see if gradebooks that are in the folder were made today and there for up to date.
    os.chdir(folder_path_schoology_gradebooks)
    date_today = now.date()
    today_datetime = datetime.datetime(date_today.year, date_today.month, date_today.day)
    all_made_today = True
    looking = True

    if len((os.listdir(folder_path_schoology_gradebooks))) == 0 or (
            len((os.listdir(folder_path_schoology_gradebooks))) and os.listdir(folder_path_schoology_gradebooks)[
        0] == '.DS_Store'):
        all_made_today = False
        looking = False
    for filename in os.listdir(folder_path_schoology_gradebooks):
        if looking:
            if os.stat(filename)[8] < today_datetime.timestamp():
                all_made_today = False
                looking = False

    if all_made_today:
        print('all_made_today is True')
    elif not all_made_today:
        print('all_made_today is False')

        # Iterate through Schoology Gradebooks folder to remove gradebooks in order to make room for the most recent versions.
        os.chdir(folder_path_schoology_gradebooks)
        for filename in os.listdir(folder_path_schoology_gradebooks):
            os.remove(filename)

        # Run another file that downloads Schoology gradebooks for each class period to the downloads folder.
        exec(open("/Users/christopherrogers/Desktop/Work Programs/Download Schoology Gradebooks.py").read())

        # Goes to downloads folders and searches for Schoology gradebooks that were downloaded since the start of the program and copies them to the Schoology Gradebooks folder.
        os.chdir(folder_path_downloads)
        list_for_checking = []
        print(now.timestamp())
        for filename in os.listdir(folder_path_downloads):
            if filename != '.DS_Store':
                list_for_checking.append(filename)
                if os.stat(filename)[8] > now.timestamp():
                    shutil.copy(os.path.abspath(filename), folder_path_schoology_gradebooks)
        list_for_checking.sort()

    # Make a list of file paths for the Schoology Gradebooks to be iterated through later.
    os.chdir(folder_path_schoology_gradebooks)
    for filename in os.listdir(folder_path_schoology_gradebooks):
        list_of_paths_for_gradebooks_and_assignments.append(os.path.abspath(filename))

    for filename in os.listdir(folder_path_schoology_gradebooks):
        if filename != '.DS_Store':
            if os.stat(filename)[8] > now.timestamp():
                list_of_paths_for_gradebooks_and_assignments.append(os.path.abspath(filename))

    # Make Gradebooks and Score Templates on the Desktop to be easily access when uploaded final versions of Score Templates after program is complete.
    os.chdir(folder_path_desktop)
    folder_name = 'Gradebooks and Score Templates'
    os.mkdir(folder_path_desktop + "/" + folder_name)
    os.chdir(folder_path_desktop + "/" + folder_name)

    # Copy Gradebooks to Desktop Folder above to be backed up and easily accessed if needed.
    for file_path in list_of_paths_for_gradebooks_and_assignments:
        shutil.copy(file_path, os.path.basename(file_path))
    filenames_in_folder = os.listdir()

    # List of students whose data does not show up in the gradebook download and must be manually entered later.
    names_for_manual = ['Rose, Aidan', 'Seitz, Colton', 'Gray, Mei Mei', 'Boyce, D\'Arcy']
    manual_notice_lines = []

    for filename in filenames_in_folder:
        print(filename)
        if filename[0:9] != 'gradebook':
            if filename != '.DS_Store':
                max_assignment_row = 0
                assignment_rows = []
                with open(filename) as f:
                    reader = csv.reader(f, delimiter=',')
                    for row in reader:
                        if row[-1] == '':
                            row.pop()
                        max_assignment_row = reader.line_num
                        assignment_rows.append(row)
                assignment_title = assignment_rows[2][1]
                print(assignment_title)
                is_quiz = False
                if 'Quiz' in assignment_title:
                    is_quiz = True
                    print('----------------------')
                    print('- ' + assignment_title, end='')
                    points_returned = input('How many points need to be returned?\n')
                    print('This many points will be returned: ' + str(points_returned))
                    print('----------------------')

                keys_for_period_for_assignments = {
                    '2nd': 'Achanta, Chris',
                    '3rd': 'Bone, Devin',
                    '4th': 'Chen, Matt',
                    '5th': 'Bisignano, Drew',
                    '7th': 'Amaechi, Jonathan',
                    '8th': 'Amaba, Troy',
                }

                keys_for_period_for_gradebooks = {
                    '2nd': 'Chris',
                    '3rd': 'Devin',
                    '4th': 'Matt',
                    '5th': 'Drew',
                    '7th': 'Jonathan',
                    '8th': 'Troy',
                }

                period = ''

                for key in keys_for_period_for_assignments:
                    if assignment_rows[8][1] == keys_for_period_for_assignments[key]:
                        period = key

                for gradebook in filenames_in_folder:
                    if is_gradebook(gradebook):
                        if is_correct_gradebook(gradebook, period):
                            max_gradebook_row = 0
                            gradebook_rows = []
                            grades = []
                            with open(gradebook) as f:
                                reader = csv.reader(f, delimiter=',')
                                for row in reader:
                                    gradebook_rows.append(row)
                                    max_gradebook_row = reader.line_num
                                    if reader.line_num == 1:
                                        col_titles = row
                                        for item in col_titles:
                                            if '(Individual)' in item:
                                                continue
                                            if (assignment_title in item) and ('Upload Work' not in item):
                                                assignment_col_index = col_titles.index(item)
                                                # print(assignment_col_index)
                                for i in range(1, max_gradebook_row):
                                    grades.append(gradebook_rows[i][assignment_col_index])

                                if is_quiz:
                                    grade_as_float = 0
                                    points_returned_as_float = float(points_returned)
                                    for i in range(len(grades)):
                                        if grades[i] == '':
                                            continue
                                        else:
                                            grade_as_float = float(grades[i])
                                            grades[i] = str(grade_as_float + points_returned_as_float)
                        else:
                            continue
                    else:
                        continue
                print(period + ' - ' + assignment_title + '.csv')
                print(filename)
                print(grades)
                with open(period + ' - ' + assignment_title + '.csv', 'w', newline='') as csvfile:
                    writer = csv.writer(csvfile, delimiter=',')
                    row_num = 1
                    for row in assignment_rows:
                        if row_num <= 8:
                            writer.writerow(row)
                        if row_num > 8 and row_num <= max_assignment_row:
                            row_for_writing = [row[0], row[1], grades[row_num - 9]]
                            if row[1] in names_for_manual:
                                manual_notice_lines.append(
                                    period + ', ' + row[1] + ', ' + grades[row_num - 9] + ' - ' + assignment_title)
                            writer.writerow(row_for_writing)
                        row_num += 1

    manual_notice_lines.sort()
    print('---------------------------')
    print('You need to manually enter these grades:')
    print()
    for line in manual_notice_lines:
        print(line + '\n')

