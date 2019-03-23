# Raspi-Power
## What is this?
This circuit keeps power supply to a raspberry pi for a second after the main power is down to shut down safely.. The functionalities are almost same as a UPS, but this is specialized to mount a car. This is useful for broadcasting your driving scenary, for example.

## How it works?
A car has two (strictly three) outlets: direct to battery and ACC. After you turn off an engine, ACC also turns off. This circuit detects that, and keep the power from battery directly while the raspberry pi is shutting down.

## Environment
- [kicad](http://kicad-pcb.org/) to see this circuit

## Misc
- A OKL\_T footprint thanks to (stm32f1/stm32-board)[https://github.com/stm32f1/stm32_board]
