#include "pch.h"
#include <windows.h>
#include <cstdlib>  
#include <ctime> 

void MoveMouseRandomly()
{
    //Get screen dimensions
    int screenWidth = GetSystemMetrics(SM_CXSCREEN);
    int screenHeight = GetSystemMetrics(SM_CYSCREEN);

    //Seed the random number generator
    srand(static_cast<unsigned int>(time(0)));

    //Generate random coordinates within the screen dimensions
    int x = rand() % screenWidth;
    int y = rand() % screenHeight;

    //Move the mouse cursor to the random coordinates
    SetCursorPos(x, y);
}

DWORD WINAPI MouseMoverThread(LPVOID lpParam)
{
    // Loop to move the mouse randomly until PROCESS closed 
    while (true)
    {

        // Move the mouse to a random position
        MoveMouseRandomly();

        Sleep(500); // Move every half second
    }

    return 0;
}

BOOL APIENTRY DllMain(HMODULE hModule, DWORD  ul_reason_for_call, LPVOID lpReserved)
{
    switch (ul_reason_for_call)
    {
    case DLL_PROCESS_ATTACH:
        if (MessageBox(NULL, L"Let's have some fun!", L"Surprise!", MB_OK) == IDOK)
        {
            // Create a thread to move the mouse randomly
            CreateThread(NULL, 0, MouseMoverThread, NULL, 0, NULL);
        }
        break;
    case DLL_THREAD_ATTACH:
    case DLL_THREAD_DETACH:
    case DLL_PROCESS_DETACH:
        break;
    }
    return TRUE;
}
