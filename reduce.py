import h5py
import subprocess

data_dir = "cgns"
time_delay_in_hour = 6
time_delay_in_hour = time_delay_in_hour * 3600
while True:
    time.sleep(time_delay_in_hour)
    print "Pause for ", str(time_delay_in_hour / 3600), " hours."
    filelist = subprocess.Popen(["ls", data_dir], stdout=subprocess.PIPE).communicate()[0].strip().split("\n")
    for filename in filelist:
        filename = data_dir + "/" + filename
        # adf2hdf5
        cmd_adf2hdf5_list = ["cgnsconvert", "-h", filename, filename]
        cmd_adf2hdf5_str = " ".join(cmd_adf2hdf5_list)
        flag_err = subprocess.call(cmd_adf2hdf5_list)
        if flag_err == 0:
            # remove extra data
            h5file = h5py.File(filename, "a")
            del h5file["/Base/Zone/GridCoordinates"]
            del h5file["/Base/Zone/ZoneBC"]
            del h5file["/Base/Zone/ZoneType"]
            del h5file["/Base/Zone/farfield"]
            del h5file["/Base/Zone/fluid"]
            del h5file["/Base/Zone/in_freestream"]
            del h5file["/Base/Zone/in_nozzle"]
            del h5file["/Base/Zone/outflow"]
            del h5file["/Base/Zone/wall_nozzle"]
            del h5file["/Base/Zone/wall_nozzle-shadow"]
            h5file.close()
            # h5pack
            cmd_h5repack_list = ["h5repack", filename, filename+".tmp"]
            flag_err = subprocess.call(cmd_h5repack_list)
            if flag_err != 0:
                exit("Error: h5repack!")
            # remove old and get new
            cmd_old2new_list = ["mv", "-f", filename+".tmp", filename]
            flag_err = subprocess.call(cmd_old2new_list)
            if flag_err != 0:
                exit("Error: remove old cgns!")

