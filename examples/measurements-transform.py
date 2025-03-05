import openhtf as htf

@htf.measures(
    htf.Measurement("voltage")
    .in_range(0,10)
    .with_transform(lambda x: x * 1.1)
    .with_units("V")
)
def phase_voltage(test):
    test.measurements.voltage = 5

def main():
    test = htf.Test(phase_voltage)
    test.execute(lambda: "PCB001")

if __name__ == "__main__":
    main()