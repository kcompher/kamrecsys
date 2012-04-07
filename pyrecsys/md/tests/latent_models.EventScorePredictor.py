#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
>>> import numpy as np
>>>
>>> from pyrecsys.datasets import *
>>> from pyrecsys.md.latent_factor import EventScorePredictor
>>>
>>> np.random.seed(1234)
>>>
>>> data = load_movielens_mini()
>>>
>>> recommender = EventScorePredictor(C=0.1, k=2)
>>> print vars(recommender)
{'C': 0.1, 'n_otypes': 0, 'bu_': None, 'bi_': None, 'k': 2, 'p_': None, 'q_': None, 'f_loss_': inf, 'iid': None, 'coef_': None, 'eid': None, 'n_objects': None, 'mu_': None}
>>>
>>> recommender.fit(data, disp=True, gtol=1e-03)
Optimization terminated successfully.
         Current function value: 0.041362
         Iterations: 28
         Function evaluations: 55
         Gradient evaluations: 55
>>> print vars(recommender)
{'event_otypes': array([0, 1]), 'C': 0.1, 'n_otypes': 2, 'bu_': array([-0.21564908, -1.04233246, -0.06157792, -0.3118242 ,  1.37232348,
       -1.14096741,  0.19455614,  0.26853631,  0.        ]), 'bi_': array([ 0.56576553, -0.58197975,  0.62733207, -0.13134276, -1.06205273,
        1.07056572,  0.23409911, -1.00032167,  0.54094141, -0.82827541,  0.        ]), 'k': 2, 'p_': array([[ 1.04478423,  0.44689326],
       [ 0.83739591, -0.165298  ],
       [-0.18222167, -0.11556423],
       [ 0.13730554, -1.78987991],
       [-0.59188215, -0.38421568],
       [ 0.69241523,  0.32657381],
       [ 0.06755593, -0.10375833],
       [-0.50583626, -0.19203944],
       [ 0.        ,  0.        ]]), 'q_': array([[ 0.9518302 ,  0.02300344],
       [ 0.21112834, -0.19107502],
       [ 0.09943394, -0.40238463],
       [-0.42549055,  0.30052102],
       [ 0.62495312, -0.07551696],
       [ 0.60399383, -0.34648057],
       [-0.07033854,  0.8787781 ],
       [-0.96237509, -0.99783873],
       [ 0.94682156,  0.01181251],
       [ 0.29838862,  0.09419616],
       [ 0.        ,  0.        ]]), 's_event': 2, 'f_loss_': 0.041362129019781292, 'iid': array([{1: 0, 2: 1, 5: 2, 6: 3, 7: 4, 8: 5, 9: 6, 10: 7},
       {1: 0, 2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 7: 6, 8: 7, 9: 8, 10: 9}], dtype=object), 'coef_': array([ 3.66306486, -0.21564908, -1.04233246, -0.06157792, -0.3118242 ,
        1.37232348, -1.14096741,  0.19455614,  0.26853631,  0.        ,
        0.56576553, -0.58197975,  0.62733207, -0.13134276, -1.06205273,
        1.07056572,  0.23409911, -1.00032167,  0.54094141, -0.82827541,
        0.        ,  1.04478423,  0.44689326,  0.83739591, -0.165298  ,
       -0.18222167, -0.11556423,  0.13730554, -1.78987991, -0.59188215,
       -0.38421568,  0.69241523,  0.32657381,  0.06755593, -0.10375833,
       -0.50583626, -0.19203944,  0.        ,  0.        ,  0.9518302 ,
        0.02300344,  0.21112834, -0.19107502,  0.09943394, -0.40238463,
       -0.42549055,  0.30052102,  0.62495312, -0.07551696,  0.60399383,
       -0.34648057, -0.07033854,  0.8787781 , -0.96237509, -0.99783873,
        0.94682156,  0.01181251,  0.29838862,  0.09419616,  0.        ,  0.        ]), 'eid': array([[ 1  2  5  6  7  8  9 10], [ 1  2  3  4  5  6  7  8  9 10]], dtype=object), 'n_objects': array([ 8, 10]), '_reg': 0.0018181818181818182, 'mu_': array([ 3.66306486])}
>>>
>>> for u in [1, 3, 5]:
...     for i in [7, 9, 11]:
...         print u, i, recommender.predict((u, i))
...
1 7 4.00074631485
1 9 4.98286035672
1 11 3.44741578214
3 7 3.89716397809
3 9 4.20400627475
3 11 3.66306486366
5 7 3.7468479513
5 9 3.96853184458
5 11 3.60148694779
>>> x = np.array([[1, 7], [1, 9], [1, 11], [3, 7], [3, 9], [3, 11], [5, 7], [5, 9], [5, 11]])
>>> print recommender.predict(x)
[ 4.00074631  4.98286036  3.44741578  3.89716398  4.20400627  3.66306486
  3.74684795  3.96853184  3.60148695]
"""

import sys
import doctest

doctest.testmod()

sys.exit(0)

"""
import numpy as np

from pyrecsys.datasets import *
from pyrecsys.md.latent_factor import EventScorePredictor

np.random.seed(1234)

data = load_movielens_mini()

recommender = EventScorePredictor(C=0.1, k=2)
print vars(recommender)

recommender.fit(data, disp=True, gtol=1e-03)
print vars(recommender)

for u in [1, 3, 5]:
    for i in [7, 9, 11]:
        print u, i, recommender.predict((u, i))

x = np.array([[1, 7], [1, 9], [1, 11], [3, 7], [3, 9], [3, 11], [5, 7], [5, 9], [5, 11]])
print recommender.predict(x)
"""
