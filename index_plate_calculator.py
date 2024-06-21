from fractions import Fraction

indexing_plates = {
    'Plate 1': [15, 16, 17, 18, 19, 20],
    'Plate 2': [21, 23, 27, 29, 31, 33],
    'Plate 3': [37, 39, 41, 43, 47, 49]
}

def find_smallest_divisible_hole(denominator):
    smallest_hole = None
    smallest_plate = None
    for plate, holes in indexing_plates.items():
        for hole in holes:
            if hole % denominator == 0:
                if smallest_hole is None or hole < smallest_hole:
                    smallest_hole = hole
                    smallest_plate = plate
    return smallest_plate, smallest_hole

def calculate_turns(teeth):
    turns = 40 / teeth
    integer_part = int(turns)
    fractional_part = turns - integer_part

    # Convert the fractional part to a fraction
    fraction = Fraction(fractional_part).limit_denominator()

    # Extract the numerator and denominator
    numerator = fraction.numerator
    denominator = fraction.denominator

    smallest_plate, smallest_hole = find_smallest_divisible_hole(denominator)
    if smallest_hole:
        multiplier = smallest_hole / denominator
        numerator_new = int(numerator * multiplier)
        denominator_new = int(denominator * multiplier)
        hole_move = (integer_part * denominator_new) + numerator_new

        # If partial use of hole
        if denominator != 1:
            result = f"Use {smallest_plate} with {smallest_hole} holes\n"
            if numerator == numerator_new and integer_part == 0: # fraction (no conversion)
                result += f"The number of turns is {numerator}/{denominator}\n"
                result += f"Which translates to moving {hole_move} hole(s) per index"
            elif numerator != numerator_new and integer_part == 0: # fraction (get LCD)
                result += f"The number of turns is {numerator}/{denominator} or {numerator_new}/{denominator_new}\n"
                result += f"Which translates to moving {hole_move} hole(s) per index"
            elif numerator == numerator_new and integer_part != 0: # mixed fraction (no conversion)
                result += f"The number of turns is {integer_part} {numerator}/{denominator}\n"
                result += f"Which translates to moving {integer_part} complete revolution(s) and {numerator_new} hole(s), OR a total of {hole_move} holes per index"
            else: # mixed fraction
                result += f"The number of turns is {integer_part} {numerator}/{denominator} or {integer_part} {numerator_new}/{denominator_new}\n"
                result += f"Which translates to moving {integer_part} complete revolution(s) and {numerator_new} hole(s), OR a total of {hole_move} holes per index"
        else:
            result = "You can use any plate.\n"
            result += f"Move {integer_part} complete revolution(s) per index"
    else:
        result = "No divisible hole found"
    
    return result

if __name__ == "__main__":
    teeth = int(input("Enter the number of teeth: "))
    print(calculate_turns(teeth))