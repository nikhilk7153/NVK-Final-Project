# CourseProject

NVK Final Project:

Presentation Video: https://youtu.be/5mnNC3_LPJc

## How to run
0. Clone this repository locally
1. Install Conda v4.10.3 or better. Create conda environment `conda create --name test python=3.9`
2. Activate conda environment `conda activate test`
3. Open the `Python` folder and run the `pip install -r requirements.txt` command in console to install the dependencies. We ran a conda environment in Python 3.8 and 3.9 and can't gurantee that functionality with other versions.
4. Start the app as a flask server from the `app.py` file. Use the `python -m flask run` command.
5. Open the `js-ui` folder and run the `npm install` command to install dependencies. 
6. After the dependencies are installed run the `npm start` command to open the UI app.
7. After a while the window with `localhost:3000` will open in browser. You can start using the app.

## Alternative way to test
Since the app is created as an API it can be tested by just making a request to it through browser in the following format: `http://127.0.0.1:5000/api/keywords/<google_place_id>`. Example: `http://127.0.0.1:5000/api/keywords/ChIJ4Vrk3Bo3DogRpHfXxy0yu98`. You can find Google Place Ids on the following page https://developers.google.com/maps/documentation/places/web-service/place-id.
