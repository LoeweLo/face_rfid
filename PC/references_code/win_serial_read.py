import serial
import sys
import winsound 
# Configure the serial connection
serial_port = "COM12"  # Update with your serial port (e.g., "/dev/ttyUSB0" on Linux)
baud_rate = 9600
winsound.Beep(1200, 400)  # Frequency 1000 Hz, Duration 200 ms

try:
    ser = serial.Serial(serial_port, baud_rate, timeout=1)
    print(f"Connected to {serial_port} at {baud_rate} baud.")
    i=1
    while True:
        try:
            
            # Send the input data over the serial connection
            
            data = ser.readline()  # read a line of data from the UART
            if data:
                print(i,data.decode('utf-8').strip())  # decode bytes to string and print
                winsound.Beep(1200, 400) # beep
                i+=1
        
        except KeyboardInterrupt:
            print("Exiting...")
            break

except serial.SerialException as e:
    print(f"Error: {e}")
    sys.exit(1)
finally:
    ser.close()  # ensure the serial connection is closed