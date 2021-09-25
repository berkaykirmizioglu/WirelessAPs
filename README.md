# Libs
* bokeh 
* flask
* numpy
* multiprocessing

# WirelessAPs
WirelessAPs

## How to start applications ?

1. First of all, clone https://github.com/berkaykirmizioglu/WirelessAPs.git repository and follow
the **README.md** commands.
2. Go into project directoy (WirelessAPs)
3. In terminal, just type in **order**
````
python3 server.py
````
This command will setup your communcation server.

````
python3 client.py
````
This one is for client should connect to the server.

## Detecting Changes

In the project your access_points.json file is like this;
````
{
   "access_points":[
      {
         "ssid":"MyAP",
         "snr":63,
         "channel":11
      },
      {
         "ssid":"YourAP",
         "snr":42,
         "channel":1
      },
      {
         "ssid":"HisAP",
         "snr":54,
         "channel":6
      }
   ]
}
````
You can change it when applications are running and you are going to see the results like;

````
New connections can be received! ('127.0.0.1', 58530)
Getting Changes...
Getting Changes...
MyAP's SNR changed 63  to  82
YourAP's Channel changed 1  to  6
HerAP is added to the list with SNR 71 and channel 1
````


## Visualize

You can also visualize the JSON file as a bar chart rendered in the GUI.

````
cd flask/
python3 app.py
````

When application starts;

Go to ->
````
http://localhost:8000/graph
````
When you edit **access_points.json** and refresh the page, graphs are interactive.

See the example graph below;
![Image of Visual GUI](https://i.imgur.com/orXJ0mz.png)

