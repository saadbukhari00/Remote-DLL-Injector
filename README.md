# Remote DLL Injection

This Python script demonstrates how to perform remote DLL injection into a target process using the Windows API. This technique can be used to inject a dynamic link library (DLL) into another process for various purposes, including code execution and process manipulation.

## Disclaimer

**This script is intended for educational purposes only. Unauthorized DLL injection can be illegal and unethical. Always ensure you have explicit permission before performing such actions on any system.** <br>

This Script was included in Python201 course by TCM Security. I have enchanced this a little bit and modified the dll file to make it more fun experience.

## Prerequisites

- Python 3.x
- Windows operating system

## Script Overview

The script performs the following steps:
1. Starts a new process (e.g., Notepad).
2. Opens the target process with necessary permissions.
3. Allocates memory in the target process.
4. Writes the path to the DLL into the allocated memory.
5. Retrieves the address of `LoadLibraryA` from `kernel32.dll`.
6. Creates a remote thread in the target process to load the DLL.

## How to Use

1. **Prepare Your DLL**: 
   - The provided .c file for the DLL is not included here. Compile it into a DLL yourself or create your own DLL. 
   - Modify the `dll_path` variable in the script to point to your compiled DLL.

2. **Run the Script**:
   - Ensure you have Python installed on your system.
   - Update the `dll_path` variable with the path to your DLL.
   - Run the script. It will start a new Notepad process and inject the DLL into it.

## Libraries and Concepts Used

- **ctypes**: A Python library for interfacing with C-style libraries and functions in Windows. It is used to call Windows API functions from Python.
- **subprocess**: A Python module used to spawn new processes, connect to their input/output/error pipes, and obtain their return codes. In this script, it starts a new process (e.g., Notepad) for DLL injection.

### Windows API Functions

- **OpenProcess**: Opens an existing local process object and obtains a handle to it. This handle is required for interacting with the process.
- **VirtualAllocEx**: Allocates memory within the address space of the specified process.
- **WriteProcessMemory**: Writes data to the memory of a specified process.
- **GetModuleHandleA**: Retrieves a module handle for the specified module (DLL or executable).
- **GetProcAddress**: Retrieves the address of an exported function or variable from the specified module.
- **CreateRemoteThread**: Creates a thread that runs in the virtual address space of another process.

### Concepts

- **DLL Injection**: A technique used to run code within the address space of another process. This can be used for debugging, extending application functionalities, or malicious purposes.
- **Memory Allocation**: Allocating memory within a process's address space to store data or code, such as a DLL path in this case.
- **Remote Thread Creation**: Creating a new thread in the target process to execute the injected DLL.

## Further Improvements

1. **Error Handling**: Enhance error handling to provide more detailed feedback and recovery options.
2. **Dynamic DLL Path**: Modify the script to accept the DLL path as a command-line argument for flexibility.
3. **Target Process Selection**: Implement functionality to allow users to select the target process more dynamically.
4. **Security Considerations**: Add features to ensure safe and authorized use of the injection technique.

## Contact Me

For questions or further discussions, please contact me at [syed4000saad@gmail.com](mailto:syed4000saad@gmail.com). 

Here's a README file you can use for your GitHub project:

## References

- [DLL Injection - Wikipedia](https://en.wikipedia.org/wiki/DLL_injection)
- [OpenProcess - Microsoft Docs](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-openprocess)
- [VirtualAllocEx - Microsoft Docs](https://learn.microsoft.com/en-us/windows/win32/api/memoryapi/nf-memoryapi-virtualallocex)
- [WriteProcessMemory - Microsoft Docs](https://learn.microsoft.com/en-us/windows/win32/api/memoryapi/nf-memoryapi-writeprocessmemory)
- [GetModuleHandleA - Microsoft Docs](https://learn.microsoft.com/en-us/windows/win32/api/libloaderapi/nf-libloaderapi-getmodulehandlea)
- [GetProcAddress - Microsoft Docs](https://learn.microsoft.com/en-us/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress)
- [CreateRemoteThread - Microsoft Docs](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-createremotethread)
- [Walkthrough: Creating and Using a Dynamic Link Library - Microsoft Docs](https://learn.microsoft.com/en-us/cpp/build/walkthrough-creating-and-using-a-dynamic-link-library-cpp?view=msvc-170)




