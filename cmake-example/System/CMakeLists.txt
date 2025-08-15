add_library(System INTERFACE)
target_include_directories(System
    INTERFACE
        ${CMAKE_CURRENT_SOURCE_DIR}
)


target_sources(System
    INTERFACE
        stm32f4xx_conf.h
        stm32f4xx.h
        system_stm32f4xx.c
        system_stm32f4xx.h
)