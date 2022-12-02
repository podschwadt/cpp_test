"""
Implement the rest of Matrix class. Do not use any other modules than `ctypes`.
The matrix class needs to support the following operators:
  + for element wise addition
  * for element wise multiplication
  @ for matrix multiplication
  == for testing equality

The actual addition, multiplication, and matrix multplication must be performed 
in C++. You need to use the `ctypes` module to transfere the data between Python
and C++. (See the README.MD and interface.h files).

For the element wise operattions you only need to handle matrices that have
the same dimensions, for matrix multiplication the dimensions must be 
compitable. Have the code fail appropriately if these requriements are not met.

In the main block of this file you can find some test code that you can use to 
test your implementation. Beware, these tests do not cover all cases.

"""
import cytpes


class Matrix(object):

  def __init__(self, values) -> None:
    raise RuntimeError('you need to implement me')


# test code below. do no modify
if __name__ == '__main__':
  A = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
  B = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

  # test addition
  C = A + B
  add_result = Matrix([[10, 10, 10], [10, 10, 10], [10, 10, 10]])
  if C == add_result:
    print('Addition works')
  else:
    raise RuntimeWarning('Addition does not work')

  # test multiplication
  C = A * B
  mul_result = Matrix([[9, 16, 21], [24, 25, 24], [21, 16, 9]])
  if C == mul_result:
    print('Multiplication works')
  else:
    raise RuntimeWarning('Multiplication does not work')

  # test matrix multiplication
  C = A @ B
  matmul_result_0 = Matrix([[30, 24, 18], [84, 69, 54], [138, 114, 90]])

  # another test
  D = Matrix([[0.9, 0.8], [0.7, 0.6], [0.5, 0.4]])
  E = A @ D

  matmul_result_1 = Matrix([[3.8, 3.2], [10.1, 8.6], [16.4, 14.]])

  if C == matmul_result_0 and E == matmul_result_1:
    print(' Matrix Multiplication works')
  else:
    raise RuntimeWarning('Multiplication does not work')
