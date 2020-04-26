#!/usr/bin/env python3

import argparse
import copy
import csv
import os
import sys

'''

************************************
*******        EXAMPLE       *******
************************************


    candidates = [wikipedia.org, warcraft.com]
    
    prefs = [
        google -> [warcraft(1), wikipedia(2)]
        yandex -> [warcraft(1), wikipedia(6)]
    ]
    
'''


class InputError(Exception):

    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return repr(self.msg)


class PreferenceSchedule:

    def __init__(self, candidates, prefs):
        # check whether the candidates list consists of only strings
        if not all(map(lambda x: type(x) == str, candidates)):
            raise InputError('Candidate must be a string')

        # check the validity of the preferences
        for pref in prefs:
            # check whether the number of candidates in the preference schedule
            # is valid
            if len(pref) != len(candidates):
                raise InputError('Invalid preference schedule')

            # check whether the candidates in the preference schedule are unique
            if len(pref) != len(candidates):
                raise InputError('Invalid preference schedule')

            # check whether the candidates in the preference schedule are also
            # in the candidates list
            for candidate in pref:
                if candidate not in candidates:
                    raise InputError('Invalid preference schedule')

        self.prefs = prefs

    def original(self):
        """
        Returns the original preference schedule as a printable string
        :return:
        """

        res = ''
        for i in range(len(self.prefs)):
            res += 'Voter {}: '.format(i + 1) + ', '.join(self.prefs[i]) + '\n'

        return res[:-1]

    def detailed(self):
        """
        Returns the detailed preference schedule as a printable string
        :return:
        """

        # count the number of occurences of each preference
        prefs = self.prefs[:]
        prefs = [tuple(p) for p in self.prefs]
        counts = {}
        while prefs:
            pref = prefs.pop(0)
            count = 1
            while pref in prefs:
                prefs.remove(pref)
                count += 1
            counts[pref] = count

        res = ''
        for pref in counts:
            res += str(counts[pref]) + ' Voters: ' + ', '.join(pref) + '\n'

        return res[:-1]


class Aggregator:

    def __init__(self, candidates, prefs):
        self.candidates = candidates
        self.pref_schedule = PreferenceSchedule(candidates, prefs)

    def __str__(self):
        res = ''
        res += 'Preference Schedule:\n'
        res += self.pref_schedule.original() + '\n\n'
        res += 'Detailed Preference Schedule:\n'
        res += self.pref_schedule.detailed() + '\n'

        return res

    def borda(self):
        '''Prints who wins by the Borda count'''

        counts = {}
        candidates = list(self.pref_schedule.prefs[0])
        for candidate in candidates:
            counts[candidate] = 0

        max_point = len(candidates)
        for pref in self.pref_schedule.prefs:
            for i in range(len(pref)):
                counts[pref[i]] += max_point - i

        print('Borda scores:', counts)
        print('The winner(s) is(are)', find_winner(counts))

    def condorcet_pairwise_comparison(self):
        """
        Prints who wins by the pairwise comparison method
        :return:
        """

        points = {candidate: 0 for candidate in self.candidates}
        candidates = list(self.candidates)
        for candidate in candidates[:]:
            candidates.remove(candidate)
            for rival in candidates:
                candidate_points = 0
                for pref in self.pref_schedule.prefs:
                    if pref.index(candidate) < pref.index(rival):
                        candidate_points += 1
                    else:
                        candidate_points -= 1
                if candidate_points > 0:
                    points[candidate] += 1
                else:
                    points[rival] += 1

        print('Pairwise comparison points:', points)
        print('The winner(s) is(are)', find_winner(points))


def find_winner(aggregated_result):
    max_point = 0
    for point in aggregated_result.values():
        if point > max_point:
            max_point = point

    winner = []  # winner can be many, so use a list here
    for candidate in aggregated_result.keys():
        if aggregated_result[candidate] == max_point:
            winner.append(candidate)

    return winner
