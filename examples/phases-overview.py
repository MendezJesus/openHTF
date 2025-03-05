import openhtf as htf

def phase_one(test):
    return htf.PhaseResult.CONTINUE

def phase_two(test):
    return htf.PhaseResult.CONTINUE

def main():
    test = htf.Test(phase_one, phase_two)
    test.execute(lambda: "PCB001")

if __name__ == '__main__':
    main()