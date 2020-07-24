# How to upgrade PyDAL

Sometimes you're told in places like the [py4web group](https://groups.google.com/forum/#!forum/py4web) to upgrade PyDAL. Try this first:

```bash
:: -m pip means run the module named pip
:: -U pydal means update the PyDAL package
python3 -m pip install -U pydal
```

If that doesn't work, you may need to uninstall previous version explicitly, or install for a particular version of Python itself. If so, read on.

## If you need to uninstall a previous version of PyDAL

You may need to remove earlier versions of PyDAL. If so, see [How to uninstall PyDAL](https://github.com/tomcam/py4webcasts/blob/master/docs/how-to-uninstall-pydal)

## How to install PyDAL for a particular version of Python

You can install PyDAL for a particular version of Python. For example, if it's Python 3.8, use `pip` as expected:

```
python3.8 -m pip install -U pydal
```
