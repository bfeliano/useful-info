### Project Configuration

Download the readme.md, requirements.txt and monit.py to an empty directory. Open terminal from this directory and follow the steps below.

1. Creation of virtual environment

```
python3 -m venv venv
```

2. Activating venv on Linux

```
source ./venv/bin/activate
 ```

3. With venv activated, install the dependencies. 

```
pip install -r requirements.txt
```
(This will install the dependencies needed to run the application. This command is only needed the first time that you are running it.)


4. Run the application

```
python3 monit.py queuename*
```

(Replace queuename* with the name of the queue that you are monitoring.)