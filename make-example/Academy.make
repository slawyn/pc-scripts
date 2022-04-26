# Usage:
# make        # compile all binary
# make clean  # remove ALL binaries and objects
# NB! Do not put spaces after commas
.PHONY = build clean
uniq = $(if $1,$(firstword $1) $(call uniq,$(filter-out $(firstword $1),$1)))
rwildcard=$(wildcard $1$2) $(foreach d,$(wildcard $1*),$(call rwildcard,$d/,$2))


# Tools
TOOL_MKDIR = mkdir -p
TOOL_CC = gcc                        # compiler to use
TOOL_LD = ld
TOOL_CP = cp

# Unique Files and directories
SOURCES := $(call rwildcard,Src/,*.c)
DIR_INCLUDES := "Inc/"

# Outputs
DIR_BUILD = Build/
DIR_LIBS = Libs/
DEPS=
EXE = $(DIR_BUILD)dina-academy.exe
OBJECTS := $(SOURCES:%.c=%.o)
DIRS_OBJECTS :=  $(addprefix $(DIR_BUILD), $(call uniq, $(sort $(dir $(SOURCES)))))

# Compiler flags
CFLAGS := -I$(DIR_INCLUDES)
LINKERFLAG = -lm


# Clean Objects
clean:
			@echo "-- Cleaning up --"
			rm -rvf $(DIR_BUILD)*

# Final outputs
build: $(DIRS_OBJECTS) $(EXE)



# Create directoreies, copy libs into Build folder etc.
$(DIRS_OBJECTS):
			@echo "-- Creating Directories --"
	 		${TOOL_MKDIR} $(DIRS_OBJECTS)
			$(TOOL_CP) $(DIR_LIBS)* $(DIR_BUILD)

# Generate an Object
%.o: %.c
			@echo "-- Creating Object $< --"
			$(TOOL_CC) $(CFLAGS) -c $< -o $(DIR_BUILD)$@

# Create .ex
$(EXE): $(OBJECTS)
			@echo "-- Creating Exe $(EXE) --"
			${TOOL_CC} ${LINKERFLAG}  -o $@ $(addprefix $(DIR_BUILD),$(OBJECTS))
