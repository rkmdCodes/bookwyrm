# fedireads

Social reading and reviewing, decentralized with ActivityPub

## Setting up the developer environment
You will need postgres installed and running on your computer.

``` bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
createdb fedireads
```

Create the psql user in `psql fedireads`:
``` psql
CREATE ROLE fedireads WITH LOGIN PASSWORD 'fedireads';
GRANT ALL PRIVILEGES ON DATABASE fedireads TO fedireads;
```

Initialize the database
``` bash
./rebuilddb.sh
```
This creates two users, `mouse@your-domain.com` with password `password123` and `rat@your-domain.com` with password `ratword`.

And go to the app at localhost:8000

For most testing, you'll want to use ngrok. Remember to set the DOMAIN in settings.py to your ngrok domain.


## Structure

All the url routing is in `fedireads/urls.py`. This includes the application views (your home page, user page, book page, etc),
application endpoints (things that happen when you click buttons), and federation api endpoints (inboxes, outboxes, webfinger, etc).

The application views and actions are in `fedireads/views.py`. The internal actions call api handlers which deal with federating content.
Outgoing messages (any action done by a user that is federated out), as well as outboxes, live in `fedireads/outgoing.py`, and all handlers for incoming
messages, as well as inboxes and webfinger, live in `fedireads/incoming.py`. Misc api functions live in `fedireads/api.py`, which is
probably not a good name for that file.

Connection to openlibrary.org to get book data is handled in `fedireads/openlibrary.py`.