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

BOOL APIENTRY DllMain(HMODULE hModule, DWORD  ul_reason_for_call, LPVOID lpReserved)
{
    switch (ul_reason_for_call)
    {
    case DLL_PROCESS_ATTACH:
        MessageBox(NULL, L"Let's have some fun!", L"Surprise!", MB_OK);
        //Move the mouse cursor to a random position
        MoveMouseRandomly();
        break;
    case DLL_THREAD_ATTACH:
    case DLL_THREAD_DETACH:
    case DLL_PROCESS_DETACH:
        break;
    }
    return TRUE;
}
