import serial
import time

PORT = "COM8"   # change this to "/dev/ttyUSB0" in RPi
BAUD = 9600
PARITY = serial.PARITY_EVEN
STOPBITS = serial.STOPBITS_ONE
BYTESIZE = serial.SEVENBITS


def hexstr(b: bytes) -> str:
    return " ".join(f"{x:02X}" for x in b)


def simpleMssgPassing():
    ser = serial.Serial(
        PORT, BAUD,
        bytesize=serial.EIGHTBITS,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        timeout=0.2
    )

    print(f"Sending on {PORT} @ {BAUD}")

    for i in range(15):
        msg = f"[RPi] Hello over RS485 #{i}\r\n".encode("ascii")
        ser.write(msg)
        print(msg.decode("utf-8", errors="replace"), end="")
        ser.flush()
        time.sleep(0.5)

    ser.close()
    print("Done.")


if __name__ == "__main__":

    simpleMssgPassing()
