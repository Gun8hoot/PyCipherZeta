import os, sys, time

def wreport(method, string, encoded, key):
    path = "report/"
    curr_time = time.strftime('-%H:%M:%S-%d_%m_%Y')

    try:
        os.makedirs("report/")
    except FileExistsError:
        pass
    
    try:
        f = open(f"{path}{method}{curr_time}","w")
        f.writelines(f"{method} | {string} : {encoded} ")
        if len(key) < 1:
            pass
        elif len(key) > 1:
            f.writelines("\n\n")
            f.writelines(f"Key : {key}")
    except ValueError:
        pass