import EJScreenTool
import sys

def main(usa_st, input_table, output_data_csv, output_lookup, to_gdb, source_geom, output_fc, schema):

    if usa_st == 1:
        EJScreenTool.ejscreen_cal(input_table, output_data_csv, output_lookup, to_gdb, source_geom, output_fc, schema, output_csv_path_state)
    if usa_st == 2:
        EJScreenTool.ejscreenState_cal(input_table, output_data_csv, output_lookup, to_gdb, source_geom, output_fc, schema)

    print("Complete")

if __name__ == '__main__':

#*************************************************************************************************************************************    
    
    #set `option` to 1 to generate national percentiles.
    #set `option` to 2 to generate state percentiles
    level = 1

    #path to input csv dataset
    input_csv_path = "data/EJSCREEN_2024_Ozone.csv"

    #path to output csv dataset
    output_csv_path = "data/EJSCREEN_2024_USA_NewPctiles.csv"

    #path to output lookuptable excel file
    lookuptable_xlsx_path = "data/lookup_USA_NewPctiles.xlsx"

    #whether or not you wish to join the output to geometry and export to ESRI Feature Class
    output_to_featureclass = True

    #path to geometry which the output table will be joined
    geometry_featureclass_path = "data/BlockGroups.gdb/BG"

    #path to output ESRI Feature Class
    output_featureclass_path = "data/BlockGroups.gdb/EJSCREEN_2024_USA_NewPctiles"

    #path to ESRI schema csv file 
    schema_csv_path = "ejscreen_schema_usa.csv"

    output_csv_path_state = "data/EJSCREEN_2024_State_NewPctiles.csv"

#*************************************************************************************************************************************    
    if level != 1 and level != 2:
        sys.exit("`level` must have a value of either 1 or 2")
    
    if output_to_featureclass == True:
        if not geometry_featureclass_path or not output_featureclass_path or not schema_csv_path:
            sys.exit("If outputing to featureclass, all parameters must have a value")
    
    main(level, 
    input_csv_path, 
    output_csv_path, 
    lookuptable_xlsx_path, 
    output_to_featureclass, 
    geometry_featureclass_path, 
    output_featureclass_path, 
    schema_csv_path)

