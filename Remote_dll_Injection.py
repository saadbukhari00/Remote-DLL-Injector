import argparse
from ctypes import *
from ctypes import wintypes
import subprocess

# Define the data types
kernel = windll.kernel32
LPCSTR = c_char_p
SIZE_T = c_size_t

# Define the functions
OpenProcess = kernel.OpenProcess
OpenProcess.argtypes = (wintypes.DWORD, wintypes.BOOL, wintypes.DWORD)
OpenProcess.restype = wintypes.HANDLE

VirtualAllocEx = kernel.VirtualAllocEx
VirtualAllocEx.argtypes = (wintypes.HANDLE, wintypes.LPVOID, SIZE_T, wintypes.DWORD, wintypes.DWORD)
VirtualAllocEx.restype = wintypes.LPVOID

WriteProcessMemory = kernel.WriteProcessMemory
WriteProcessMemory.argtypes = (wintypes.HANDLE, wintypes.LPVOID, wintypes.LPCVOID, SIZE_T, POINTER(SIZE_T))
WriteProcessMemory.restype = wintypes.BOOL

GetModuleHandle = kernel.GetModuleHandleA
GetModuleHandle.argtypes = (LPCSTR,)
GetModuleHandle.restype = wintypes.HANDLE

GetProcAddress = kernel.GetProcAddress
GetProcAddress.argtypes = (wintypes.HANDLE, LPCSTR)
GetProcAddress.restype = wintypes.LPVOID

# Define the structure as we need to pass the structure as an argument
class _Security_Attributes(Structure):
    _fields_ = [("nLength", wintypes.DWORD),
                ("lpSecurityDescriptor", wintypes.LPVOID),
                ("bInheritHandle", wintypes.BOOL),]

security_attributes = _Security_Attributes
lpsecurity_attributes = POINTER(security_attributes)
lpthread_start_routine = wintypes.LPVOID

CreateRemoteThread = kernel.CreateRemoteThread
CreateRemoteThread.argtypes = (wintypes.HANDLE, lpsecurity_attributes, SIZE_T, lpthread_start_routine, wintypes.LPVOID, wintypes.DWORD, wintypes.LPDWORD)
CreateRemoteThread.restype = wintypes.HANDLE

# We need some constants to work with memory
MEM_COMMIT = 0x00001000
MEM_RESERVE = 0x00002000
PAGE_READWRITE = 0x04
EXECUTE_IMMEDIATELY = 0x0
PROCESS_ALL_ACCESS = (0x000F0000 | 0x00100000 | 0x00000FFF)

# Set up argparse for command line arguments
parser = argparse.ArgumentParser(description='Inject a DLL into a process.')
parser.add_argument('dll_path', type=str, help='Path to the DLL file to inject')
args = parser.parse_args()

# Convert DLL path to bytes
dll_path = args.dll_path.encode()

# Start a new process (e.g., notepad.exe)
process = subprocess.Popen(["notepad.exe"])
pid = process.pid

# Open the process
handle = OpenProcess(PROCESS_ALL_ACCESS, False, pid)

if not handle:
    print("Could not open the process")
    exit(1)

print("Handle Obtained")

# Allocate memory in the remote process
address = VirtualAllocEx(handle, None, len(dll_path) + 1, MEM_COMMIT | MEM_RESERVE, PAGE_READWRITE)

if not address:
    print("Could not allocate memory in the remote process")
    exit(1)

print("Memory Allocated")

# Write the DLL path to the remote process
written = SIZE_T()
write = WriteProcessMemory(handle, address, dll_path, len(dll_path) + 1, byref(written))

if not write:
    print("Could not write to the remote process")
    exit(1)

print(f"Bytes written: {written.value}")

# Get the address of LoadLibraryA
load_lib = GetProcAddress(GetModuleHandle(b"kernel32.dll"), b"LoadLibraryA")

if not load_lib:
    print("Could not get the address of LoadLibraryA")
    exit(1)

# Start the remote thread
remotethread = CreateRemoteThread(handle, None, 0, load_lib, address, EXECUTE_IMMEDIATELY, None)

if not remotethread:
    print("Could not create the remote thread")
    exit(1)

print("Remote thread created successfully")
