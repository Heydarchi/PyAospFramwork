# PyAospFramework

PyAospFramwork aims to facilitate testing the application, services, etc. in Android powered devices. The target devices could be an Android mobile or an Infotainment system. Regardless of the target it provides the required functionalities to communicate through ADB and run the required tasks and commands. 

## Requirements

The following packages must be installed before using the framework:

- **Python 3.x** and **pip** installed on your system.

```
sudo apt update
sudo apt install -y python3.11 python3-pip
```


- **ADB** installed and configured on your system. 



## Installation and Setup

Follow these steps to set up the project on your local machine:


```
chmod +x setup_venv.sh
./setup_venv.sh
```

## Run the tests

```
source venv/bin/activate
python tests
```