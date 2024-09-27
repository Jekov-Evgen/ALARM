#include "pch.h"
#include "Time.h"
#include <ctime>


extern "C" __declspec(dllexport) const char* GetTime() {
    time_t seconds = time(NULL);
    tm timeinfo;
    localtime_s(&timeinfo, &seconds);

    char buffer[26];
    asctime_s(buffer, sizeof(buffer), &timeinfo);

    return _strdup(buffer);
}