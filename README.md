# CourseProject

NVK Final Project:

Presentation Video: 

Presentation Slides + Demo Youtube Video: https://docs.google.com/presentation/d/1x7FOVrt9H3-FKMX1jjnYv_hquu2TYZrSphNrxLxyx3E/edit?usp=sharing

## How to run
1. Open the `Python` folder and run the `pip install -r requirements.txt` command in console to install the dependencies. We ran a conda environment in Python 3.8 and 3.9 and can't gurantee that functionality with other versions.
2. Start the app as a flask server from the `app.py` file. Use the `python -m flask run` command.
3. Open the `js-ui` folder and run the `npm install` command to install dependencies. 
4. After the dependencies are installed run the `npm start` command to open the UI app.
5. After a while the window with `localhost:3000` will open in browser. You can start using the app.

## Video of how to run

Link: https://youtu.be/y1uNM5kK2cg

## Alternative way to test
Since the app is created as an API it can be tested by just making a request to it through browser in the following format: `http://127.0.0.1:5000/api/keywords/<google_place_id>`. Example: `http://127.0.0.1:5000/api/keywords/ChIJ4Vrk3Bo3DogRpHfXxy0yu98`. You can find Google Place Ids on the following page https://developers.google.com/maps/documentation/places/web-service/place-id.
