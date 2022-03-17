# -*- coding: utf-8 -*-
import sys
from string import Template 

if len(sys.argv) == 1:
    print('Specification of the argument is insufficient')
else:
    args = sys.argv[1:]

    N = len(args)
    baggages = []

    for idx in range(N):
        i, weight = args[idx].split(":")
        baggages.append((i, int(weight)))

    tracks_weightSum = [0]*3
    tracks_ids = [[],[],[]]

    for baggage in baggages:
        idx_weight_min = tracks_weightSum.index(min(tracks_weightSum))
        tracks_weightSum[idx_weight_min] += baggage[1]
        tracks_ids[idx_weight_min].append(baggage[0])
    
    for idx in range(len(tracks_ids)):
        template = Template('track_$num: $ids')
        ids = ','.join(tracks_ids[idx])
        print(template.substitute({
            'num': idx+1,
            'ids': ids
        }))