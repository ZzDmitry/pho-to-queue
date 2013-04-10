#-------------------------------------------------------------------------------
# Name:        РјРѕРґСѓР»СЊ1
# Purpose:
#
# Author:      Dmitry
#
# Created:     08.04.2013
# Copyright:   (c) Dmitry 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------


import os, subprocess, threading


to_run = 3


def run_calc_sync(wait):

    def run():
        while True:
            proc = subprocess.Popen('calc')
            proc.wait()
            print('calc wait done')

    print('run calc sync')
    thread = threading.Thread(target = run)
    thread.start()
    if wait:
        thread.join()
        print('join')


def run_next(onExit):
    global to_run
    def run():
        global to_run
        proc = subprocess.Popen('calc')
        proc.wait()
        #exit_calc_index(index)
        print('calc wait done')
        to_run += 1
        #onExit()

    print('run_next ' + str(to_run))
    if to_run < 0:
        raise "to_run < 0"
    thread = threading.Thread(target = run)
    thread.start()
    to_run -= 1
    if not to_run:
        thread.join()
        print('join')




def main():
    for i in range(to_run):
        print(i)
        run_calc_sync(i == to_run - 1)
    pass

def exit_calc_index(index):
    print('exit ' + str(index))

def run_calc_index(index):

    def run():
        proc = subprocess.Popen('calc')
        proc.wait()
        exit_calc_index(index)

    print('run ' + str(index))
    thread = threading.Thread(target = run)
    thread.start()
    thread.join()
    print('join ' + str(index))

if __name__ == '__main__':
    main()
    print('terminated')