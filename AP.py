import requests
from urllib import request

from bs4 import BeautifulSoup

def decode_secret_message(url):
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    data = []

    for row in soup.find_all("tr"):
        cells = row.find_all(["td", "th"])

        if len(cells) >= 3:
            try:
                x = int(cells[0].get_text(strip=True))
                char = cells[1].get_text(strip=True)
                y = int(cells[2].get_text(strip=True))

                if char:
                    data.append((x, y, char))
            except ValueError:
                continue

    if not data:
        return ""

    max_x = max(item[0] for item in data)
    max_y = max(item[1] for item in data)

    grid = [
        [" "] * (max_x + 1)
        for _ in range(max_y + 1)
    ]

    for x, y, char in data:
        grid[y][x] = char

    for row in reversed(grid):
        print("".join(row))

    return "".join(
        "".join(row)
        for row in reversed(grid)
    )


url = input("Enter Google Docs URL: ")
decode_secret_message(url)