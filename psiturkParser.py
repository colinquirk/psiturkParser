#! /usr/bin/env python

import os, sys, argparse
import csv, json


class Parser:
    def __init__(self, filename=None, newfile=None, overwrite=False):
        if filename is None:
            self.filename = 'trialdata.csv'
        else:
            self.filename = filename

        if newfile is None:
            newfile = 'fixedtrialdata.csv'
            if not overwrite:
                i = 1
                while os.path.isfile(newfile):
                    newfile = 'fixedtrialdata(%i).csv' % i
                    i += 1
            self.newfile = newfile
        else:
            self.newfile = newfile

        self.fieldnames = []
        self.data = []

    def _append_fieldnames(self, keys):
        for new_key in set(keys).difference(self.fieldnames):
            self.fieldnames.append(new_key)

    def _get_data(self):
        with open(self.filename, 'r') as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                trial = json.loads(row[3])
                trial['UID'], trial['trial_number'], trial['datetime'] = row[:3]
                self._append_fieldnames(trial.keys())
                self.data.append(trial)

    def _write_data(self):
        with open(self.newfile, 'w') as f:
            writer = csv.DictWriter(f, self.fieldnames)
            writer.writeheader()
            writer.writerows(self.data)

    def run(self):
        self._get_data()
        self._write_data()

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('-f', '--filename',
                    help='The filepath or filename of the file you want to parse')
    ap.add_argument('-n', '--newfile',
                    help='The filepath or filename of the file you want to create')
    ap.add_argument('-o', '--overwrite',
                    help='Files will be overwritten', action='store_true')

    args = ap.parse_args()

    p = Parser(**vars(args))
    p.run()
