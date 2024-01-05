# Wasalt Real Estate Data Scraper

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Changing Parameters](#changing-parameters)
  - [Changing the Output Filename](#changing-the-output-filename)
  - [Executing the Code](#executing-the-code)
- [Output Format](#output-format)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Welcome to the **Wasalt Real Estate Data Scraper** project. This repository contains a powerful scraper designed to extract real estate data from the [Wasalt](https://wasalt.com/en) platform in Saudi Arabia. As a prominent real estate platform, Wasalt offers a diverse range of properties, and this scraper streamlines the process of collecting detailed property information, creating a valuable dataset for various applications.

## Features

- Efficiently extracts real estate data from the Wasalt platform.
- Provides a comprehensive dataset including property details, pricing, and location information.
- Facilitates analysis, database creation, and other creative projects using the extracted data.

## Installation

Follow these steps to set up the Wasalt Real Estate Data Scraper:

### Prerequisites

- Python 3.6 or higher
- Install required Python packages:
  - BeautifulSoup4: `pip install beautifulsoup4`
  - Requests: `pip install requests`
  - Playwright: `pip install playwright`
  - Pandas: `pip install pandas`

### Instructions

1. Clone this repository to your local machine using Git:

   ```bash
   git clone https://github.com/adil6572/wasalt-real-estate-scraper.git
   cd wasalt-real-estate-scraper
   ```

2. Install the required Python packages:

   ```bash
   pip install beautifulsoup4 requests playwright pandas
   ```

## Usage

To utilize the Wasalt Real Estate Data Scraper, follow these steps:

### Changing Parameters

1. Open the main file (`main.py`)

#### Customize the Search Parameters as per mention in (`main.py`)

```python
{
        "propertyFor": 'sale',
        "countryId": 1,
        "cityId": 273,
        "type": 'residential',
        "propertyTypeData": 'floor,building',
        "bedroomsCount": '3,6,2',
        "bathroomsCount": '3,6,2',
        "propertyAge": "1_3",
        "min_price": None,
        "max_price": None,
        "min_size": None,
        "max_size": None,
        "furnishingTypeId": None,
    }
```

### Changing the Output Filename

1. Open the scraper file (`main.py`) and update the `params` dictionary with your desired input:

   Replace `'FILENAME="data'` with your preferred filename.

### Executing the Code

1. Run the scraper:

   ```bash
   python main.py
   ```

2. The scraped data will be saved in csv format in the specified output file.

You can now use this data for various purposes, such as analysis, building a real estate database, or any other creative project you have in mind.

## Output Format

The scraped data will be saved in a csv file with items structured as follows (top 30 columns shown out of 50+) :

```json
[
  {
    "Property ID": "123456",
    "Property For": "Sale",
    "Title": "Luxurious Villa with Panoramic Views",
    "Number of Bedrooms": 5,
    "Number of Bathrooms": 6,
    "Built-up Area": "500 sqm",
    "Status Type Slug": "available",
    "Property Main Type": "Villa",
    "Property Sub Type": "Luxury",
    "Furnishing Type": "Furnished",
    "Unit Type": "Independent",
    "Possession Type": "Immediate",
    "Tags": ["Swimming Pool", "Garden", "Smart Home"],
    "Currency Type": "SAR",
    "Conversion Unit": 1.0,
    "Sale Price": 2000000,
    "Conversion Price": 2000000,
    "Currency Type Marker": "SAR",
    "Slug": "luxury-villa-panoramic-views",
    "Age of Listing": 30,
    "Score": 95,
    "Published At": "2023-12-01",
    "Last Update": "2024-01-05",
    "Completion Year": 2022,
    "Managed By": "Property Management Company",
    "Rega Property": true,
    "Longitude": 39.1234,
    "Latitude": 24.5678,
    "Country": "Saudi Arabia",
    "Address": "123 Main Street",
    "City": "Riyadh",
    "Zone": "Luxury Zone",
    "District": "Elite District",
    "Territory": "Central"
  }
]
```

## Contributing

Thank you for considering contributing to the **Wasalt Real Estate Data Scraper** project! Whether it's reporting an issue, suggesting an enhancement, or submitting a pull request, your contributions are highly appreciated.

### Reporting Issues

If you encounter any issues or have suggestions for improvements, please check the [existing issues](https://github.com/adil6572/wasalt-real-estate-scraper/issues) to avoid duplicates. If your issue is not already documented, feel free to [open a new one](https://github.com/adil6572/wasalt-real-estate-scraper/issues/new) with a clear description, including steps to reproduce if applicable.

### Pull Requests

We welcome pull requests that address existing issues or introduce new features. Before submitting a pull request:

1. Fork the repository to your own GitHub account.
2. Clone the forked repository to your local machine.
3. Create a new branch with a descriptive name for your feature or bug fix.
4. Make your changes and commit them.
5. Push your branch to your GitHub repository.
6. Create a pull request to the main repository, explaining your changes and improvements.

Your contributions play a crucial role in improving and maintaining this project. Thank you for being part of the community!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
