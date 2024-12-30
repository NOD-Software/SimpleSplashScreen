# SimpleSplashScreen

## Overview
SimpleSplashScreen displays a splash screen while your program is loading, with a minimalistic progress bar and the ability to use a custom (transparent or not) image.

## Usage
To use SplashScreen in your project, follow these steps:

1. Import the class from the module:
    ```python
    from SimpleSplashScreen import SplashScreen
    ```
2. Initialize the splash screen with your desired image:
    ```python
    splash = SplashScreen("path_to/image.png")
    ```
3. Update the percentage for the progressbar:
    ```python
    splash.update_progress(simulated_percentage_done)
    ```
**The splash screen will automatically close once the progress percentage reaches 100%**

You can also check and execute main.py to see the module in action.

### See the license [here](LICENSE)