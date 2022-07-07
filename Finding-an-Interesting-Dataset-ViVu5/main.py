import pandas

pandas.options.display.max_columns = None
pandas.options.display.max_rows = None

water_potability_data = pandas.read_csv("water_potability.csv")

print(water_potability_data)