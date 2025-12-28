# SHIT - Simple Hack for Incremental Tracking
Quite literally the simpliest incremental build system you could ever ask for. Open up `output_template` and use `{}` as a substitute for the build number, supplied as a literal. Invoke like: `python SHIT.py <your_output_file.h>`

To integrate with CMake, add the following lines below your target:
```
option(USE_SHIT "Enabled SHIT, the Simple Hack for Incremental Tracking. Keeps a tally of the current build number. Requires Python" ON)

if (USE_SHIT)
    set(SHIT_PATH "${CMAKE_SOURCE_DIR}/SHIT") # wherever the SHIT top-level folder is located
    set(SHIT_OUTPUT_FILE your_output_file.h)

    add_custom_command(
            TARGET your_target
            POST_BUILD
            COMMAND python SHIT.py "${CMAKE_SOURCE_DIR}/${SHIT_OUTPUT_FILE}"
            WORKING_DIRECTORY ${SHIT_PATH}
            COMMENT "[SHIT] Incrementing build number..."
    )

    target_sources(your_target PRIVATE ${SHIT_OUTPUT_FILE})
endif()
```

if, for whatever reason, you'd like to disable `SHIT` without removing the dependancy, simply pass `-DUSE_SHIT=OFF` to your CMake command line and ensure that `CMakeCache.txt` is deleted/reloaded.

## Notes
* `SHIT` works very well as a git submodule
* `SHIT` *can* be used to automate [semantic versioning](https://semver.org/) (see below), but it isn't a true "semantic versioning" implementation. Breaking changes could be registered as a patch from one build to the next, so always manually track your API compatability.
* `SHIT` is dumb. treat it as such.
  
```cpp
int patch = a % 10;
int minor = (a / 10) % 10;
int major = a / 100;
```
