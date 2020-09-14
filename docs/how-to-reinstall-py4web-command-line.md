# How to Reinstall py4web from the command line

## TODO
* Separate page: How to install git
* Separate page: How to install python3 
* Separate page: How to install pip (PIP is automatically installed with Python 2.7. 9+ and Python 3.4+)

```
git clone https://github.com/web2py/py4web.git
cd py4web
python3 -m pip install -r requirements.txt
./py4web.py setup apps
./py4web.py set-password
./py4web.py run apps
```
