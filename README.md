```
            .                         
            |       o                 
;-. . .     |-  ;-. . ,-: ,-: ,-. ;-. 
| | | |     |   |   | | | | | |-' |   
|-' `-|     `-' '   ' `-| `-| `-' '   
'   `-' ---           `-' `-'         
```

A ros2 module to publish the state of a pin.

## Setup

The pin, the topic and the polling time an be configured with the following parameters:

        trigger_pin (default: 'D4')
        trigger_topic (default: 'trigger')       
        polling_time (default: 0.5)

## Dependencies
 
  - Adafruit Blinka
  - CiruitPython

## Supported Boards

Tested on jetson nano, but should work on all boards supported by Blinka + ROS2.
