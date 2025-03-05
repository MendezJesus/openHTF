import openhtf as htf
import random

def phase_pass(test):
    return htf.PhaseResult.CONTINUE

def phase_retry(test):
    if random.choice([True, False]):
        return htf.PhaseResult.CONTINUE
    else:
        return htf.PhaseResult.REPEAT

def phase_fail(test):
    return htf.PhaseResult.STOP

def main():
    test = htf.Test(phase_pass, phase_retry, phase_fail)
    test.execute(lambda: "PCB001")

if __name__ == '__main__':
    main()