import os


def send_email(user, pwd, recipients, subject, body):
    import smtplib

    if type(recipients) is not list:
        recipients = [recipients]

    # Prepare actual message

    message = "From: %s" + "\n" \
              "To: %s" + "\n" \
              "Subject: %s" + "\n\n" \
              "%s" \
              % user, ",".join(recipients), subject, body

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(user, pwd)
        server.sendmail(user, recipients, message)
        server.close()

        print 'successfully sent the mail'

    except:
        print "failed to send mail"


def get_file_paths(directory):
    """
    This function will generate the file names in a directory
    tree by walking the tree either top-down or bottom-up. For each
    directory in the tree rooted at directory top (including top itself),
    it yields a 3-tuple (dirpath, dirnames, filenames).
    """
    file_paths = []  # List which will store all of the full filepaths.

    # Walk the tree.
    for root, directories, files in os.walk(directory):
        for filename in files:
            # Join the two strings in order to form the full filepath.
            file_path = os.path.join(root, filename)
            file_paths.append(file_path)  # Add it to the list.

    return file_paths  # Self-explanatory.


def filename_assistant(data_folder):

    # Run the above function and store its results in a variable.
    full_file_paths = get_file_paths(data_folder)

    print "\t~~~~~~~~~~~~~~~~~~~~~~"
    print "\t~ Filename Assistant ~"
    print "\t~~~~~~~~~~~~~~~~~~~~~~"
    print ""
    
    mouse = raw_input("\tMouse : ")

    if mouse != '':
        # Store Mouse Names
        task_list = []
        for path in full_file_paths:
            if path.endswith(".txt"):
                filename = path.split('/')[-1]

                if filename.startswith(mouse):
                    f2 = filename.split('_')
                    if len(f2) == 5:
                        task = f2[1]
                        if task not in task_list:
                            task_list.append(task)

        for i, task in enumerate(task_list):
            print "\t[" + str(i) + "] " + task

        task_number = input("\tTask : ")
        task_to_find = task_list[task_number]

        session_list = []
        for path in full_file_paths:
            if path.endswith(".txt"):
                filename = path.split('/')[-1]

                if filename.startswith(mouse):
                    f2 = filename.split('_')
                    if len(f2) == 5:
                        task = f2[1]

                        if task == task_to_find:
                            # print f2
                            session = f2[2]
                            if session not in session_list:
                                session_list.append(int(session))

        # print session_list

        max_session = max(session_list)

        new_filename = mouse + "_" + task_to_find + "_%02d" % (max_session + 1)
        use_filename = raw_input("\tDo you accept the following filename :" + new_filename + " (Y) ? ")

        if use_filename == 'Y':
            return new_filename

    new_filename = raw_input("\tEnter a new filename : ")
    # print "\t" + new_filename

    return new_filename
