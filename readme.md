# Karma Farmer
Generates karma for user running script by participating in r/KarmaStreet, where this script uploads a post for a user and upvotes other active users. This is kinda a side project for me but there is some more work to do before its a final project, so if it gains traction ill go back to it but for now this is it. 

### Python Installation
Linux:
```sh
sudo apt install python3
python3 -m pip install KarmaFarmer
```
Windows:
Install latest stable python3.+ release from https://www.python.org/downloads/windows/.
Open a terminal and type:
```sh
python -m pip install KarmaFarmer
```
Create a python file called script-name.py:
```python
import KarmaFarmer
import praw
r = praw.Reddit(client_id='client-id-example', client_secret='client-secret-example', user_agent='karmafarmer', username='JohnSmith', password='password123')
KarmaFarmer.Network(r)
```
(Make sure to change all fields for praw).

### Running
For linux:
```sh
python3 script-name.py
```
For windows:
```sh
python script-name.py
```
