# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.10

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/devluis/Documentos/GitHub/VVC_research/VVCSoftware_VTM

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/devluis/Documentos/GitHub/VVC_research

# Include any dependencies generated for this target.
include source/Lib/Utilities/CMakeFiles/Utilities.dir/depend.make

# Include the progress variables for this target.
include source/Lib/Utilities/CMakeFiles/Utilities.dir/progress.make

# Include the compile flags for this target's objects.
include source/Lib/Utilities/CMakeFiles/Utilities.dir/flags.make

source/Lib/Utilities/CMakeFiles/Utilities.dir/VideoIOYuv.cpp.o: source/Lib/Utilities/CMakeFiles/Utilities.dir/flags.make
source/Lib/Utilities/CMakeFiles/Utilities.dir/VideoIOYuv.cpp.o: VVCSoftware_VTM/source/Lib/Utilities/VideoIOYuv.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/devluis/Documentos/GitHub/VVC_research/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object source/Lib/Utilities/CMakeFiles/Utilities.dir/VideoIOYuv.cpp.o"
	cd /home/devluis/Documentos/GitHub/VVC_research/source/Lib/Utilities && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/Utilities.dir/VideoIOYuv.cpp.o -c /home/devluis/Documentos/GitHub/VVC_research/VVCSoftware_VTM/source/Lib/Utilities/VideoIOYuv.cpp

source/Lib/Utilities/CMakeFiles/Utilities.dir/VideoIOYuv.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/Utilities.dir/VideoIOYuv.cpp.i"
	cd /home/devluis/Documentos/GitHub/VVC_research/source/Lib/Utilities && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/devluis/Documentos/GitHub/VVC_research/VVCSoftware_VTM/source/Lib/Utilities/VideoIOYuv.cpp > CMakeFiles/Utilities.dir/VideoIOYuv.cpp.i

source/Lib/Utilities/CMakeFiles/Utilities.dir/VideoIOYuv.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/Utilities.dir/VideoIOYuv.cpp.s"
	cd /home/devluis/Documentos/GitHub/VVC_research/source/Lib/Utilities && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/devluis/Documentos/GitHub/VVC_research/VVCSoftware_VTM/source/Lib/Utilities/VideoIOYuv.cpp -o CMakeFiles/Utilities.dir/VideoIOYuv.cpp.s

source/Lib/Utilities/CMakeFiles/Utilities.dir/VideoIOYuv.cpp.o.requires:

.PHONY : source/Lib/Utilities/CMakeFiles/Utilities.dir/VideoIOYuv.cpp.o.requires

source/Lib/Utilities/CMakeFiles/Utilities.dir/VideoIOYuv.cpp.o.provides: source/Lib/Utilities/CMakeFiles/Utilities.dir/VideoIOYuv.cpp.o.requires
	$(MAKE) -f source/Lib/Utilities/CMakeFiles/Utilities.dir/build.make source/Lib/Utilities/CMakeFiles/Utilities.dir/VideoIOYuv.cpp.o.provides.build
.PHONY : source/Lib/Utilities/CMakeFiles/Utilities.dir/VideoIOYuv.cpp.o.provides

source/Lib/Utilities/CMakeFiles/Utilities.dir/VideoIOYuv.cpp.o.provides.build: source/Lib/Utilities/CMakeFiles/Utilities.dir/VideoIOYuv.cpp.o


source/Lib/Utilities/CMakeFiles/Utilities.dir/program_options_lite.cpp.o: source/Lib/Utilities/CMakeFiles/Utilities.dir/flags.make
source/Lib/Utilities/CMakeFiles/Utilities.dir/program_options_lite.cpp.o: VVCSoftware_VTM/source/Lib/Utilities/program_options_lite.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/devluis/Documentos/GitHub/VVC_research/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object source/Lib/Utilities/CMakeFiles/Utilities.dir/program_options_lite.cpp.o"
	cd /home/devluis/Documentos/GitHub/VVC_research/source/Lib/Utilities && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/Utilities.dir/program_options_lite.cpp.o -c /home/devluis/Documentos/GitHub/VVC_research/VVCSoftware_VTM/source/Lib/Utilities/program_options_lite.cpp

source/Lib/Utilities/CMakeFiles/Utilities.dir/program_options_lite.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/Utilities.dir/program_options_lite.cpp.i"
	cd /home/devluis/Documentos/GitHub/VVC_research/source/Lib/Utilities && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/devluis/Documentos/GitHub/VVC_research/VVCSoftware_VTM/source/Lib/Utilities/program_options_lite.cpp > CMakeFiles/Utilities.dir/program_options_lite.cpp.i

source/Lib/Utilities/CMakeFiles/Utilities.dir/program_options_lite.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/Utilities.dir/program_options_lite.cpp.s"
	cd /home/devluis/Documentos/GitHub/VVC_research/source/Lib/Utilities && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/devluis/Documentos/GitHub/VVC_research/VVCSoftware_VTM/source/Lib/Utilities/program_options_lite.cpp -o CMakeFiles/Utilities.dir/program_options_lite.cpp.s

source/Lib/Utilities/CMakeFiles/Utilities.dir/program_options_lite.cpp.o.requires:

.PHONY : source/Lib/Utilities/CMakeFiles/Utilities.dir/program_options_lite.cpp.o.requires

source/Lib/Utilities/CMakeFiles/Utilities.dir/program_options_lite.cpp.o.provides: source/Lib/Utilities/CMakeFiles/Utilities.dir/program_options_lite.cpp.o.requires
	$(MAKE) -f source/Lib/Utilities/CMakeFiles/Utilities.dir/build.make source/Lib/Utilities/CMakeFiles/Utilities.dir/program_options_lite.cpp.o.provides.build
.PHONY : source/Lib/Utilities/CMakeFiles/Utilities.dir/program_options_lite.cpp.o.provides

source/Lib/Utilities/CMakeFiles/Utilities.dir/program_options_lite.cpp.o.provides.build: source/Lib/Utilities/CMakeFiles/Utilities.dir/program_options_lite.cpp.o


# Object files for target Utilities
Utilities_OBJECTS = \
"CMakeFiles/Utilities.dir/VideoIOYuv.cpp.o" \
"CMakeFiles/Utilities.dir/program_options_lite.cpp.o"

# External object files for target Utilities
Utilities_EXTERNAL_OBJECTS =

VVCSoftware_VTM/lib/umake/gcc-7.5/x86_64/release/libUtilities.a: source/Lib/Utilities/CMakeFiles/Utilities.dir/VideoIOYuv.cpp.o
VVCSoftware_VTM/lib/umake/gcc-7.5/x86_64/release/libUtilities.a: source/Lib/Utilities/CMakeFiles/Utilities.dir/program_options_lite.cpp.o
VVCSoftware_VTM/lib/umake/gcc-7.5/x86_64/release/libUtilities.a: source/Lib/Utilities/CMakeFiles/Utilities.dir/build.make
VVCSoftware_VTM/lib/umake/gcc-7.5/x86_64/release/libUtilities.a: source/Lib/Utilities/CMakeFiles/Utilities.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/devluis/Documentos/GitHub/VVC_research/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Linking CXX static library ../../../VVCSoftware_VTM/lib/umake/gcc-7.5/x86_64/release/libUtilities.a"
	cd /home/devluis/Documentos/GitHub/VVC_research/source/Lib/Utilities && $(CMAKE_COMMAND) -P CMakeFiles/Utilities.dir/cmake_clean_target.cmake
	cd /home/devluis/Documentos/GitHub/VVC_research/source/Lib/Utilities && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/Utilities.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
source/Lib/Utilities/CMakeFiles/Utilities.dir/build: VVCSoftware_VTM/lib/umake/gcc-7.5/x86_64/release/libUtilities.a

.PHONY : source/Lib/Utilities/CMakeFiles/Utilities.dir/build

source/Lib/Utilities/CMakeFiles/Utilities.dir/requires: source/Lib/Utilities/CMakeFiles/Utilities.dir/VideoIOYuv.cpp.o.requires
source/Lib/Utilities/CMakeFiles/Utilities.dir/requires: source/Lib/Utilities/CMakeFiles/Utilities.dir/program_options_lite.cpp.o.requires

.PHONY : source/Lib/Utilities/CMakeFiles/Utilities.dir/requires

source/Lib/Utilities/CMakeFiles/Utilities.dir/clean:
	cd /home/devluis/Documentos/GitHub/VVC_research/source/Lib/Utilities && $(CMAKE_COMMAND) -P CMakeFiles/Utilities.dir/cmake_clean.cmake
.PHONY : source/Lib/Utilities/CMakeFiles/Utilities.dir/clean

source/Lib/Utilities/CMakeFiles/Utilities.dir/depend:
	cd /home/devluis/Documentos/GitHub/VVC_research && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/devluis/Documentos/GitHub/VVC_research/VVCSoftware_VTM /home/devluis/Documentos/GitHub/VVC_research/VVCSoftware_VTM/source/Lib/Utilities /home/devluis/Documentos/GitHub/VVC_research /home/devluis/Documentos/GitHub/VVC_research/source/Lib/Utilities /home/devluis/Documentos/GitHub/VVC_research/source/Lib/Utilities/CMakeFiles/Utilities.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : source/Lib/Utilities/CMakeFiles/Utilities.dir/depend

