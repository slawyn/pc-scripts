add_library(Src INTERFACE)
target_include_directories(Src
    INTERFACE
        ${CMAKE_CURRENT_SOURCE_DIR}
)


target_sources(Src
    INTERFACE
        main.c
        syscalls.c
        sysmem.c
        inject.s
)

