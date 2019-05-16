import serial
import time
import serial.tools.list_ports

class SerialDevice(object):

    def __init__(self, baudrate = None, port = None):
        try:
            self.Serial = serial.Serial()

            #check and assign baudrate
            if baudrate is not None:    
                self.baudrate = baudrate
                self.Serial.baudrate = baudrate
            else:    
                self.baudrate = 115200
                self.Serial.baudrate = 115200

            #check and sassign port    
            if port is not None:
                self.port = port
            else:
                self.ports = list(serial.tools.list_ports.comports())
                self.port = self.ports[0].device
                self.Serial.port = self.ports[0].device

            # set timeout and open serial settings
            self.Serial.timeout = 10
            self.Serial.open()
        except serial.SerialException:  # for some reason 'no backend available error can arise.
            print(serial.SerialException)

    def isAvailabale(self):
        try:
            if self.Serial.isOpen(): #Opens SerialPort
                return True
            return False    
        except serial.SerialException:  # for some reason 'no backend available error can arise.
            return False

    def read_serial_data(self):
        data = []
        max_time = 60
        start_time = time.time()

        while (time.time() - start_time) < max_time:
            line_data = self.Serial.readline()
            print(line_data)
            data.append(line_data)
        return data

    def write(self, message = None):
        if self.Serial.is_open and message is not None:
            self.Serial.write(message)

if __name__ == '__main__':
    port = None
    baudrate = None
    device = SerialDevice(baudrate, port)
    if device.isAvailabale():
        device.read_serial_data()