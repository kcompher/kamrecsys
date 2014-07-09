#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Load sample sushi3 data sets
"""

from __future__ import (
    print_function,
    division,
    absolute_import)

#==============================================================================
# Imports
#==============================================================================

import sys
import os
import io
import logging
import numpy as np

from ..data import EventWithScoreData
from ._base import SAMPLE_PATH

#==============================================================================
# Public symbols
#==============================================================================

__all__ = ['SUSHI3_INFO',
           'load_sushi3b_score']

#==============================================================================
# Constants
#==============================================================================

# Conversion tables for mapping the numbers to names for the ``sushi3``
# data set. available tables are ``user_age``, ``user_prefecture``,
# ``user_region``, and ``item_genre``.
SUSHI3_INFO = {
    'user_age': np.array([
        '15-19', '20-29', '30-39', '40-49', '50-59', '60-'
    ]),
    'user_prefecture': np.array([
        'Hokkaido', 'Aomori', 'Iwate', 'Akita', 'Miyagi',
        'Yamagata', 'Fukushima', 'Niigata', 'Ibaraki', 'Tochigi',
        'Gunma', 'Saitama', 'Chiba', 'Tokyo', 'Kanagawa',
        'Yamanashi', 'Shizuoka', 'Nagano', 'Aichi', 'Gifu',
        'Toyama', 'Ishikawa', 'Fukui', 'Shiga', 'Mie',
        'Kyoto', 'Osaka', 'Nara', 'Wakayama', 'Hyogo',
        'Okayama', 'Hiroshima', 'Tottori', 'Shimane', 'Yamaguchi',
        'Ehime', 'Kagawa', 'Tokushima', 'Kochi', 'Fukuoka',
        'Nagasaki', 'Saga', 'Kumamoto', 'Kagoshima', 'Miyazaki',
        'Oita', 'Okinawa', 'non-Japan'
    ]),
    'user_region': np.array([
        'Hokkaido', 'Tohoku', 'Hokuriku', 'Kanto+Shizuoka', 'Nagano+Yamanashi',
        'Chukyo', 'Kinki', 'Chugoku', 'Shikoku', 'Kyushu',
        'Okinawa', 'non-Japan'
    ]),
    'item_genre': np.array([
        'aomono (blue-skinned fish)',
        'akami (red meat fish)',
        'shiromi (white-meat fish)',
        'tare (something like baste; for eel or sea eel)',
        'clam or shell',
        'squid or octopus',
        'shrimp or crab',
        'roe',
        'other seafood',
        'egg',
        'non-fish meat',
        'vegetable'
    ])
}

#==============================================================================
# Module variables
#==============================================================================

#==============================================================================
# Classes
#==============================================================================

#==============================================================================
# Functions 
#==============================================================================


def load_sushi3b_score(infile=None, event_dtype=None):
    """ load the sushi3b score data set

    An original data set is distributed at:
    `SUSHI Preference Data Sets <http://www.kamishima.net/sushi/>`_.

    Parameters
    ----------
    infile : optional, file or str
        input file if specified; otherwise, read from default sample directory.
    event_dtype : np.dtype, default=None
        dtype of extra event features

    Returns
    -------
    data : :class:`kamrecsys.data.EventWithScoreData`
        sample data

    Notes
    -----
    Format of events:

    * each event consists of a vector whose format is [user, item].
    * 50,000 events in total
    * 5,000 users rate 100 items (=sushis)
    * dtype=np.int

    Format of scores:

    * one score is given to each event
    * domain of score is [0.0, 1.0, 2.0, 3.0, 4.0]
    * dtype=np.float

    Format of user's feature ( `data.feature[0]` ):

    original_uid : int
        uid in the original data
    gender : int {0:male, 1:female}
        gender of the user
    age : int, SUSHI3_INFO['user_age']
        age of the user
    answer_time : int
    #     the total time need to fill questionnaire form
    child_prefecture : int, SUSHI3_INFO['user_prefecture']
        prefecture ID at which you have been the most long lived
        until 15 years old
    child_region : int, SUSHI3_INFO['user_region']
        region ID at which you have been the most long lived
        until 15 years old
    child_ew : int {0: Eastern, 1: Western}
        east/west ID at which you have been the most long lived
        until 15 years old
    current_prefecture : int, SUSHI3_INFO['user_prefecture']
        prefecture ID at which you currently live
    current_region : int, SUSHI3_INFO['user_region']
        regional ID at which you currently live
    current_ew : int {0: Eastern, 1: Western}
        east/west ID at which you currently live
    moved : int {0: don't move, 1: move}
        whether child_prefecture and current_prefecture are equal or not

    Format of item's feature ( `data.feature[1]` ):

    name : str, encoding=utf-8
        title of the movie with release year
    maki : int {0:otherwise, 1:maki}
        whether a style of the sushi is *maki* or not
    seafood : int {0:otherwise, 1:seafood}
        whether seafood or not
    genre : int, int, SUSHI3_INFO['item_genre']
        the genre of the sushi *neta*
    heaviness : float, range=[0-4], 0:heavy/oily
        mean of the heaviness/oiliness/*kotteri* in taste,
    frequency : float, range=[0-3], 3:frequently eat
        how frequently the user eats the SUSHI,
    price : float, range=[1-5], 5:expensive
        maki and other style sushi are normalized separately
    supply : float, range=[0-1]
       the ratio of shops that supplies the sushi
    """

    # load event file
    if infile is None:
        infile = os.path.join(SAMPLE_PATH, 'sushi3b_score.event')
    if event_dtype is None:
        dtype = np.dtype([('event', np.int, 2), ('score', np.float)])
    else:
        dtype = np.dtype([('event', np.int, 2), ('score', np.float),
                          ('event_feature', event_dtype)])
    x = np.genfromtxt(fname=infile, delimiter='\t', dtype=dtype)
    data = EventWithScoreData(n_otypes=2, n_stypes=1)
    if event_dtype is None:
        data.set_events(x['event'], x['score'], score_domain=(0.0, 4.0))
    else:
        data.set_events(x['event'], x['score'], score_domain=(0.0, 4.0),
                        event_feature=x['event_feature'])

    # load user's feature file
    infile = os.path.join(SAMPLE_PATH, 'sushi3.user')
    fdtype = np.dtype([
        ('original_uid', np.int),
        ('gender', np.int),
        ('age', np.int),
        ('answer_time', np.int),
        ('child_prefecture', np.int),
        ('child_region', np.int),
        ('child_ew', np.int),
        ('current_prefecture', np.int),
        ('current_region', np.int),
        ('current_ew', np.int),
        ('moved', np.int)])
    dtype = np.dtype([('eid', np.int), ('feature', fdtype)])
    x = np.genfromtxt(fname=infile, delimiter='\t', dtype=dtype)
    data.set_features(0, x['eid'], x['feature'])

    # load item's feature file
    infile = io.open(os.path.join(SAMPLE_PATH, 'sushi3.item'), 'r',
                     encoding='utf-8')
    fdtype = np.dtype([
        ('name', 'U20'),
        ('maki', np.int),
        ('seafood', np.int),
        ('genre', np.int),
        ('heaviness', np.float),
        ('frequency', np.float),
        ('price', np.float),
        ('supply', np.float)])
    dtype = np.dtype([('eid', np.int), ('feature', fdtype)])
    x = np.genfromtxt(fname=infile, delimiter='\t', dtype=dtype)
    data.set_features(1, x['eid'], x['feature'])

    return data

#==============================================================================
# Module initialization 
#==============================================================================

# init logging system ---------------------------------------------------------
logger = logging.getLogger('kamrecsys')
if not logger.handlers:
    logger.addHandler(logging.NullHandler)

#==============================================================================
# Test routine
#==============================================================================


def _test():
    """ test function for this module
    """

    # perform doctest
    import doctest

    doctest.testmod()

    sys.exit(0)

# Check if this is call as command script -------------------------------------

if __name__ == '__main__':
    _test()
