# SimpleSplashScreen

## Overview
SimpleSplashScreen displays a splash screen while your program is loading, with a minimalistic progress bar and the ability to use a custom (transparent or not) image.

## Usage
To use SplashScreen in your project, follow these steps:

1. Copy the `SimpleSplashScreen` folder to your project folder

2. In your main.py file, import the class from the module:
    ```python
    from SimpleSplashScreen import SplashScreen
    ```
3. Initialize the splash screen with your desired image:
    ```python
    splash = SplashScreen("path_to/image.png")
    ```
4. Update the percentage for the progressbar:
    ```python
    splash.update_progress(simulated_percentage_done)
    ```

You can either update it periodically using a loop or update it whenever the percentage value in your program changes.

**The splash screen will automatically close once the progress percentage reaches 100%**

You can also check and execute main.py to see it in action.

## See the license [here](LICENSE)
