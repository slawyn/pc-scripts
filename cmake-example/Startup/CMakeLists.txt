add_library(Startup INTERFACE)
target_include_directories(Startup
    INTERFACE
        ${CMAKE_CURRENT_SOURCE_DIR}
)


target_sources(Startup
    INTERFACE
        startup_stm32f446retx.s
)


set_property(SOURCE startup_stm32f446retx.s PROPERTY LANGUAGE C)