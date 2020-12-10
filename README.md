# entsocwash

Navigate to the directory where you want to install the repo:

    cd your/file/path/here

Next, create a virtual environment (if you haven't already) and activate it

    python3 -m venv myvenv
    source myvenv/bin/activate

Initialize git and clone this repository

    git init
    git clone https://github.com/Meganmccarty/entsocwash.git

Navigate down one level to the folder containing the manage.py file:

    cd entsocwash

Install dependencies

    pip install -r requirements.txt

Then run the following commands:

    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver

The website should now be accessible via your browser on localhost:8000 or 127.0.0.1:8000
