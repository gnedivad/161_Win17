import math
from closest_pair import (
  find_closest_pair_n2,
  find_closest_pair_nlog2n,
  find_closest_pair_nlogn,
)


def test_closest_pair_n2():
  tests = [
    ([(0, 0), (1, 0)], 1),
    ([(0, 0), (2, 0), (1, 1)], math.sqrt(2)),
    ([(0, 0), (1, 1), (2, 1), (3, 0)], 1),
    ([(0, 0), (2, 2), (2, 4), (3, 5), (4, 5), (3, 4), (3, 2), (5, 0)], 1),
  ]

  for test in tests:
    A, d_opt = test
    d = find_closest_pair_n2(A)
    assert d == d_opt


def test_closest_pair_nlog2n():
  tests = [
    ([(0, 0), (1, 0)], 1),
    ([(0, 0), (2, 0), (1, 1)], math.sqrt(2)),
    ([(0, 0), (1, 1), (2, 1), (3, 0)], 1),
    ([(0, 0), (2, 2), (2, 4), (3, 5), (4, 5), (3, 4), (3, 2), (5, 0)], 1),
  ]

  for test in tests:
    A, d_opt = test
    d = find_closest_pair_nlog2n(A)
    assert d == d_opt


def test_closest_pair_nlogn():
  tests = [
    ([(0, 0), (1, 0)], 1),
    ([(0, 0), (2, 0), (1, 1)], math.sqrt(2)),
    ([(0, 0), (1, 1), (2, 1), (3, 0)], 1),
    ([(0, 0), (2, 2), (2, 4), (3, 5), (4, 5), (3, 4), (3, 2), (5, 0)], 1),
  ]

  for test in tests:
    A, d_opt = test
    d = find_closest_pair_nlogn(A)
    assert d == d_opt
