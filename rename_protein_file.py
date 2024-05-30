#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Title: rename_protein_file.py
Date: May 29th, 2024
Author: Auguste de Pennart
Description:
    unzip fasta files and relabel the fasta headers to include shortened species name

List of functions:
    rename_file
        sort numerically file list
    rename_file_stack
        processing, more information online
    rename_file_stack_2
        makes image pyramid

List of "non standard modules"
    no non standard modules

Procedure:
    1. takes unzipped images as input
    2. unzips images into temporary folder
    3. relabels fasta headers
    4. exports fasta files with relabelled headers to the designated output folder

Usage:
    pyramid_make.py [-h] [-v] -i INPUT_FOLDER -o OUTPUT_FOLDER [-c CORES]

known error:
    1. NA

 """
import logging
import os, re, sys
import argparse


from multiprocessing import Pool
from tqdm import tqdm
import gzip
import shutil
import pathlib

logging.basicConfig(level=logging.INFO)

#function for unzipping and relabelling fasta headers
def rename_file(file_paths):
    fasta = file_paths[0].split('/')[-1] #file name
    if re.search(".gz$",fasta):  #finds file ending with .gz, unzipped files
        with gzip.open(file_paths[0], 'rb') as f_in: #unzips file
            match = re.search(r'(.+).gz', fasta).group(1)
            temp_out=os.path.join(file_paths[1], "temp_dir")
            os.makedirs(temp_out, exist_ok=True)
            filename = os.path.join(temp_out, match)
            with open(filename, 'wb') as f_temp:
                shutil.copyfileobj(f_in, f_temp)
            
            with open (filename, "r") as f_temp: #relabels fasta headers
                filename_2 = os.path.join(file_paths[1], match)
                with open (filename_2, "w") as f_out:
                    for line in f_temp:
                        if re.search('^>', line):  # finds line if fasta header
                            try:
                                match = re.search(r'\[([A-Za-z]{3})[A-Za-z]*\s([A-Za-z]{3})[A-Za-z]*\]$', line).group(1,2) #finds genus and species for relabelling headers
                            except AttributeError:
                                    match = re.search(r'\[([A-Za-z]{3})[A-Za-z]*\s[A-Za-z]*[\s]*([A-Za-z]{3})[A-Za-z]*\]$', line).group(1,2)
                            not_start = re.search(r'>(.+)', line).group(1)
                            line=">"+match[0]+"_"+match[1]+"_"+not_start
                            print(line.strip(), file=f_out)
                        else:
                            print(line.strip(), file=f_out)
            pathlib.Path.unlink(filename)  
    return True

#old version for renaming  the fasta headers off the fasta file name. This works when species name in fasta file name
# def rename_file_stack(files_dir,
#                         n_workers,                        
#                         out_dir):
#     #making list of all viariables except files_dir, this will be added to all variables in inputs in the form of a dictionary, to allow iteration but also keeping the meta with each image
#     files_dir = os.path.abspath(files_dir)
#     files_list=os.listdir(files_dir)
#     os.makedirs(out_dir, exist_ok=True)

#     inputs = [os.path.join(files_dir, f) for f in files_list]
#     logging.info(f'Processing {len(inputs)} files from: {files_dir}')
#     logging.info(f'Using {n_workers} workers')

#     for input in inputs:
#         z = input.split('/')[-1]
#         if re.search(".fasta",z): 
#             inputted = open(input, 'r')
#             match = re.search(r'^([A-Za-z]{0,3})[A-Za-z]*\_([A-Za-z]{2,3})', z).group(1,2)
#             filename = os.path.join(out_dir, z)
#             output = open(filename, 'w')
#             for line in inputted:
#                 if re.search('^>', line):  # finds line if fasta header
#                     not_start = re.search(r'>(.+)', line).group(1)
#                     line=">"+match[0]+"_"+match[1]+"_"+not_start
#                     print(line.strip(), file=output)
#                 else:
#                     print(line.strip(), file=output)
#             inputted.close()  # closing
#             output.close()  # closing
#     logging.info('Done!')
#     logging.info(f'Output in: {out_dir}')
#     return

#sets up the previous function rename_file for parralel processing
def rename_file_stack_2(files_dir,
                        n_workers,                        
                        out_dir):
    files_list=os.listdir(files_dir) #files in input folder
    os.makedirs(out_dir, exist_ok=True)  #makes output directory
    inputs = [os.path.join(files_dir, f) for f in files_list] #creates file paths
    path_dic= {input: out_dir for input in inputs} #dictionary of input file with output file destination
    logging.info(f'Processing {len(inputs)} images from: {files_dir}') 
    logging.info(f'Using {n_workers} workers')
    with Pool(n_workers) as p: #parallel processor
        results = list(tqdm(p.imap(rename_file, path_dic.items()), total=len(inputs)))
    #removes temporary folder
    temp_out=os.path.join(out_dir, "temp_dir")
    try:
        pathlib.Path.rmdir(temp_out)
    except OSError:
        print("Did not remove temporary folder as folders were still inside")
    logging.info('Done!')
    logging.info(f'Output in: {out_dir}')
    return

if __name__ == '__main__':
    usage='make an image pyramd of inputted image(s)'
    parser=argparse.ArgumentParser(description=usage)#create an argument parser

    #creates the argument for program version
    parser.add_argument('-v', '--version',
                        action='version',
                        version='%(prog)s 1.0')
    #creates the argument where input_folder will be inputted
    parser.add_argument('-i', '--input_folder',
                        metavar='INPUT_FOLDER',
                        dest='files_dir',
                        required=True,
                        help='input folder')
    #creates the argument where the output folder will be inputted
    parser.add_argument('-o', '--output_folder',
                        metavar='OUTPUT_FOLDER',
                        dest='out_dir',
                        required=True,
                        help='output folder')
    parser.add_argument('-c', '--cores',
                        metavar='CORES',
                        dest='n_workers',
                        default=1,
                        type=int,
                        help='number of cores to use')
    args=parser.parse_args()#parses command line
    rename_file_stack_2(os.path.abspath(args.files_dir),
                        args.n_workers,
                        os.path.abspath(args.out_dir)
                       )
    
    
