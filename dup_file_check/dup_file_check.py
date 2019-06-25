import glob
import os.path

input_dir = r'C:\GitHub\dup_file_check\test\gdbs'
replica_list = glob.glob(os.path.join(input_dir, '*.gdb'))

replica_count = {}


def dup_check(replicas):
    try:
        for replica in replicas:
            basename = os.path.basename(replica)
            lib_name = basename.split('_')[0]
            if lib_name in replica_count:
                replica_count[lib_name] += 1
            else:
                replica_count[lib_name] = 1

        dups = {k: v for (k, v) in replica_count.items() if v > 1}

        if len(dups) > 0:
            dup_names = ', '.join(dups.keys())
            raise ValueError("There are duplicate replicas in the test folder. "
                             "Please check libraries: {}".format(dup_names))
    except ValueError as e:
        print e
    except Exception as e:
        print e


dup_check(replica_list)
