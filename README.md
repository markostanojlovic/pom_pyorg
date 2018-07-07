# Usage info

### Running test in parallel/concurrent/multiprocess

1. With concurrency test module 
```python
from concurrencytest import ConcurrentTestSuite, fork_for_tests
if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    suite = suite()
    concurrent_suite = ConcurrentTestSuite(suite, fork_for_tests(3))
    runner.run(concurrent_suite)
```
then to run suite: 
```python
python suite_file_name.py -v 
```

* it's faster if used local webdrier, compared to remote selenium server and grid

2. With pytest-xdist module
```python
pytest suite_file_name.py -v -n 3 # where 3 is the num of processes
```

