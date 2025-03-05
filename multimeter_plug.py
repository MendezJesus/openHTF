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
        self.connected = False

    def measure_voltage(self):
        # Simulate voltage measurement
        return random.uniform(0, 10)

    def measure_current(self):
        # Simulate current measurement
        return random.uniform(0, 2)

    def get_id(self):
        # returns identity
        return self.session.query('*IDN?')
