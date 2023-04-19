"""
# Pipe 를 이용한 프로세스간 통신
# pipein , pipeout -> os.pipe()
# pipein -> write , pipeout -> read
"""

import multiprocessing
import os, sys
import traceback


class ChildProcess(multiprocessing.Process):
    def __init__(self, pipein):
        super(ChildProcess, self).__init__()
        self.pipein = pipein

    def run(self):
        try:
            raise Exception("This broke stuff")
        except:
            except_type, except_class, tb = sys.exc_info()

        print("Attempting to pipeline to pipe")
        self.pipein = os.fdopen(self.pipein, "w")
        self.pipein.write("My Name is LEE")
        self.pipein.close()


def main():
    pipeout, pipein = os.pipe()
    child = ChildProcess(pipein)
    child.start()
    child.join()

    os.close(pipein)
    pipeout = os.fdopen(pipeout)
    print(f"Pipe : {pipeout.read()}")


if __name__ == "__main__":
    main()
