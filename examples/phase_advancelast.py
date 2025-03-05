import openhtf as htf
from openhtf.util import units

def setup_phase(test):
    return htf.PhaseResult.CONTINUE

def first_measurement_phase(test):
    return htf.PhaseResult.CONTINUE

def second_measurement_phase(test):
    return htf.PhaseResult.STOP

def teardown_phase(test):
    return htf.PhaseResult.CONTINUE

def main():
    test = htf.Test(
        htf.PhaseGroup(
            setup=[setup_phase],
            main=[first_measurement_phase, second_measurement_phase],
            teardown=[teardown_phase],
        )
    )
    test.execute(lambda: "PCB001")

if __name__ == '__main__':
    main()