import openhtf as htf
import random

@htf.PhaseOptions(timeout_s= 5)
def phase_pass(test):
    return htf.PhaseResult.CONTINUE

@htf.PhaseOptions(repeat_limit=3)
def phase_entry(test):
    if random.choice([True, False]):
        return htf.PhaseResult.CONTINUE
    else:
        return htf.PhaseResult.REPEAT

def main():
    test = htf.Test(phase_pass, phase_entry)
    test.execute(lambda: "PCB001")

if __name__ == '__main__':
    main()