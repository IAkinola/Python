from bs4 import BeautifulSoup
import requests

search = input("Search for: ")
params = {"q": search}
r = requests.get("https://steamcommunity.com/market/search", params=params)

soup = BeautifulSoup(r.text, "html.parser")
results = soup.find("div", {"id": "searchResultsRows"})
links = results.findAll("a", {"class": "market_listing_row_link"})


# For each item, display the name, the game, price and quality and the link to the item

for item in links:
    item_name = item.find("span", {"class": "market_listing_item_name"}).text
    item_game = item.find("span", {"class": "market_listing_game_name"}).text
    item_price = item.find("span", {"class": "sale_price"}).text

    # if item_name and item_quality and item_price:
    print(item_name)
    print(item_game)
    print(item_price)
    print("\n")
    #    print(item_quality)

# Notes:
# It only displays the first 10 items
# Item quality really necessary?
