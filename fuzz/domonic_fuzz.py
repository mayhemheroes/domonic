#!/usr/local/bin/python3
import atheris
import sys
import io
import os

with atheris.instrument_imports():
    from domonic import domonic

@atheris.instrument_func
def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)
    in_string = fdp.ConsumeUnicode(len(data))
    domonic.parseString(in_string)
        
        
atheris.Setup(sys.argv, TestOneInput)
# atheris.instrument_all()
atheris.Fuzz()