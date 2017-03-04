#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import common.ml as ml
import common.pz as pz
import json, argparse, os, arff
from common.utils import use_progressbar, count_file, read_hashed_call_graph

def remove_emtpy_hcg(directory):
    # progressbar
    file_count = count_file(directory, '_hcg.json')
    pbar = use_progressbar('Removing empty hcgs...', file_count)
    pbar.start()
    progress = 0

    emtpy_hcg_list = []
    count = 0
    for parent, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            if filename == 'directed_hcg.json':
            # if filename == 'hcg.json':
                hcg_file = os.path.join(parent, filename)
                statinfo = os.stat(hcg_file)
                hcg_size = statinfo.st_size
                if hcg_size <= 2:
                    emtpy_hcg_list.append(hcg_file)
                    count += 1
                    os.remove(hcg_file)

                # progressbar
                progress += 1
                pbar.update(progress)

    # progressbar
    pbar.finish()

    print '[SC] Removed %d empty hcgs' % count
    for empty_hcg in emtpy_hcg_list:
        print empty_hcg

def compute_label_histogram(hcg):
    '''compute the histogram of nhashs in hashed call graph. Every label is a
       binary array. The histogram length is 2**len(nhashs)'''
    labels = [hcg[node]['nhash'] for node in hcg]
    h = np.zeros(2 ** len(labels[0]))
    for l in labels:
        h[int(l, base=2)] += 1
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
                hcg = read_hashed_call_graph(os.path.join(parent, filename))
                x_i = compute_label_histogram(hcg)
                matrix.append(x_i)
                filename_list.append(os.path.split(parent)[1])

                # progressbar
                progress += 1
                pbar.update(progress)

    # progressbar
    pbar.finish()

    # 3. convert matrix to binary
    print '[SC] Converting python list to numpy matrix...'
    matrix = np.array(matrix, dtype=np.int16)
    print '[SC] Converting features vectors to binary...'
    matrix, m = ml.make_binary(matrix)

    return matrix, m, truth_label, filename_list

def save_data(X, m, Y, filenames):
    '''Store pz objects for the data matrix, the labels and
        the name of the original samples so that they can be used
        in a new experiment without the need to extract all
        features again'''
    print '[SC] Saving labels, data matrix and file names...'
    pz.save(X, 'X.pz')
    pz.save(m, 'maximum.pz')
    pz.save(Y, 'Y.pz')
    pz.save(filenames, 'filenames.pz')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--directory', help='directory of the hcg file')
    args = parser.parse_args()
    if args.directory:
        remove_emtpy_hcg(args.directory)
        matrix, m, truth_label, filename_list = embed_all(args.directory)
        save_data(matrix, m, truth_label, filename_list,)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()