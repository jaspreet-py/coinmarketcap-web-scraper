import requests
from bs4 import BeautifulSoup, NavigableString, ResultSet, Tag
from typing import Optional


def scrape(url):
    data: list[dict] = []
    request = requests.get(url)
    soup: BeautifulSoup = BeautifulSoup(request.content, "lxml")
    table: Tag = soup.find("table", class_="cmc-table")
    tbody: Tag = table.find("tbody")
    rows: ResultSet[Tag] = tbody.find_all("tr")

    for row in rows:
        cells: ResultSet[Tag] = row.find_all("td")
        # As we don't have an identifier to work with in identifying the cells
        # according to a attributes, we create a map based on indexes,
        # referring a {name} to a particular cell at index[i] containing data for
        # field {name}
        # Eg. A currency's 'Name' data is stored in the 3rd cell
        # of the row, 'Price' in the 4th cell and so on
        try:
            cell_map: dict[str, Tag] = {
                "name": cells[2],
                "price": cells[3],
                "1h": cells[4],
                "24h": cells[5],
                "7d": cells[6],
                "mcap": cells[7],
                "volume": cells[8],
                "c_supply": cells[9],
            }
        except IndexError:
            continue

        name_cell: Tag = cell_map["name"].find("div", class_="name-area")
        name: str = name_cell.find("p").text
        symbol: str = name_cell.find("p", class_="coin-item-symbol").text
        price: str = cell_map["price"].find("span").text
        change: dict[str, str] = {
            "1h": cell_map["1h"].find("span").text,
            "24h": cell_map["24h"].find("span").text,
            "7d": cell_map["7d"].find("span").text
        }
        mcap: str = cell_map["mcap"].find("span", attrs={"data-nosnippet": "true"}).text
        volume: dict[str, str] = {
            "amt": cell_map["volume"].find("p").text,
            "units": cell_map["volume"].find("div", attrs={"data-nosnippet": "true"}).find("p").text
        }
        c_supply: str = cell_map["c_supply"].find("p").text

        currency_data: dict[str, (str | dict[str, str])] = {
            "name": name,
            "symbol": symbol,
            "price": price,
            "change": change,
            "mcap": mcap,
            "volume": volume,
            "c_supply": c_supply
        }
        data.append(currency_data)
        
    return data


url = "https://coinmarketcap.com/"
scrape(url)
