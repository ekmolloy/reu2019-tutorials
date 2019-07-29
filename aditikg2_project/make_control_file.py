import sys

def make_control_file(tree_f_name, control_f_name):
    
    log = open(tree_f_name.replace(".bestTree", ".log"), 'r')
    control = open(control_f_name, 'w+')

    log_lines = log.readline()
    control = control.readlines()
