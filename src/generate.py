import os
import shutil

def clean_public(dir="./public"):
    logging(f"Removing {dir}")
    shutil.rmtree(dir)
    os.mkdir(dir)

def copy_static(input_dir="./static/", output_dir="./public/"):
    for item in os.listdir(input_dir):
        in_file = os.path.join(input_dir, item)
        out_file = os.path.join(output_dir, item)
        if os.path.isfile(in_file):
            logging(f"Copying {in_file} to {output_dir}")
            shutil.copy(in_file, output_dir)
        else:
            if not os.path.isdir(out_file):
                logging(f"Making directory {out_file}")
                os.mkdir(out_file)
            copy_static(in_file, out_file)

def logging(msg):
    print(f"LOG: {msg}")
    pass