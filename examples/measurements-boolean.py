import openhtf as htf
from openhtf import units


@htf.measures(
    htf.Measurement("is_led_switch_on")
    .equals(True)
)
def phase_led(test):
    test.measurements.is_led_switch_on = True

def main():
    test = htf.Test(phase_led)
    test.execute(lambda: "PCB001")

if __name__ == "__main__":
    main()

