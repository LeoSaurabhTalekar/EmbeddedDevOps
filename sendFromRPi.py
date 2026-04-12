import serial
import time
import os  # <-- Add this import

# --- Update this section ---
# Use the PORT environment variable if set, otherwise default to "COM8"
PORT = os.environ.get("SERIAL_PORT", "COM8")
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
