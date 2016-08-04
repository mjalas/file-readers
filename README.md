# File readers
[![PyPI version](https://badge.fury.io/py/file-readers.svg)](https://badge.fury.io/py/file-readers)
[![Build Status](https://travis-ci.org/mjalas/file-readers.svg?branch=master)](https://travis-ci.org/mjalas/file-readers)
[![Coverage Status](https://coveralls.io/repos/github/mjalas/file-readers/badge.svg?branch=master)](https://coveralls.io/github/mjalas/file-readers?branch=master)
[![Code Health](https://landscape.io/github/mjalas/file-readers/master/landscape.svg?style=flat)](https://landscape.io/github/mjalas/file-readers/master)

File readers is a library that currently includes reader for Excel and CSV files. By default the library includes a data collector for each reader. The default data collectors might be sufficient for most basic cases. The library has been design to be extendable. Users can inherit the base data collector and write their own implementation, which can then be injected into one of the reader classes. More documentation about the libary will be added soon.


## Usage

The default Excel reader is the simplest class to start with. The only 
requirement for using the default Excel reader is to have the header row
on the first row in the Excel file, since it creates a dictionary of 
each row for easy row searching.

Currently the best way to find out how to use the reader and data 
collector classes is by looking at the tests.