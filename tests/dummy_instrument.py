import numpy as np
from numpy import random

from itatools import itaw

class DummyInstrument:
    def __init__(self):
        self.address = 'TCPIP0::172.16.10.10::inst0::INSTR'

    def get_trace(self, npt=10000, **kwargs):
        """Reads a current trace from the instrument. Does not initiate or 
        stop data acquisition.

        Args:
            n: 
                Trace number.
            mem: 
                Selects between reading a currently displayed trace (False) 
                and reading a reference stored in the memory (True).

        Returns:
            A dictionary with the x and y data (under the keys 'x' and 'y'), 
            and metadata.
        """
        
        x = np.linspace(-5, 5, npt)
        y = (np.sin(x + 2*np.pi*random.random_sample())
             + 0.5*np.random.rand(len(x)))

        # d = {'x': x, 'y': y,
        #      'name_x': 'Time', 'unit_x': 's',
        #      'name_y': 'Voltage', 'unit_y': 'V'}

        d = {'x': x, 'y': y, 'xlabel': 'Time (s)', 'ylabel': 'Voltage (V)'}

        return d


if __name__ == "__main__":
    di = DummyInstrument()
    it = itaw(get_trace=di.get_trace)
