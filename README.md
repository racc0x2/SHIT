# SHIT - Simple Hack for Incremental Tracking
Quite literally the simpliest incremental build system you could ever ask for. Open up `output_template` and use `{}` as a substitute for the build number, supplied as a literal. Invoke like as `python SHIT.py` or `python SHIT.py <path/to/output.h>`
To integrate with CMake, add the following lines below your target:
```
# // SHIT INTEGRATION \\
option(USE_SHIT "Enabled SHIT, the Simple Hack for Incremental Tracking. Keeps a tally of the current build number. Requires Python3" ON)

if (USE_SHIT)
    find_package(Python3 COMPONENTS Interpreter REQUIRED)

    set(SHIT_OUTPUT "${CMAKE_BINARY_DIR}/YOUR_OUTPUT_NAME.h")
    set(SHIT_PATH "${CMAKE_SOURCE_DIR}/SHIT")

    add_custom_command(
            OUTPUT ${SHIT_OUTPUT}
            COMMAND ${Python3_EXECUTABLE} ${SHIT_PATH}/SHIT.py > ${SHIT_OUTPUT}
            DEPENDS
                ${SHIT_PATH}/SHIT.py
                ${SHIT_PATH}/build_number
                ${SHIT_PATH}/output_template
            WORKING_DIRECTORY ${SHIT_PATH}
            VERBATIM
    )

    add_custom_target(SHIT_Generator ALL DEPENDS ${SHIT_OUTPUT})

    add_dependencies(YOUR_TARGET_HERE SHIT_Generator)
    target_include_directories(YOUR_TARGET_HERE PRIVATE ${CMAKE_BINARY_DIR})
endif()
# \\ SHIT INTEGRATION //
```

if, for whatever reason, you'd like to disable `SHIT` without removing the dependancy, simply pass `-DUSE_SHIT=OFF` to your CMake command line and ensure that `CMakeCache.txt` is deleted/reloaded.

## Notes
* `SHIT` works very well as a git submodule
* `SHIT` *can* be used to automate [semantic versioning](https://semver.org/) (see below), but it isn't a true "semantic versioning" implementation. Breaking changes could be registered as a patch from one build to the next, so always manually track your API compatability.
* `SHIT` is dumb. treat it as such.
* Yes, Python is a bad choice for this project. I don't care. I needed it to work cross-platform and the vast majority of developers have a Python instance available.
* Yes, the code has zero error handling. `SHIT` is a predictable "set-it-and-forget-it" program, and is meant to be configured once per workspace.
  
```cpp
int patch = a % 10;
int minor = (a / 10) % 10;
int major = a / 100;
```
