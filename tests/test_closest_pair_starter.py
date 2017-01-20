from closest_pair_starter import find_closest_pair_nlogn


def test_closest_pair():
  tests = [
    ([(0, 0), (1, 0)], 1),
  ]

  for test in tests:
    A, d_opt = test
    d = find_closest_pair_nlogn(A)
    assert d == d_opt
