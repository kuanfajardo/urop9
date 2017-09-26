import os
import serial  # library to read data from Arduino board through USB connection
from time import strftime, localtime # Library to read the current date and time to create the output filename


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


def setup_serial(port):
    # configure the serial connections check in the arduino editor menu the name of the port
    # and the baudrate that are used to communicate with the arduino

    ser = serial.Serial(
        port=port,
        baudrate=115200,
        parity=serial.PARITY_ODD,
        stopbits=serial.STOPBITS_TWO,
        bytesize=serial.SEVENBITS
    )

    # Just in case the connection was still open from a previous execution of the program
    if ser.isOpen():
        ser.close()

    ser.open()
    # The arduino is waiting for input, so we can flush input
    # and output buffers at thea time for communication safety
    ser.flushInput()
    ser.flushOutput()

    return ser


def open_file(data_folder, box):
    filename = filename_assistant(data_folder)
    time_str = strftime("_%Y%m%d-%H%M", localtime())
    extension = "_box" + box + ".txt"

    file_path = data_folder + filename + time_str + extension

    # print("Name = " + filename)

    fo = open(file_path, "w")

    return fo


def establish_connection(ser):
    expected_response = "Let's Go!"
    connected = False

    print ""
    print ""

    print "\tArduino Could You Hear Us ??"
    while not connected:
        print "\tPC ==> Do You Wanna Go?"
        ser.write("Do You Wanna Go?")
        out = ser.readline()
        out = out.strip()  # to remove the end line char
        print("\tARDUINO ==> " + out)
        if out == expected_response:
            connected = True

    print("\tConnection with Arduino Established!")
    print ""
    print ""
    print "\tExperiment Started"
