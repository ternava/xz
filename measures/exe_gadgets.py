import os
import subprocess

from options import all_options

stats_file = "measures/gadgets_2-200.csv"
exe_path = "./src/xz/xz"

def compilexz(compile_time_opt):
    subprocess.run(["make", "clean"])
    subprocess.run(["./configure"] + ["--disable-shared"] + compile_time_opt)
    subprocess.run(["make"])

def ropgadget():
    p = subprocess.run(["ROPgadget", "--binary", exe_path], 
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT)
    print(p)
    nr_of_gadgets = p.stdout.decode('ascii').split()[-1]
    return nr_of_gadgets


def calculate_percentage(org_nr, res_nr): 
    if((org_nr - res_nr) > 0):
        return str("{:.4%}".format(1 - (res_nr/org_nr))) + " less" 
    elif((org_nr - res_nr) < 0):
        return str("{:.4%}".format(abs(1 - (res_nr/org_nr)))) + " more"
    else:
        return str("{:.4%}".format(1 - (res_nr/org_nr))) 

def print_nr_gadgets(opt, nr_of_gardgets_01, nr_of_gardgets_02): 
    print("The unique number of found gadgets when " +
        str(opt) + " is removed: " +
        str(nr_of_gardgets_02) + ". Or, " + 
        calculate_percentage(int(nr_of_gardgets_01), int(nr_of_gardgets_02)), 
                            file=open(stats_file, "a"))

def do_operations():
    compilexz([])
    nr_of_gadgets_01 = ropgadget()
    print("The original unique number of found gadgets is: " +
        str(nr_of_gadgets_01), file=open(stats_file, "a"))

    for opt in all_options:
        compilexz(opt)
        nr_of_gadgets_02 = ropgadget()
        print_nr_gadgets(opt, nr_of_gadgets_01, nr_of_gadgets_02)

if os.path.exists(stats_file):
    os.remove(stats_file)
    do_operations()
else: 
    do_operations()