# Gmaps_pathfinder

Gmaps_pathfinder is a Python project that allows you to find the shortest path between two locations using the Google Maps API. The project uses the `googlemaps` library to interact with the API and retrieve information about the route.

## Installation

To use Gmaps_pathfinder, you'll need to have Python 3 installed on your computer. You'll also need to install the `googlemaps` library, which can be done using pip:

```
pip install googlemaps
```

Once you have Python and `googlemaps` installed, you can clone the Gmaps_pathfinder repository to your local machine:

```
git clone https://github.com/Zciwolvo/Gmaps_pathfinder.git
```

## Usage

To use Gmaps_pathfinder, you'll need to have a Google Maps API key. You can obtain a key by following the instructions on the [Google Maps Platform website](https://developers.google.com/maps/gmp-get-started#create-project).

Once you have an API key, you can run the `main.py` file and enter the starting and ending locations:

```
python main.py
```

The program will use the Google Maps API to find the shortest path between the two locations and display the distance and estimated travel time.

## Customization

If you want to customize the behavior of the program, you can modify the code in the `pathfinder.py` file. You can adjust the parameters of the `googlemaps` API calls to retrieve additional information about the route, such as the directions or the traffic conditions.

## Contributing

If you'd like to contribute to the Gmaps_pathfinder project, feel free to submit a pull request with your changes. We welcome contributions from the community and are always looking for ways to improve the project.

## License

Gmaps_pathfinder is licensed under the MIT License. See the `LICENSE` file for more information.
