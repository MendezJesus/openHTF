from openhtf import Test, PhaseResult
from tofupilot.openhtf import TofuPilot

def get_sn(test):
    test.test_record.dut_id = 'PCB001'
    return PhaseResult.CONTINUE

def main():
    test = Test(get_sn)
    with TofuPilot(test):
      test.execute()

if __name__ == '__main__':
    main()
