#!/usr/bin/env python3

import os, json
import numpy as np

import viz

def load_data(f):
    return json.load(open(str(f)))

DATA_DIR = "../data/training/"
files = os.listdir(DATA_DIR)

class Task():
    def __init__(self, idx, task, data):
        self.idx = idx
        self.task = task
        self.x = [np.array(i['input']) for i in data]
        self.y = [np.array(i['output']) for i in data]

idx = 64
task = files[idx]
data = load_data(str(DATA_DIR + task))

sample = Task(idx, task, data['train'])

print(f"ID: {sample.idx} | {sample.task}")
viz.plot_set(sample.x, sample.y)