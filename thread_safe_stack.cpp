include thread_safe_stack.hpp


template<class t>
class Stack<T> {

  size_t size;
  vector<T> storage;

  // constructor
  // destructor
  // # rule of 3


  void _lock();
  void _unlock();
  
  public:
  void push();
  void pop();
  size_t size();
  T front();
};



/*
 * Should locks be built into the data structures?
 * Should we ever use dynamic memory allocation other than for the basest primitives?
 *
 * If the data structure is not thread safe, then we have to wrap the thread safety around the data structure in the application code
 * we will need many lines of code for managing a 1:1 binding of a lock to a data structure and then passing / waiting / lock/unlocking 
 * - this has the overhead of having to write code
 *
 *
 * How do we manage our memory usage thorugh unique_ptr and shared_ptr?
 * Should I be attempting this in c++? This language is massively more complex and it would not be good to overload myself
 */
