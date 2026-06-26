@echo off
setlocal enabledelayedexpansion

:: Configuration
set OPENOCD="C:\Program Files (x86)\ST\STM32CubeIDE_1.10.1\STM32CubeIDE\plugins\com.st.stm32cube.ide.mcu.externaltools.openocd.win32_2.2.100.202206011703\tools\bin\openocd.exe"

set CMD_ARGS=
set DO_FLASH=0
set DO_SWO=0

:: Parse arguments
:loop
if "%~1"=="" goto end_loop
if "%~1"=="--flash" (
    set DO_FLASH=1
    set CMD_ARGS=!CMD_ARGS! "-f" "Flash.cfg" -c "program build/Debug.elf verify reset exit"
)
if "%~1"=="--debug" (
    set DO_SWO=1
    :: Add SWO configuration commands
    set CMD_ARGS=!CMD_ARGS! "-f" "Debug.cfg"
)
shift
goto loop
:end_loop

:: Run OpenOCD
%OPENOCD% ^
  %CMD_ARGS% ^
  -s "D:/projects/git/pc-scripts/cmake-example" ^
  -s "C:/Program Files (x86)/ST/STM32CubeIDE_1.10.1/STM32CubeIDE/plugins/com.st.stm32cube.ide.mcu.debug.openocd_2.0.300.202206090745/resources/openocd/st_scripts" ^
  -s "C:/Program Files (x86)/ST/STM32CubeIDE_1.10.1/STM32CubeIDE/plugins/com.st.stm32cube.ide.mpu.debug.openocd_2.0.300.202206090731/resources/openocd/st_scripts" ^
  -c "gdb_report_data_abort enable" ^
  -c "gdb_port 3333" ^
  -c "tcl_port 6666" ^
  -c "set USE_SWO 1" ^
  -c "tpiu config internal :3344 uart off 16000000 115200" ^
  -c "telnet_port 4444"