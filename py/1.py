#-------------------------------------------------------------------------------
# Name:        модуль1
# Purpose:
#
# Author:      Dmitry
#
# Created:     08.04.2013
# Copyright:   (c) Dmitry 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------


import os, subprocess, threading


def main():
    print("hello, world")
    pass

def run_calc(onExit):

    def run():
        proc = subprocess.Popen('calc')
        proc.wait()
        print('ok')
        onExit()

    thread = threading.Thread(target = run)
    thread.start()

    def f():
        print('ok')


def e():
    print('exited')

if __name__ == '__main__':
    main()
    run_calc(e)
