#!/usr/bin/python
import matplotlib.pyplot as plt
import numpy as np
import random
import time


def partition_xs(A, x):
  """
  Performs a stable partition of list A into two lists A_l and A_r, such that
  the zero-indices of all tuples in A_l are less than or equal to x and the
  zero-indices of all tuples in A_r are greater than x.

  Inputs:
  - A: A list of tuples to be partitioned.
  - x: An int to partition the zero indices of the tuples around.
  """
  A_l, A_r = [], []
  for A_i in A:
    if A_i[0] <= x:
      A_l.append(A_i)
    else:
      A_r.append(A_i)
  return A_l, A_r


def dist(p1, p2):
  """
  Computes the L2 distance between p1 and p2.

  Inputs:
  - p1: A tuple of length 2 that represents the first point.
  - p2: A tuple of length 2 that represents the second point. 
  """
  p = np.array(p1) - np.array(p2)
  return np.linalg.norm(p, 2)


def min_of_not_nones(*args):
  """
  Returns the minimum value not equal to None.

  Inputs:
  - args: An arbtirary number of numeric and None values.
  """
  return min(d for d in args if d is not None)


def find_closest_pair_for_strip_n(A_strip, d_lr):
  """
  Finds the closest pair in a strip in O(n) since the inner loop executes a
  constant number of times.

  Inputs:
  - A: A list of tuples in the strip for which to find the closest pair.
  - d_lr: An int that represents the smallest distance between points both in
    the left partition or both in the right partition.
  """
  n = len(A_strip)
  d_strip = None
  for i in xrange(n):
    j = i + 1
    while j < n and A_strip[j][1] - A_strip[i][1] < d_lr:
      d = dist(A_strip[i], A_strip[j])
      if d_strip is None or d < d_strip:
        d_strip = d
      j += 1

  return d_strip


def find_closest_pair_n2(A):
  """
  Finds the closest pair using brute force in O(n^2). Returns None for lists of
  length less than 2.

  Inputs:
  - A: A list of tuples for which to find the closest pair.
  """
  n = len(A)
  d_smallest = None
  for i in xrange(n):
    for j in xrange(i+1, n):
      d = dist(A[i], A[j])
      if d_smallest is None or d < d_smallest:
        d_smallest = d
  return d_smallest


def find_closest_pair_nlog2n(A):
  """
  Finds the closest pair using divide and conquer in O(n(logn)^2) since
  T(n) = 2T(n/2) + O(nlogn) => O(n(logn)^2).

  Inputs:
  - A: A list of tuples for which to find the closest pair.
  """
  if len(A) <= 3:
    return find_closest_pair_n2(A)

  mx = np.median(A, axis=0)[0]  # median of x's; O(n) next Monday
  A_l, A_r = partition_xs(A, mx)

  d_l = find_closest_pair_nlog2n(A_l)  # includes median if len(A) is odd
  d_r = find_closest_pair_nlog2n(A_r)

  d_lr = min_of_not_nones(d_l, d_r)
  
  A_strip = filter(lambda A_i: abs(A_i[0] - mx) < d_lr, A)  # filter is stable

  A_strip.sort(key=lambda A_strip_i: A_strip_i[1])  # O(nlogn)

  d_strip = find_closest_pair_for_strip_n(A_strip, d_lr)
  return min_of_not_nones(d_lr, d_strip)


def find_closest_pair_nlogn_helper(A):
  """
  Helper to find the closest pair using divide and conquer in O(nlogn) since
  T(n) = 2T(n/2) + O(n) => O(nlogn).

  Inputs:
  - A: A list of tuples for which to find the closest pair, with y values
    sorted in ascending order.
  """
  if len(A) <= 3:
    return find_closest_pair_n2(A)

  mx = np.median(A, axis=0)[0]  # median of x's
  A_l, A_r = partition_xs(A, mx)

  d_l = find_closest_pair_nlogn_helper(A_l)  # includes median if len(A) is odd
  d_r = find_closest_pair_nlogn_helper(A_r)

  d_lr = min(d_l, d_r)
  
  A_strip = filter(lambda A_i: abs(A_i[0] - mx) < d_lr, A)  # filter is stable

  # Not necessary: A_strip.sort(key=lambda A_strip_i: A_strip_i[1])

  d_strip = find_closest_pair_for_strip_n(A_strip, d_lr)
  return min_of_not_nones(d_lr, d_strip)


def find_closest_pair_nlogn(A):
  """
  Finds the closest pair using divide and conquer in O(nlogn) since
  T(n) = 2T(n/2) + O(n) => O(nlogn).

  Inputs:
  - A: A list of tuples for which to find the closest pair.
  """
  A = sorted(A, key=lambda A_i: A_i[1])
  return find_closest_pair_nlogn_helper(A)


def simulate():
  n2s = []
  nlog2ns = []
  nlogns = []

  ns = list(xrange(100, 500, 100))

  for n in ns:
    A = [(random.random(), random.random()) for i in xrange(n)]

    a = time.time()
    find_closest_pair_n2(A)
    b = time.time()
    find_closest_pair_nlog2n(A)
    c = time.time()
    find_closest_pair_nlogn(A)
    d = time.time()
    
    n2s.append(b - a)
    nlog2ns.append(c - b)
    nlogns.append(d - c)
    
    print "[n=%04d] n^2: %.4fs, n(logn)^2: %.4fs, nlogn: %.4fs" % (
      n, b - a, c - b, d - c,
    )

  plt.plot(ns, n2s, 'r--', ns, nlog2ns, 'g--', ns, nlogns, 'b--')
  plt.show()

def main():
  # simulate()  # uncomment to time these functions!
  pass

if __name__ == "__main__":
  main()
