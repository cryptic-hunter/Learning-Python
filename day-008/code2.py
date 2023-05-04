#Area Calculation
#1 can of paint can cover 5 square meters of wall. Given a random height and width of wall, calculate how many cans of paint will be needed to be bought.
#number of cans = (wall height * wall width)/coverage per can

wall_height = int(input("Height of wall(m): "))
wall_width = int(input("Width of wall(m): "))

coverage_per_can = 5


def paint_calc(height=wall_height, width=wall_width, coverage=coverage_per_can):
    area_wall = (height * width)
    number_of_cans = area_wall/coverage_per_can
    print(f"The cans needed are: {round(number_of_cans)}")

paint_calc()