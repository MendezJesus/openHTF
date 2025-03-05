import openhtf as htf
from tofupilot.openhtf import TofuPilot

def phase_one(test):
    return htf.PhaseResult.CONTINUE

def phase_two(test):
    return htf.PhaseResult.CONTINUE

def main():
    test = htf.Test(phase_one, phase_two, part_number="PCBA01",)
    with TofuPilot(test):
        test.execute()

if __name__ == '__main__':
    main()