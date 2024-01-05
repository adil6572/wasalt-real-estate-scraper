import json
import requests
from bs4 import BeautifulSoup
import math
from page import ExtractContent
from playwright.sync_api import Playwright, sync_playwright
from clean import clean_data


class PropertyScraper:
    def __init__(self, propertyFor="sale", countryId=None, cityId=None, type="residential",
                 propertyTypeData=None, bedroomsCount=None, min_price=None, max_price=None, bathroomsCount=None,
                 propertyAge=None, furnishingTypeId=None, min_size=None, max_size=None, pageSize=100):

        self.browser = ExtractContent(sync_playwright(),headless=False)

        self.base_url = "https://wasalt.com/en/sale/search"
        self.pageSize = pageSize
        self.currentpage = 2
        self.params = {
            "propertyFor": propertyFor,
            "countryId": countryId,
            "cityId": cityId,
            "type": type,
            "propertyTypeData": propertyTypeData,
            "bedroomsCount": bedroomsCount,
            "min_price": min_price,
            "max_price": max_price,
            "bathroomsCount": bathroomsCount,
            "propertyAge": propertyAge,
            "furnishingTypeId": furnishingTypeId,
            "min_size": min_size,
            "max_size": max_size,
            "pageSize": pageSize,
            'page': 1
        }

        self.content = None

    def make_request(self, pageNo=1):

        self.params["page"] = pageNo

        self.url = self.base_url + "?" + \
            "&".join(f"{key}={value}" for key, value in self.params.items() if value not in [None, '', 0])

        response = self.browser.go_to_page(self.url)
        if response:
            try:
                soup = BeautifulSoup(response, "html.parser")
                next_data_script = soup.find('script', {'id': '__NEXT_DATA__'})
                if next_data_script:
                    self.content = json.loads(next_data_script.string)
                    print(f"Request successful for page : {pageNo}")
                    return True
                else:
                    print("Captcha verification ")
                    return False
            except:
                print("Exception occured ")
        else:
            print(f"Request failed ")

    def parse_properties(self):

        result_proprties = []

        ret = self.make_request()
        if ret:
            props = self.content["props"]["pageProps"]
            searchResult = props["searchResult"]
            properties = searchResult["properties"]
            self.count = searchResult["count"]
            self.pageCount = math.ceil(self.count/self.pageSize)
            print(f"properties count: {self.count} ")
            print(f"Total Page :{self.pageCount}")

            # adding first list at it is
            result_proprties = properties

            for page in range(self.currentpage, self.pageCount+1):
                ret = self.make_request(page)
                properties = self.content["props"]["pageProps"]["searchResult"]["properties"]
                result_proprties = result_proprties + properties
                self.currentpage += 1

            print("All Data Extracted successfully")
            return result_proprties

    def run_scraper(self):
        result_proprties = self.parse_properties()
        self.browser.close_browser()
        if result_proprties:
            df = clean_data(result_proprties)
            return df
            # with open('data.json', 'w', encoding='utf-8') as json_file:
            #     json.dump(result_proprties, json_file, indent=2)

