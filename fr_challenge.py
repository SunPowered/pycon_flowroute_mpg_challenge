""" A simple code challenge from Flowroute.

Instructions:

Each line of the input file describes the purchase of one full tank of gas.

• Any one of the first 3 fields may be specified as ‘?’, in which case your program must reconstruct
    it from the remaining data.

Each line follows this format:

• There may be leading whitespace (spaces and tabs) before the first field. Ignore this.

• The rest of the line contains five fields separated by whitespace. Ignore any whitespace at the end of the
    line as well.

• The first field contains the total cost of the fillup in dollars.

• The second field is the quantity in gallons.

• The third field contains the price per gallon in dollars with three digits after the decimal.

• The fourth field is the number of miles traveled since the last fillup.

• The fifth field is the date. Don’t worry about the format of this field, just save it for use in the output
     report.


Output:


• Begin your program’s output with a header formatted as follows:

 Total                                 Miles/
  cost    Gallons    Price    Miles    gallon    Date
------    -------    -----    -----    ------    ----

• After the header, output your record reconstruction formatted to fit within the header fields, with a
summary at the end showing the total cost for the fuel, mean fuel price per gallon, and mean MPG.
"""
import os
import logging

# Set up logging
logger = logging.getLogger()
hdlr = logging.StreamHandler()
logger.addHandler(hdlr)
logger.setLevel(logging.INFO)


data_file = '51973064'
output_file = 'output.txt'

data_fields = [{'name': 'cost', 'type': float, 'width': 6},
               {'name': 'volume', 'type': float, 'width': 7},
               {'name': 'price', 'type': float, 'width': 5},
               {'name': 'distance', 'type': int, 'width': 5},
               {'name': 'date', 'type': str, 'width': None}]

column_spacing = 4
unknown_value_char = '?'
mpg_width = 6
mpg_fmt = "{:.3f}"
currency_fmt = "{:3,.2f}"


def compute_cost(data):
    volume, price = data[1:3]
    return volume * price


def compute_volume(data):
    cost = data[0]
    price = data[2]
    return cost / price


def compute_price(data):
    cost, volume = data[:2]
    return cost / volume

compute_missing = [compute_cost, compute_volume, compute_price]


def compute_mpg(data):
    """ Compute the mpg and insert into data structure """
    mpg = 1.0 * data[3] / data[1]
    data.insert(4, mpg)
    return data


def compute_statistics(data):
    """ Compute total cost, mean price, and mean MPG """
    cost, volume, price, distance, mpg, date = zip(*data)
    summary = {"total_cost": sum(cost),
               "avg_price": sum(price) / len(price),
               "avg_mpg": sum(mpg) / len(mpg)}
    return summary


def parse_line(line):
    """ parse the raw data line, convert to intended data type"""
    line.strip()
    split_line = line.split()
    assert len(split_line) == len(data_fields)

    line_data = []

    for n, line_item in enumerate(split_line):
        data_type = data_fields[n]['type']
        line_data.append(data_type(line_item))

    return line_data


def any_unknown_vals(data):
    """ Check for an unknown value, return the unknown index if found, otherwise return None """
    for n, item in enumerate(data):
        if item == unknown_value_char:
            return n
    return


def write_header(f):
    """ Write the file header """
    f.write(" Total                                 Miles/" + os.linesep)
    f.write("  cost    Gallons    Price    Miles    gallon    Date" + os.linesep)
    f.write("------    -------    -----    -----    ------    ----" + os.linesep)


def write_summary(f, summary):
    """ Write the summary data to the file """
    f.write(os.linesep + "Summary" + os.linesep + "-" * 10 + os.linesep)
    f.write("Total Cost: ${}".format(summary['total_cost']) + os.linesep)
    f.write("Mean Fuel Price [/gal]: ${:.2f}".format(summary["avg_price"]) + os.linesep)
    f.write("Mean MPG: {:.3f}".format(summary["avg_mpg"]) + os.linesep)


def render_item(item, width):
    """ Render the item to a given width. """

    ws = width - len(item)
    return " " * ws + item + " " * column_spacing


def render_line(line_data):
    """ Render the line for printing """
    line_str = ""
    for n, item in enumerate(line_data):
        if n == 0:
            # Cost
            item = currency_fmt.format(item)
            item_str = render_item(item, data_fields[n]['width'])
        elif n == 4:
            # MPG data
            item = mpg_fmt.format(item)
            item_str = render_item(item, mpg_width)
        elif n == 5:
            # Date
            item_str = str(item)
        else:
            item = str(item)
            item_str = render_item(item, data_fields[n]['width'])
        line_str += item_str
    line_str += os.linesep
    return line_str


def main():
    # Read the data
    logger.info("Flowroute MPG Challenge")
    logger.info("-" * 25)
    logger.info("Reading data file")
    with open(data_file, 'r') as f:
        all_data = []

        for line in f:
            line_data = parse_line(line)

            # Check for empty values
            unknown_field = any_unknown_vals(line_data)
            if unknown_field is not None:
                line_data = compute_missing[unknown_field](line_data)

            line_data = compute_mpg(line_data)

            all_data.append(line_data)

    logger.debug(all_data[:3])
    # compute summary
    logger.info("Computing Statistics")
    data_statistics = compute_statistics(all_data)

    # Write output
    with open(output_file, 'w') as f:
        logger.info("Writing output to {}".format(output_file))
        write_header(f)
        for line in all_data:
            f.write(render_line(line))
        write_summary(f, data_statistics)
    logger.info("Finished!")

if __name__ == '__main__':

    main()
