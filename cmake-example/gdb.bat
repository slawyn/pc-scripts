@echo off
setlocal

set "GDB=C:\Program Files (x86)\ST\STM32CubeIDE_1.10.1\STM32CubeIDE\plugins\com.st.stm32cube.ide.mcu.externaltools.gnu-tools-for-stm32.10.3-2021.10.win32_1.0.0.202111181127\tools\bin\arm-none-eabi-gdb.exe"
set "ELF=build\Debug.elf"

"%GDB%" ^
  -q "%ELF%" ^
  -ex "set pagination off" ^
  -ex "set confirm off" ^
  -ex "target extended-remote localhost:3333" ^
  -ex "load" ^
  -ex "continue" ^
  -ex "quit"
