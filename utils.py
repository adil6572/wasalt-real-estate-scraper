# constant and mappings

column_mapping = {
    'arMessageBody': 'Arabic Message Body',
    'ownerName': 'Owner Name',
    'arMessageTitle': 'Arabic Message Title',
    'enMessageTitle': 'English Message Title',
    'enMessageBody': 'English Message Body',
    'price': 'Sale Price',
    'count': 'Sale Count',
    'total': 'Total Units',
    'available': 'Available Units',
    'isVerified': 'Verified',
    'isRegaProp': 'Rega Property',
    'carpetAreaMin': 'Minimum Carpet Area',
    'createdAt': 'Creation Date',
    'id': 'Property ID',
    'updatedAt': 'Last Update',
    'enBrandName': 'English Brand Name',
    'micRedir': 'Mic Redirection',
    'arCmpName': 'Arabic Company Name',
    'phoneNumberCountryCode': 'Phone Number Country Code',
    'absherverified': 'Absher Verified',
    'arFirstName': 'Arabic First Name',
    'enFirstName': 'English First Name',
    'whatsAppNumberCountryCode': 'WhatsApp Number Country Code',
    'licenseNumber': 'License Number',
    'crownIco': 'Crown Icon',
    'enCmpName': 'English Company Name',
    'enFamilyName': 'English Family Name',
    'arBrandName': 'Arabic Brand Name',
    'arSellerName': 'Arabic Seller Name',
    'enFatherName': 'English Father Name',
    'whatsApp': 'WhatsApp',
    'referenceNo': 'Reference Number',
    'roleId': 'Role ID',
    'arFatherName': 'Arabic Father Name',
    'roleNameAr': 'Role Name (Arabic)',
    'cmpLogoUrl': 'Company Logo URL',
    'arFamilyName': 'Arabic Family Name',
    'roleNameEn': 'Role Name (English)',
    'phone': 'Phone',
    'isQuara': 'Is Quara',
    'contactName': 'Contact Name',
    'wafiNo': 'Wafi Number',
    'enSellerName': 'English Seller Name',
    'fullName': 'Full Name',
    'regaId': 'Rega ID',
    'labels': 'Labels',
    'masterPlanArea': 'Master Plan Area',
    'propIdentityTypeId': 'Property Identity Type ID',
    'packageScore': 'Package Score',
    'subsPkg': 'Subscribed Packages',
    'completionDate': 'Completion Date',
    'lon': 'Longitude',
    'lat': 'Latitude',
    'images': 'Images',
    'authorization_letter': 'Authorization Letter',
    'developer_logo': 'Developer Logo',
    'wafiFiles': 'Wafi Files',
    'attributes': 'Attributes',
    'carpetAreaMax': 'Maximum Carpet Area',
    'pinTextColor': 'Pin Text Color',
    'logo': 'Developer Logo',
    'developerId': 'Developer ID',
    'pinBgColor': 'Pin Background Color',
    'developerName': 'Developer Name',
    'unitTypes': 'Unit Types',
    'currencyType': 'Currency Type',
    'country': 'Country',
    'address': 'Address',
    'city': 'City',
    'zone': 'Zone',
    'district': 'District',
    'propertyFor': 'Property For',
    'slug': 'Slug',
    'title': 'Title',
    'description': 'Description',
    'tags': 'Tags',
    'salePriceMin': 'Minimum Sale Price',
    'salePriceMax': 'Maximum Sale Price',
    'districtId': 'District ID',
    'cityId': 'City ID',
    'conversionPriceMin': 'Minimum Conversion Price',
    'conversionPriceMax': 'Maximum Conversion Price',
    'conversionUnit': 'Conversion Unit',
    'currencyTypeMarker': 'Currency Type Marker',
    'currencyTypeId': 'Currency Type ID',
    'propertyRegionId': 'Property Region ID',
    'managedById': 'Managed By ID',
    'zoneId': 'Zone ID',
    'ageOfListing': 'Age of Listing',
    'noOfBedrooms': 'Number of Bedrooms',
    'noOfBathrooms': 'Number of Bathrooms',
    'noOfLivingrooms': 'Number of Living Rooms',
    'noOfGuestrooms': 'Number of Guest Rooms',
    'userAvatar': 'User Avatar',
    'companyName': 'Company Name',
    'regaAdvLicNo': 'Rega Advertising License Number',
    'enName': 'English Name',
    'email': 'Email',
    'companyLogo': 'Company Logo',
    'arName': 'Arabic Name',
    'regaAuthorizationNumber': 'Rega Authorization Number',
    'enUserRole': 'English User Role',
    'arUserRole': 'Arabic User Role',
    'postedAs': 'Posted As',
    'regaAdvertiserNumber': 'Rega Advertiser Number',
    'crNo': 'CR Number',
    'brandName': 'Brand Name',
    'isUpdated': 'Is Updated',
    'score': 'Score',
    'reservation': 'Reservation',
    'publishedAt': 'Published At',
    'fullDarReference': 'Full DAR Reference',
    'darReference': 'DAR Reference',
    'brochure': 'Brochure',
    'floorPlans': 'Floor Plans',
    'propertyMainType': 'Property Main Type',
    'propertySubType': 'Property Sub Type',
    'furnishingType': 'Furnishing Type',
    'unitType': 'Unit Type',
    'possessionType': 'Possession Type',
    'managedBy': 'Managed By',
    'territory': 'Territory',
    'salePrice': 'Sale Price',
    'expectedRent': 'Expected Rent',
    'conversionPrice': 'Conversion Price',
    'statusTypeId': 'Status Type ID',
    'statusTypeSlug': 'Status Type Slug',
    'territoryId': 'Territory ID',
    'propertySubTypeSlug': 'Property Sub Type Slug',
    'carpetArea': 'Carpet Area',
    'completionYear': 'Completion Year',
    'builtUpArea': 'Built-up Area',
    'showMasterPlanCardTag': 'Show Master Plan Card Tag',
    'isFeatured': 'Is Featured',
}


# List name categories
property_columns = ['Property ID', 'Property For', 'Title', 'Number of Bedrooms', 'Number of Bathrooms', 'Number of Living Rooms', 'Number of Guest Rooms', 'Minimum Carpet Area', 'Maximum Carpet Area', 'Built-up Area', "Master Plan Area",  'Status Type Slug', 'Carpet Area', 'Property Main Type', 'Property Sub Type', 'Furnishing Type', 'Unit Type', 'Possession Type',
                    'Tags', 'Currency Type', 'Minimum Sale Price', 'Maximum Sale Price', 'Minimum Conversion Price', 'Price', 'Maximum Conversion Price', 'Conversion Unit', 'Sale Price', 'Conversion Price', 'Currency Type Marker', 'Slug', 'Age of Listing', 'Score', 'Published At',  'Last Update', 'Completion Year', 'Managed By', 'Rega Property', 'License Number',]

contact_columns = ['Owner Name', 'Arabic Seller Name', 'name', 'Full Name', 'Package Score',
                   'Currency Type Marker', 'Phone Number Country Code', 'Phone', 'WhatsApp', 'Email', 'English User Role', 'Arabic User Role', 'CR Number',]

location_columns = ['Longitude', 'Latitude', 'Country', 'Address', 'City', 'Zone', 'District',
                    'District ID', 'City ID', 'Territory', 'Property Region ID', 'Zone ID', 'District ID', 'City ID']

selected_columns = property_columns+location_columns+contact_columns