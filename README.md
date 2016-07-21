# python_progress

Show progress in console

Using:

```
    max = 1000
    for i in range(max + 1):
        print_progress('ABCDEFGHIJKLMNOPQRSTUVWXYZ.csv (%d)' % i, i,1000)
        time.sleep(0.01)
```

Look like:

```
ABCDEFGHIJKLMNOPQRSTUVWXYZ.csv (1000)           100.00%
```


