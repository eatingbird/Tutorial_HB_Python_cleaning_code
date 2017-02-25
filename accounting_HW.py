def calc_sales_by_type(orders_by_type):
    """calculates and prints the sales by mellon type"""

    file = open(orders_by_type)

    melon_tallies = {"Musk":0, 
                    "Hybrid":0, 
                    "Watermelon":0,
                    "Winter": 0}

    for line in file: # add up sales amount by type
        data = line.rstrip().split("|")
        melon_type = data[1]
        melon_count = int(data[2])
        melon_tallies[melon_type] += melon_count

    melon_prices = {"Musk": 1.15,
                    "Hybrid": 1.30,
                    "Watermelon": 1.75,
                    "Winter": 4.00}

    total_revenue = 0
    for melon_type in melon_tallies: # add up sales revenue by type
        price = melon_prices[melon_type]
        revenue = price * melon_tallies[melon_type]
        total_revenue += revenue
        # print "We sold <#> <type of melons> at <individual price> each for a total of <revenue>" for each type of melon
        print "We sold {} {} melons".format(melon_tallies[melon_type], melon_type)
        print "Sales was at {:.2f} each for a total of {:.2f}".format(price, revenue)
        print ""
    file.close()

def calc_sales_by_source(sales_by_source):
    """Adds up sales by sales person and by internet"""

    file = open(sales_by_source)
    sales = {"ONLINE":0,
             "PHONE":0}

    for line in file: # add up revenue by source
        data = line.split("|")
        if data[2] == "ONLINE":
            sales["ONLINE"] += float(data[3])
        else:
            sales["PHONE"] += float(data[3])
    file.close()

    print "Salespeople generated ${:.2f} in revenue.".format(sales["PHONE"])
    print "Internet sales generated ${:.2f} in revenue.".format(sales["ONLINE"])
    print ""

    if sales["PHONE"] > sales["ONLINE"]:
        print "Guess there's some value to those salespeople after all."
    else:
        print "Time to fire the sales team! Online sales rule all!"

def print_report(sales_by_source, orders_by_type):
    """Print reports with by-type sales amount&revenue, by-source sales revenue """

    LINE_LENGTH = 80

    print "*" * LINE_LENGTH #prints separator line
    print ""
    calc_sales_by_type(orders_by_type) #prints by-type
    print "*" * LINE_LENGTH
    print ""
    calc_sales_by_source(sales_by_source) #prints by-source
    print ""
    print "*" * LINE_LENGTH

sales_by_source = "orders_with_sales.txt"
orders_by_type = "orders_by_type.txt"
print_report(sales_by_source, orders_by_type)

