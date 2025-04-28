# T-systems

This guide explains how to use the `api_scripts` and `custom_scripts` provided in this repository to interact with your running NetBox Docker instance.

## Prerequisites

1. A running NetBox Docker instance.
2. A superuser account in your NetBox instance.
3. Python 3 installed on your local machine.

## Setup
1. Ensure necessary Python libraries are installed.

    ```bash
    pip install -r requirements.txt
    ```

2. Create an ```.env``` file in the root directory of your project to  store your API key. Ensure your ```.env``` file is configured with the correct API token. Replace ```your-40-character-api-token``` with a valid API token from your NetBox instance.
    ```bash
    NETBOX_API_TOKEN=your-40-character-api-token
    ```
    You can find an ```.env``` example inside the ```setup/``` folder.

3. Load ```initial_data.yaml``` into your NetBox instance.

## API Scripts

The ```api_scripts/``` folder contains Python scripts that interact with the NetBox API. Below is an example of how to use the ```count_sites.py``` script.

### count_sites.py
This script retrieves and counts sites in your NetBox instance based on their status (e.g., active or planned).

**Steps to Use:**
1. Navigate to the ```api_scripts/``` directory:
    ```bash
    cd /path/to/api_scripts
    ```

2. Run the script with the desired site status as an argument:
    ```bash
    python3 count_sites.py <status>
    ```

3. Replace ```<status>``` with either ```active``` or ```planned```. The script will output the number of sites with the specified status and their details.
    ```bash
    python3 count_sites.py active
    ```

## Custom Scripts
The ```custom_scripts/``` folder contains scripts that can be executed directly within the **NetBox UI**.

**Steps to Use:**
1. Log in to your NetBox instance as a superuser.
2. Navigate to ```/extras/scripts/add``` in the NetBox UI.
3. Upload the ```filter_sites.py```file from the ```custom_scripts/``` folder.
4. Navigate to ```/extras/scripts/```, you should see the custom script listed. Select the script, fill in any required parameters, and execute it.


## Summary
- Use ```api_scripts/``` for command-line interactions with the NetBox API.
- Use ```custom_scripts/``` for executing scripts directly within the NetBox UI.

