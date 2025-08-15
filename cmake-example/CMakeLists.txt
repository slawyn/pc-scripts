
set(CMAKE_SYSTEM_NAME Generic)
cmake_minimum_required(VERSION 3.5)

project("Debug Project")
enable_language(C ASM)

set(BASE "C:/Program Files (x86)/ST/STM32CubeIDE_1.10.1/STM32CubeIDE/plugins/com.st.stm32cube.ide.mcu.externaltools.gnu-tools-for-stm32.10.3-2021.10.win32_1.0.0.202111181127/tools/bin")
set(CMAKE_C_COMPILER "${BASE}/arm-none-eabi-gcc.exe")
set(CMAKE_CXX_COMPILER "${BASE}/arm-none-eabi-gcc.exe")
set(CMAKE_ASM_COMPILER  "${BASE}/arm-none-eabi-gcc.exe")
set(OBJ_DUMPER "${BASE}/arm-none-eabi-objdump.exe")
set(OBJ_COPY "${BASE}/arm-none-eabi-objcopy.exe")
include(CMakePrintHelpers)

set(EXECUTABLE Debug)
add_executable(${EXECUTABLE})
set(CMAKE_EXECUTABLE_SUFFIX ".elf")

cmake_policy(SET CMP0076 NEW)
add_subdirectory(Src)
add_subdirectory(Drivers)
add_subdirectory(CMSIS)
add_subdirectory(System)
add_subdirectory(Startup)


target_link_libraries(${EXECUTABLE}
    PRIVATE
        System
        CMSIS
        Drivers
        Src
        Startup
)

target_compile_options(${EXECUTABLE}
    PRIVATE
        -mcpu=cortex-m4
        -std=gnu11
        -g3
        -DDEBUG
        -DSTM32
        -DSTM32F4
        -DSTM32F446RETx
        -DSTM32F446xx
        -DUSE_STDPERIPH_DRIVER
        --specs=nano.specs
        -mfpu=fpv4-sp-d16
        -mfloat-abi=hard
        -mthumb
        -Og
        -ffunction-sections
        -fdata-sections
        -Wall
        -fstack-usage
        -MMD
        -MP
        $<$<COMPILE_LANGUAGE:ASM>: -c -x assembler-with-cpp>

)

target_link_options(${EXECUTABLE}
    PRIVATE
        -mcpu=cortex-m4
        --specs=nosys.specs
        -Wl,--gc-sections
        -static
        --specs=nano.specs
        -mfpu=fpv4-sp-d16
        -mfloat-abi=hard
        -mthumb -Wl,--start-group
        -T${CMAKE_SOURCE_DIR}/STM32F446RETX_FLASH.ld
        -lc
        -lm
        -Wl,--end-group
)


add_custom_command(
    TARGET ${EXECUTABLE} POST_BUILD
    COMMAND ${OBJ_COPY}  -O binary  ${CMAKE_SOURCE_DIR}/build/CMakeFiles/${EXECUTABLE}.dir/Src/inject.s.obj dumped.inject.bin
    COMMAND ${OBJ_DUMPER} -d ${CMAKE_SOURCE_DIR}/build/CMakeFiles/${EXECUTABLE}.dir/Src/inject.s.obj > dumped.inject.s
    COMMAND ${OBJ_DUMPER} -d ${CMAKE_SOURCE_DIR}/build/CMakeFiles/${EXECUTABLE}.dir/Src/main.c.obj > dumped.main.s
    COMMAND ${OBJ_DUMPER} -d ${CMAKE_SOURCE_DIR}/build/CMakeFiles/${EXECUTABLE}.dir/Drivers/stm32f4xx_usart.c.obj > dumped.stm32f4xx_usart.s
    COMMAND ${OBJ_DUMPER} -d ${CMAKE_SOURCE_DIR}/build/${EXECUTABLE}${CMAKE_EXECUTABLE_SUFFIX} > dumped.${EXECUTABLE}${CMAKE_EXECUTABLE_SUFFIX}.s
)
