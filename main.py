from scraper import PropertyScraper
if __name__ == "__main__":

    # Documentation for the params dictionary:
    """
    (*) - Required
    (-) - Optional 
    
    * 'propertyFor': Property purpose, should be set to either "sale" or "rent".
    * 'countryId': Country identifier, always set to 1.
    * 'cityId': City identifier Inetger, choose from Riyadh (273), Jeddah(274),Makkah(275),Madinah(276)
    - 'type': Property type, should be set to  "residential" 
    - 'propertyTypeData': Additional property types (multiselect) under residential. Provide as a comma-separated string., Set to None if not specified.
    - 'bedroomsCount': Number of bedrooms (multiselect). Provide as a comma-separated string, choose from 0 to 10., Set to None if not specified.
    - 'bathroomsCount': Number of bathrooms (multiselect). Provide as a comma-separated string, choose from 1 to 9., Set to None if not specified.
    - 'propertyAge': Property age range. Choose from "0_1", "1_3", "3_5", "5_10", "10_100"., Set to None if not specified.
    - 'min_price': 0 to 10,000,000, Set to None if not specified.
    - 'max_price': 0 to 10,000,000, Set to None if not specified.
    - 'min_size': 0 to 5200, Set to None if not specified.
    - 'max_size': 0 to 5200, Set to None if not specified.
    - 'furnishingTypeId': Furnishing type ID. Choose from 5 (Furnished), 6 (Semi Furnished), 7 (Unfurnished). Set to None if not specified.
    """

    params = {
        "propertyFor": 'sale',
        "countryId": 1,
        "cityId": 273,
        "type": 'residential',
        "propertyTypeData": 'floor,building',  # Additional property types
        "bedroomsCount": '3,6,2',  # Number of bedrooms
        "bathroomsCount": '3,6,2',  # Number of bathrooms
        "propertyAge": "1_3",
        "min_price": None,
        "max_price": None,
        "min_size": None,
        "max_size": None,
        "furnishingTypeId": None,
    }

    # Initialize PropertyScraper with search_parameters
    property_scraper = PropertyScraper(**params)

    try:
        # Run the scraper and export data to Excel
        df = property_scraper.run_scraper()
        if df.shape[0] == 0:
            print("No Data")
        else:
            FILENAME = "test"
            df.to_excel(f"{FILENAME}.xlsx", index=False)
            print("Data exported successfully ")

    except Exception as e:
        print(f"Exception {e.__class__} occurred ")
