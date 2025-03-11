from openhtf import plugs
import random
import pyvisa

class MultimeterPlug(plugs.BasePlug):
    def __init__(self, ip_addr: str):
        # Simulate connecting to the multimeter
        self.ip_addr = ip_addr
        rm = pyvisa.ResourceManager()
        rm.list_resources()
        self.session = rm.open_resource(self.ip_addr)
        self.connected = True

    def tearDown(self):
        # Automatically called by OpenHTF after the test to clean up
        self.session.close()
        self.connected = False

    def measure_voltage_dc(self):
        # Measures DC voltage
        return float(self.session.query('MEASure:VOLTage:DC?'))

    def measure_voltage_ac(self):
        # Measures AC voltage
        return float(self.session.query('MEASure:VOLTage:AC?'))

    def measure_current_dc(self):
        # Measures DC current
        return float(self.session.query('MEASure:CURRent:DC?'))

    def measure_current_ac(self):
        # Measures AC current
        return float(self.session.query('MEASure:CURRent:AC?'))

    def measure_resistance(self):
        # Measure Resistance
        return float(self.session.query('MEASure:RESistance?'))

    def get_id(self):
        # returns identity
        return self.session.query('*IDN?')
