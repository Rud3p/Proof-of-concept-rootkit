import ctypes
import logging

logging.basicConfig(level=logging.DEBUG)

# Original Windows api func
original_OpenProcess = ctypes.windll.kernel32.OpenProcess

# Hooked OpenProcess
def hooked_OpenProcess(dwDesiredAccess, bInheritHandle, dwProcessId):
    logging.debug("Called hooked OpenProcess")

    # Show message box    
    malicious_code()

    logging.debug("Calling original OpenProcess")
    
    # Verify the arguments received by the hooked function
    logging.debug(f"Received arguments: dwDesiredAccess={dwDesiredAccess}, "
                  f"bInheritHandle={bInheritHandle}, dwProcessId={dwProcessId}")

    return original_OpenProcess(dwDesiredAccess, bInheritHandle, dwProcessId)

ctypes.windll.kernel32.OpenProcess = hooked_OpenProcess

def malicious_code():
    logging.debug("Executing malicious code")
    ctypes.windll.user32.MessageBoxW(0, "Hooked!", "Title", 0)

handle = ctypes.windll.kernel32.OpenProcess(1, 0, 0)
