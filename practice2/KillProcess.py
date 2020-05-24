import os


def kill_process(name):
    try:
        code = os.system("taskkill /F /T /IM "+name)
        if code == 0:
            print("Process Killed Successfully")
        else:
            print("Process is not exists")

    except Exception as e:
        print("User Raised Exception Occurred", e)


kill_process("firefox.exe")
#kill_process("chromedriver.exe")

