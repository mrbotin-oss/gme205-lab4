# Tools
- Python, VS Code, GitHub, Shapely

# Overview of the Laboratory
- Integrate the Lecture 4 in this Laboratory Exercise;
- In which we will design algorithms before coding. ;
- Delegate spatial ccomputation to Shapely correctly. ;
- Avoid "God functions" and "God classes". ;

# Output
- summary.json

# System
- What is the total area of all active parcels?
- Which parcels exceed a threshold area?
- How many parcels per zone?
- Which parccels intersect a proposed development boundary (e.g. which parcel are residential or commercial and suitable for development?)

# Algorithm
i. Start
ii. Load parcel data from JSON file
iii. Convert each record into a Parcel object
iv. if no parcels are loaded:
    • Display error message 
    • Stop program
v. Initialize:
    • total_active_area = 0 sqm
    • threshold_area = 300 sqm
    • large_parcels = empty list
    • count_per_zone = emtpy dict
    • target_zone = residential or commercial
    • other_parcel_zone = industrial 
    • intersecting_parcels = empty list
vi. Each Parcel:
    • if parcel is active = true = calculate
        new total_active_area = total_active_area + parcel_area
    • if parcel_area > threshold area = add parcel to large_parcels
    • if parcel_zone = residential 
        add to count_per_zone(residential) 
      if parcel_zone = commerial
        add to count_per_zone(commercial)
      if parcel_zone = industrial
        add to count_per_zone(industrial)
    • if target_zone intersects other_parcel_zone
        add to intersecting_parcels
vii Display:
    • Display total_active_area
    • Display count_per_zone
    • Display large_parcels
    • Display intersecting_parcels

# Pseudocode
BEGIN 
    LOAD parcel_data from JSON file 
    CONVERT parcel_data into Parcel objects 
    STORE in parcel_list

    IF parcel_list is empty THEN 
    PRINT "No parcels found." 
    STOP 
    END IF 

    SET total_active_area = 0 
    SET threshold_area =  300
    SET large_parcels = empty list 
    SET count_per_zone = empty dict 
    SET target_zone = residential or commercial 
    SET other_zone = industrial
    SET intersecting_parcels = empty list

    FOR EACH parcel IN parcel_list

    IF parcel is active = TRUE
    SET total_active_area = total_active_area + parcel_area
    END IF

    IF parcel_area > threshold area
    APPEND parcel to large_parcels
    END IF

    IF parcel_zone NOT IN count_per_zone
    SET count_per_zone(residential) = 1
    ELSE
    SET count_per_zone(commercial) = 1
    ELSE
    SET count_per_zone(industrial) = 1
    END IF

    IF target_zone intersects other_zone
    APPEND parcel to intersecting_parcels
    END IF

    END FOR
    DISPLAY total_active_area
    DISPLAY count_per_zone
    DISPLAY large_parcels
    DISPLAY intersecting_parcels


    