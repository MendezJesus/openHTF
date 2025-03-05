import openhtf as htf
from openhtf.util import units

@htf.measures(
    htf.Measurement("temperature")
    .in_range(0,100)
    .with_units(units.DEGREE_CELSIUS)
    .with_precision(1)
)
def phase_temperature(test):
    test.measurements.temperature = 25

def main():
    test = htf.Test(phase_temperature)
    test.execute(lambda: "PCB001")

if __name__ == '__main__':
    main()

