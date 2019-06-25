import zipfile
import os.path
import glob
import datetime
import shutil

input_path = r'C:\GitHub\zipping\test\gdbs'

replica_list = glob.glob(os.path.join(input_path, '*.gdb'))

def zip_replicas(replicas):
    zip_dir = os.path.dirname(replicas[0])
    date = datetime.date.today().strftime('%Y%m%d')
    zip_name = 'Scanned_{}_files.zip'.format(date)
    zip_loc = os.path.join(zip_dir,zip_name)

    with zipfile.ZipFile(zip_loc, "w", zipfile.ZIP_DEFLATED) as replica_zip:
        for replica in replicas:
            print os.path.basename(replica)
            gdb_files = glob.glob(os.path.join(replica, '*'))
            print gdb_files
            for gdb_file in gdb_files:
                archive_loc = os.path.join(
                    os.path.basename(replica),
                    os.path.basename(gdb_file))
                replica_zip.write(gdb_file, archive_loc)



zip_replicas(replica_list)

