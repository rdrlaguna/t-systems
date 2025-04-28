import argparse
import logging
import requests
import os
import sys

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


def main():

    # Command-line argument parser
    parser = argparse.ArgumentParser(
        description="Get sites with a specific status."
    )
    #parser.add_argument("token", help="NetBox API token")
    parser.add_argument("status", help="Site status (e.g. planned, active)")

    args = parser.parse_args()

    # Set log messages level
    logging.basicConfig(level=logging.INFO)

    # Get the API token from environment variable
    token = os.getenv("NETBOX_API_TOKEN")

    # Validate token
    if (len(token) != 40 or token.isdigit() or token.isalpha()):
        logging.error("Token must have 40 alphanumeric characters.")
        sys.exit(1)


    # Validate status
    if args.status not in ['active', 'planned']:
        logging.error("Invalid status.")
        sys.exit(1)

    # Get sites matching provided status
    results = get_sites(token, args.status)

    if results:
        print(f"\nThere are {len(results)} {args.status} sites:")
        for site in results:
            print(f"{site.get('id')} {site.get('name')} (address: {site.get('physical_address')})")
    else:
        logging.info("No sites found with the specified status.")


def get_sites(token, status):
    """
    Get sites with specific status from Netbox API.
    """
    # Request information
    url = "http://localhost:8000/api/dcim/sites/"
    headers = {
        "Authorization": f"Token {token}",
        "Content-Type": "application/json",
        "Accept": "application/json; indent=4"
    }
    params = {"status": status}

    # Handle requests exception
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        return data.get('results', [])

    except requests.exceptions.RequestException as e:
        logging.error(f"API request failed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
