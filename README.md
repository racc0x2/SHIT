# SHIT - Simple Hack for Incremental Tracking
Quite literally the simpliest incremental build system you could ever ask for. Create a template and use `{}` as a substitute for the build number, supplied as a literal. See `python SHIT/main.py --help`
To integrate with CMake, add the following lines below your target:
```
# // SHIT INTEGRATION \\
include(/path/to/SHIT/IncludeSHIT.cmake)
SHIT_subscribe(your_target_here your_SHIT_template.in your_SHIT_output.h)
# \\ SHIT INTEGRATION //
```

## Notes
* `SHIT` works very well as a git submodule
* `SHIT` *can* be used to automate [semantic versioning](https://semver.org/) (see below), but it isn't a true "semantic versioning" implementation. Breaking changes could be registered as a patch from one build to the next, so always manually track your API compatability.
* `SHIT` is dumb. treat it as such.
* Yes, Python is a bad choice for this project. I don't care. I needed it to work cross-platform and the vast majority of developers have a Python instance available.
* Yes, the code has zero error handling. `SHIT` is a predictable "set-it-and-forget-it" program, and is meant to be configured once per workspace.
  
```cpp
auto a = ...; // build number

int patch = a % 10;
int minor = (a / 10) % 10;
int major = std::max(a / 100, 1) + 1;

printf("%i.%i.%i", major, minor, patch);
```
