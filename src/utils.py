def verifyInterfaceState (telnetObj, interface, state = "up") :
    """
    Verifies if mentioned interface matches with the state
    :param telnetObj: Obj of Telnet class on which connection command is to be run
    :param interface: A string holding interface name
    :param state: A string holding "up"/"down" states of interface
    :return: 1 if state matches on device, else 0
    -couseph@cisco.com
    """
    output = send (telnetObj,"show interface "+interface)
    print (output)
    if state == "up":
        if re.search(".*up.*line protocol is up.*",output):
            return 1
    elif state == "down":
        if re.search(".*administratively down.*line protocol is down.*",output):
            return 1
    else:
        print ("Incorrect Interface/state in argument.")
    return 0

def send (telnetObj, command, mode = "default", prompt = ""):

    """
    Runs command on the Telnet connection and returns the output
    :param telnetObj: Obj of Telnet class on which connection command is to be run
    :param command: A string holding the command to be run
    :param mode: A string specifying exec/config modes for command execution
    :param prompt: A string holding the device prompt
    :return: A string containing output from device
    """

    output = ("a","b","c")
    if mode == "exec" :
        telnetObj.write("end\r")
        if (telnetObj.expect([re.compile(".*"+prompt+"#"),], 10))[0] != -1 :
            telnetObj.write(command+"\n")
            #telnetObj.read_until(prompt+"#")
            output = telnetObj.expect([re.compile(prompt + "#"),], 10)
            if (telnetObj.expect([re.compile(".*confirm.*"),], 10))[0] != -1 :
                telnetObj.write("\n")

    elif mode == "config" :
        telnetObj.write("end\r")
        if (telnetObj.expect([re.compile(prompt+"#"),], 10))[0] != -1 :
            telnetObj.write("conf t\n")
            #print ("conf t\n")
            if (telnetObj.expect([re.compile(prompt+"\(config\)#"), ], 10))[0] != -1:
                telnetObj.write(command+"\n")
                output = telnetObj.expect([re.compile(prompt+"\(config.*\)#"),], 10)

    else:
        telnetObj.write("\r")
        if (telnetObj.expect([re.compile(".*" + "#"), ], 10))[0] != -1:
            telnetObj.write(command + "\n")
            telnetObj.read_until(prompt+"#")
            output = telnetObj.expect([re.compile(".*#"), ], 10)
            if (telnetObj.expect([re.compile(".*confirm.*"), ], 10))[0] != -1:
                telnetObj.write("end\r")
    return output[2]

