#!/usr/bin/env python
# -*- coding: utf-8 -*-

def filter(x):
    if x.strand == '+':
        x.end = x.start
        x.start -= 2500
    if x.strand == '-':
        x.start = x.end
        x.end += 2500
    x.feature = 'promoter'
    return x

def promoters(input, output):
    """
    """
    import pandas as pd
    df = pd.read_csv(input, index_col=False, sep='\t', header=None)
    df.columns = ['seqname', 'source', 'feature', 'start', 'end', 'score', 'strand', 'frame', 'attribute']
    df = df.apply(lambda x: filter(x), axis=1)
    df.to_csv(output, header=None, index=False, sep='\t')

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()#pylint: disable=invalid-name
    parser.add_argument("-i", "--input", help="Input file (.gff format)", required=True)
    parser.add_argument("-o", "--output", help="Output file (.gff format)",required=True)
    args = parser.parse_args()#pylint: disable=invalid-name
    promoters(args.input, args.output)
