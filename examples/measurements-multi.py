import openhtf as htf
from openhtf.util import units

@htf.measures(
    htf.Measurement("is_connected").equals(True),
    htf.Measurement("firmware_version").equals("1.2.4"),
    htf.Measurement("temperature")
    .in_range(0,100)
    .with_units(units.DEGREE_CELSIUS),
)
def phase_multi_measurements(test):
    test.measurements.is_connected = True
    test.measurements.firmware_version = "1.2.4"
    test.measurements.temperature = 22.5

def main():
    test = htf.Test(phase_multi_measurements)
    test.execute(lambda: "PCB001")

if __name__ == "__main__":
    main()