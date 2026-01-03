# Code for AoC 2025 day 12
# Created: 2025-12-28, by Joseph Hall


def part_1(parcel_shapes, areas):
    # Parse the parcels to a format that actually works,
    parcel_dict = {}
    # I've heard this can be solved fairly naively, so making another dictionar to hold the
    #   areas (number of #s) for each parcel
    parcel_sizes = {}

    for row in parcel_shapes:
        if row == "\n":
            continue
        elif ":" in row:
            shape_ind = int(row[0])
            parcel_dict[shape_ind] = []
            parcel_sizes[shape_ind] = 0
        else:
            parcel_dict[shape_ind].append(list(row[:-1]))
            parcel_sizes[shape_ind] += row.count("#")
    print(parcel_dict)
    print(parcel_sizes)

    # Now iterate over areas
    fittable_areas = 0
    for area in areas:
        # Split areas to get dimensions and number of parcels needed
        area_split = area.split(":")

        # Get allowed area
        dims = [int(x) for x in area_split[0].split("x")]
        allow_area = dims[0] * dims[1]

        # Get the number of parcels needed and how much area they occupy
        number_parcels = [int(x) for x in area_split[1].strip().split(" ")]
        occupy_area = 0
        for pind, parcel_count in enumerate(number_parcels):
            occupy_area += parcel_count * parcel_sizes[pind]

        fittable_areas += (occupy_area <= allow_area)

    print("Part 1 soln:", fittable_areas)

    return


def part_2(input_data):
    return


def main(input_path="2025/day-12/input.txt"):
    # Parse the imput data
    with open(input_path, "r") as f:
        input_data = f.readlines()

    # Screw it, hardcoding the split between parcels and areas
    parcel_shapes = input_data[:30]
    areas = input_data[30:]
    
    part_1(parcel_shapes, areas)
    
    return


if __name__ == "__main__":
    main()