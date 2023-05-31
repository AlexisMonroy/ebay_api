import os
import xml.etree.ElementTree as ET

def extract_shipping_details(xml_string):
    # Parse the XML string
    root = ET.fromstring(xml_string)

    # Get the parent directory of the current directory
    #parent_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))

    # Open the output file for writing
    #output_file_path = os.path.join(parent_dir, 'resp_output', 'shipping_details.txt')
    with open('resp_output/shipping_details.txt', 'w') as f:
        # Iterate over all ShippingServiceDetails tags and extract the relevant data for each one
        for shipping_service_details in root.findall('.//{urn:ebay:apis:eBLBaseComponents}ShippingServiceDetails'):
            shipping_service = shipping_service_details.find('.//{urn:ebay:apis:eBLBaseComponents}ShippingService').text
            shipping_service_id = shipping_service_details.find('.//{urn:ebay:apis:eBLBaseComponents}ShippingServiceID').text
            #shipping_time_min = shipping_service_details.find('.//{urn:ebay:apis:eBLBaseComponents}ShippingTimeMin').text
            #shipping_time_max = shipping_service_details.find('.//{urn:ebay:apis:eBLBaseComponents}ShippingTimeMax').text
            service_types = [elem.text for elem in shipping_service_details.findall('.//{urn:ebay:apis:eBLBaseComponents}ServiceType')]
            shipping_packages = [elem.text for elem in shipping_service_details.findall('.//{urn:ebay:apis:eBLBaseComponents}ShippingPackage')]
            valid_for_selling_flow = shipping_service_details.find('.//{urn:ebay:apis:eBLBaseComponents}ValidForSellingFlow').text
            detail_version = shipping_service_details.find('.//{urn:ebay:apis:eBLBaseComponents}DetailVersion').text
            update_time = shipping_service_details.find('.//{urn:ebay:apis:eBLBaseComponents}UpdateTime').text
            shipping_category = shipping_service_details.find('.//{urn:ebay:apis:eBLBaseComponents}ShippingCategory').text

            # Write the extracted data for each ShippingServiceDetails tag to the output file
            f.write(f'Shipping Service: {shipping_service}\n')
            f.write(f'Shipping Service ID: {shipping_service_id}\n')
            #f.write(f'Shipping Time Min: {shipping_time_min}\n')
            #f.write(f'Shipping Time Max: {shipping_time_max}\n')
            f.write(f'Service Types: {service_types}\n')
            f.write(f'Shipping Packages: {shipping_packages}\n')
            f.write(f'Valid For Selling Flow: {valid_for_selling_flow}\n')
            f.write(f'Detail Version: {detail_version}\n')
            f.write(f'Update Time: {update_time}\n')
            f.write(f'Shipping Category: {shipping_category}\n')
            f.write('---\n')