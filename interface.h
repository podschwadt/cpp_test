#ifndef TEST_INTERFACE_H
#define TEST_INTERFACE_H

namespace my_namespace {

/*
 * This class represents the arithemtic interface a C++ matrix supports.
 * You need to create a subclass the inherits from `Interface` and implement the
 * pure virtual functions.
 */
class Interface {
 public:
  // Element-wise addition. Returns a new object holding the result.
  virtual Interface* add(const Interface* other) const = 0;
  // Element-wise multiplication. Returns a new object holding the result.
  virtual Interface* multiply(const Interface* other) const = 0;
  // Matrix multiplication. Returns a new object holding the result
  virtual Interface* matrixMultiply(const Interface* other) const = 0;
}

}  // namespace my_namespace

#endif /* TEST_INTERFACE_H */
