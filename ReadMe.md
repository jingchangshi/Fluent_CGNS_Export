# Instruction

Ansys Fluent 16.1 export data of format CGNS during execution, then apply this Python script to reduce file size, since there are abundant contents like grid coordinates. When the number of CGNS files is large, this shrinking action is necessary to reduce disk usage.

# Requirements

+ h5py
+ cgnsconvert binary utility
+ h5repack binary utility

# Usage

+ Set all the CGNS data file exported to a separate directory, say, a subdir `cgns` in the fluent working directory.
+ Run fluent
+ Put this script in the fluent working directory and set the subdir name for the CGNS export directory.
+ Run this script. It will omit those transformed CGNS data file and only deal with the new ones.

