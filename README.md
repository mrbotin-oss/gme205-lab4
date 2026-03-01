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
     Store all Parcel objects in parcel_list

iv. If parcel_list is empty:
       Display error message
       Stop program

v. Initialize:
       total_active_area = 0 sqm
       threshold_area = 300 sqm
       large_parcels = empty list
       count_per_zone = empty dictionary
       intersecting_parcels = empty list
       target_zone = "Residential"

vi. For each parcel in parcel_list:

       If parcel is active:
           total_active_area = total_active_area + parcel.area()

       If parcel.area() > threshold_area:
           Add parcel to large_parcels

       Let zone = parcel.zone
       If zone is not in count_per_zone:
           count_per_zone[zone] = 1
       Else:
           count_per_zone[zone] = count_per_zone[zone] + 1

vii. Select all parcels whose zone == target_zone
     Store in target_zone_parcels

viii. For each parcel in parcel_list:
          For each target_parcel in target_zone_parcels:
              If parcel intersects target_parcel:
                  Add parcel to intersecting_parcels
                  Break

ix. Display:
       total_active_area
       count_per_zone
       large_parcels
       intersecting_parcels

x. End

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
    SET threshold_area = 300
    SET large_parcels = empty list
    SET count_per_zone = empty dictionary
    SET intersecting_parcels = empty list
    SET target_zone = "Residential"

    FOR EACH parcel IN parcel_list

        IF parcel is active THEN
            total_active_area = total_active_area + parcel.area()
        END IF

        IF parcel.area() > threshold_area THEN
            APPEND parcel TO large_parcels
        END IF

        IF parcel.zone NOT IN count_per_zone THEN
            count_per_zone[parcel.zone] = 1
        ELSE
            count_per_zone[parcel.zone] = count_per_zone[parcel.zone] + 1
        END IF

    END FOR

    SET zone_parcels = all parcels WHERE parcel.zone == target_zone

    FOR EACH parcel IN parcel_list
        FOR EACH target_parcel IN zone_parcels
            IF parcel intersects target_parcel THEN
                APPEND parcel TO intersecting_parcels
                BREAK
            END IF
        END FOR
    END FOR

    DISPLAY total_active_area
    DISPLAY count_per_zone
    DISPLAY large_parcels
    DISPLAY intersecting_parcels
END

# Reflection
1.  Where in your system do Sequence, Selection, and Repetition explicitly appear? 	
- In GIS programming, Sequence is the order the spatial processing steps happen, this happens everywhere in your system because procedural programming runs one step after another. 
- Selection means the program checks conditions and decides what to do. We can find it in our analysis.py and run_lab4.py where the parameter and functions is being added in the script. 
- Repetition goes hand-in-hand with selection, since GIS data often has hundreds or thousands of features, the program must repeat the same process for each one that is stated in Selection.


2. If you removed your algorithm planning step, how would your implementation likely change?	
- If I removed the algorithm planning step, my implementation would probably still function in the end, but the process of getting there would be much slower and less organized that would also leads to more trial and error in creating the scripts and more time spent reconstructing the script and in the end, the system would likely be less efficient and hard to understand and maintain. 


3. Where does spatial behavior live in your system, and why is that important?	
- Spatial behavior in the system lives in spatial.py. Keeping spatial behavior inside these classes is important because it preserves clear separation of responsibilities. The rest of the system does not need to know how spatial calculations are performed. It simply interacts with the objects through their defined methods. This hides the complexity of the spatial logic and prevents it from being scattered across multiple files.


4. Why does analysis.py contain structured logic instead of demo.py? 
- Just like the spatial behavior, another scripts are created to seperate the responsibility of each script. 
- analysis.py contains the structured logic because it is responsible for performing the actual analytical work, such as answering specific questions about the data. 
- While, demo.py manages the overall process like loading the inputs, calling the analysis functions, and producing the outputs. 
- By separating these responsibilities, the analytical logic stays organized and contained in one place, while the other script focuses on coordinating the workflow. This makes the system clearer and easier to maintain.


5. What would happen if all filtering logic were placed inside the Parcel class? 
- If all filtering logic were placed inside the Parcel class, the class would start taking on too much responsibility. Instead of just representing a parcel and handling its spatial behavior, it would also do analytical decisions like deciding which parcels meet certain criteria. Its like the system will be overwhelmed if it will represent the data or analyse the data.


6.	If a new rule is added (e.g., “exclude inactive industrial parcels”), how easily can your current design adapt?
- Because the analytical logic lives in analysis.py and the spatial data structure lives in the Parcel class, I can simply update or add a filtering condition inside the analysis.py, this change would not require modifying the overall workflow simce we took our time to structure our logic properly and assigned different responsibilities to each script. 


7.	How does separating structured logic from object behavior prevent “God classes”?
- Separating structured logic from object behavior helps prevent “God classes” because it keeps each part of the system focused on a single responsibility. A God class happens when one class tries to do everything like storing the data, managing the behavior, perform analysis, and control workflows. This quickly makes our script long and complicated thst makes it hard to maintain.




    