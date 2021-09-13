# Itaw
Itaw is an Instrument Trace Acquisition Widget for interactive acquisition, displaying and saving arrays of xy data. It is the main part of `itatools` package in the repository.

## Basic usage

Before starting the widget, one needs to have a function that acquires data traces and returns them as objects with the arrays of x and y values accessible under 'x' and 'y' subscripts. For illustration, we can define a dummy function that satisfies these criteria:

```python
def generate_trace(dx=0):
    """Generates parabolas offset along x by dx."""
    xarr = range(-10, 10)
    yarr = [(x+dx)**2 for x in xarr]
    return {'x': xarr, 'y': yarr} 
```
One can create a GUI for interactive acquisition and handling of data from `generate_trace` as:

```python
from itatools import itaw

win = itaw(generate_trace)
```
The widget has a way to supply arguments to the trace acquisition function (which must be supplied if the function does not define default values).

Below is another example in which a method of a spectrum analyzer control class is used to acquire traces:

```python
from rohdeschwarzfpc import FPC
from itatools import itaw

# Creates an object that communicates with an FPC spectrum analyzer.
sa = FPC(address='TCPIP0::172.16.10.10::inst0::INSTR')

# Creates an interactive widget using get_trace as a trace acquisition function.
win = itaw(sa.get_trace)
```

## Installation
`itatools` containing `itaw` is a regular Python package that can be installed e.g. via `pip install`. 

## Requirements
* PyQt5
* Matplotlib

