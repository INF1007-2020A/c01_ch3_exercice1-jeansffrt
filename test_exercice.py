#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import os
import sys
import unittest

import exercice


class TestExercice(unittest.TestCase):
    def setUp(self) -> None:
        self.numbers = list(range(100))

    def test_square(self) -> None:
        output_exo = list(map(exercice.square, self.numbers))
        outpur_correct = list(map(lambda x: x ** 2, self.numbers))
        
        self.assertListEqual(
            output_exo,
            outpur_correct,
            'Failed to calculate squares'
        )

    def test_square_root(self) -> None:
        output_exo = list(map(exercice.square_root, self.numbers))
        outpur_correct = list(map(lambda x: math.sqrt(x), self.numbers))
        
        self.assertListEqual(
            output_exo,
            outpur_correct,
            'Failed to calculate square roots'
        )


if __name__ == '__main__':
    if not os.path.exists('logs'):
        os.mkdir('logs')
    
    with open('logs/tests_results.txt', 'w') as f:
        loader = unittest.TestLoader()
        suite = loader.loadTestsFromModule(sys.modules[__name__])
        unittest.TextTestRunner(f, verbosity=2).run(suite)
