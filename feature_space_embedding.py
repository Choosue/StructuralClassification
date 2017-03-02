#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import common.ml as ml
import common.pz as pz
import json, argparse, os, arff
from count_hash import get_hash, count
from common.utils import use_progressbar, count_file

def compute_label_histogram(hcgpath):
    '''compute the histogram of nhashs in hashed call graph. Every label is a
       binary array. The histogram length is 2**len(nhashs)'''
    hcg_hash_dict = get_hash(hcgpath)
    nhashs = [node for node in hcg_hash_dict]
    h = np.zeros(2 ** len(nhashs[0]))
    for nhash in nhashs:
        h[int(''.join([str(i) for i in nhash]), base=2)] += 1
    return h

def get_categories(directory):
    '''get category dict'''
    # progressbar
    file_count = count_file(directory, '_hcg.json')
    pbar = use_progressbar('Get categories...', file_count)
    pbar.start()
    progress = 0

    category_dict = dict()
    category_index = 0
    for parent, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            if filename == 'directed_hcg.json':
            # if filename == 'hcg.json':
                category = os.path.basename(os.path.split(os.path.split(parent)[0])[0])
                if category not in category_dict:
                    category_dict[category] = category_index
                    category_index += 1

                # progressbar
                progress += 1
                pbar.update(progress)

    # progressbar
    pbar.finish()

    return category_dict

def embed_all(directory):
    '''iteratively embed all the hashed call graph into a sparse matrix'''

    # 1. get category dict
    category_dict = get_categories(directory)

    # progressbar
    file_count = count_file(directory, '_hcg.json')
    pbar = use_progressbar('Computing label histogram...', file_count)
    pbar.start()
    progress = 0

    # 2. iteratively embed all the hashed call graph into matrix
    #    the label of each hashed call graph stored in truth_label
    #    record filenames in filename_list also
    matrix = []
    truth_label = np.array([])
    filename_list = []
    for parent, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            if filename == 'directed_hcg.json':
            # if filename == 'hcg.json':
                category = os.path.basename(os.path.split(os.path.split(parent)[0])[0])
                truth_label = np.append(truth_label, category_dict[category])
                x_i = compute_label_histogram(os.path.join(parent, filename))
                matrix.append(x_i)
                filename_list.append(os.path.split(parent)[1])

                # progressbar
                progress += 1
                pbar.update(progress)

    # progressbar
    pbar.finish()

    # 3. convert matrix to binary
    matrix = np.array(matrix, dtype=np.int16)
    print '[SC] Converting features vectors to binary...'
    matrix, m = ml.make_binary(matrix)

    return matrix, truth_label, filename_list

def save_data(X, Y, filenames):
    '''Store pz objects for the data matrix, the labels and
        the name of the original samples so that they can be used
        in a new experiment without the need to extract all
        features again'''
    print '[SC] Saving labels, data matrix and file names...'
    pz.save(X, 'X.pz')
    pz.save(Y, 'Y.pz')
    pz.save(filenames, 'filenames.pz')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--directory', help='directory of the hcg file')
    args = parser.parse_args()
    if args.directory:
        matrix, truth_label, filename_list = embed_all(args.directory)
        save_data(matrix, truth_label, filename_list)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()