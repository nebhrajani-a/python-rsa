# RSA Pure Python Implementation

This project is a pure Python 3 implementation of RSA, OS2IP, and I2OSP.
**Note that this implementation does not include OAEP at the present,
but is expected to be added.**

## Features
- Pure Python RSA Implementation.
- Uses Miller Rabin to generate primes, along with Python
  ```secrets``` module.
- **File chunking, can encrypt and decrypt files of arbitrary length**
  by breaking it into chunks and joining it back.
- Uses a Pandas DataFrame as a database backend.
- Has a CLI and user login system.
- Portable to any machine that runs Python.
- Pretty fast.

## Installation
- Clone this directory and ```cd``` to ```/src```. 
- Run ```python main.py```.

    > Your system may run Python 2 instead of 3 using the `python` command.
    > Make sure `python` runs Python 3. On some systems, you'll have to run
    > `python3` explicitly.

## Dependencies
- Only runs on Python 3.
- ```progress``` to draw progress bars.
- ```pandas``` for backend.

## Limitations
- Does not use OAEP.
- Only supports ASCII, no Unicode support.
- Does not have an explicit signing feature.
