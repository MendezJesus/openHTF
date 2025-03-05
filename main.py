import openhtf as htf
from openhtf.util import units
from openhtf.util.configuration import CONF, bind_init_args
from multimeter_plug import MultimeterPlug
from tofupilot.openhtf import TofuPilot

IP_ADDR_1 = CONF.declare("ip_addr_1", default_value='TCPIP::192.168.50.207::INSTR')

MultimeterPlug1 = bind_init_args(MultimeterPlug, IP_ADDR_1)

@htf.measures(
    htf.Measurement("voltage")
    .in_range(0, 10)
    .with_units(units.VOLT)
    .with_precision(1)
)
@htf.plug(multimeter=MultimeterPlug1)
def phase_voltage(test, multimeter):
    # Use the plug to measure voltage
    voltage = multimeter.measure_voltage()
    test.measurements.voltage = voltage

@htf.measures(
    htf.Measurement("device_id")
    .equals("Keysight Technologies,34465A,MY64003895,A.03.03-03.15-03.03-00.52-05-02")
)
@htf.plug(multimeter=MultimeterPlug1)
def phase_getID(test, multimeter):

    device_id = multimeter.get_id()
    test.measurements.device_id = device_id

def main():
    test = htf.Test(phase_voltage, phase_getID)
    #test.execute(lambda: "PCB001")
    with TofuPilot(test):
        test.execute(lambda: "TestB001")

if __name__ == "__main__":
    main()
