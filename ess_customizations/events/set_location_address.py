import frappe
import requests

def set_location_address(doc, methods):
    try:
        if doc.location:
            doc.custom_log_location = get_address_from_location(doc.location)
            doc.save()
    except Exception:
        frappe.log_error(
            title="Failed to fetch location address", message=frappe.get_traceback()
        )


def get_address_from_location(location):
    """
    Fetch the address from latitude and longitude using OpenStreetMap's Nominatim API.

    :param location: A string in "latitude,longitude" format
    :return: Address as a string or an error message
    """

    # Validate input
    if not location or "," not in location:
        frappe.throw(_("Invalid location format. Use 'latitude,longitude'."))

    # Extract latitude and longitude from the string
    lat, lon = location.split(",")
    lat, lon = lat.strip(), lon.strip()

    # Construct the API request
    url = f"https://nominatim.openstreetmap.org/reverse?lat={lat}&lon={lon}&format=json"
    response = requests.get(url, headers={"User-Agent": "Frappe-App"})

    # Handle response
    if response.status_code == 200:
        data = response.json()
        address = data.get("display_name", "")
        return address
    else:
        frappe.throw(_("Error Fetching Address"))