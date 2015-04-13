# PyCon2015 Flowroute MPG Challenge

Fun little coding challenge from Flowroute from PyCon2015

## Instructions:

Each line of the input file describes the purchase of one full tank of gas.

* Any one of the first 3 fields may be specified as ‘?’, in which case your program must reconstruct it from the remaining data.

Each line follows this format:

* There may be leading whitespace (spaces and tabs) before the first field. Ignore this.

* *The rest of the line contains five fields separated by whitespace. Ignore any whitespace at the end of the line as well.

* The first field contains the total cost of the fillup in dollars.

* The second field is the quantity in gallons.

* The third field contains the price per gallon in dollars with three digits after the decimal.

* The fourth field is the number of miles traveled since the last fillup.

* The fifth field is the date. Don’t worry about the format of this field, just save it for use in the output report.


## Output:

* Begin your program’s output with a header formatted as follows:

 Total                                 Miles/
  cost    Gallons    Price    Miles    gallon    Date
------    -------    -----    -----    ------    ----

* After the header, output your record reconstruction formatted to fit within the header fields, with a summary at the end showing the total cost for the fuel, mean fuel price per gallon, and mean MPG.

## Running

No dependencies, just run the one file

    python fr_challenge.py

and you're good to go!
