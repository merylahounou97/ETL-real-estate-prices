# Fonctions
import re
import requests


from bs4 import BeautifulSoup as bs


def scrapping(url: str, page: int):
    """_summary_

    Args:
        url (str): _description_
        page (int): _description_
    """

    response = requests.get(url, timeout=120)

    while response.status_code == 200:
        url = rf"{url}&page={page}"
        response = requests.get(url, timeout=120)
        html = response.content
        soup = bs(html, "html")
        # print("Status code: ", response.status_code)
        descs = soup.find_all("div", {"class": "infos"})
        # print("DESCS: ", descs)

        data = []

        for i, des in enumerate(descs):
            content = {
                "id": i,
                "title": None,
                "description": None,
                "type": None,
                "surface": None,
                "price": None,
                "city": None,
                "postal_code": None,
                "number_pieces": None,
            }

            # print("DES: ", des)
            content["title"] = des.find("h3").get_text().strip().replace("\n", "")

            content["description"] = (
                des.find("p", class_="description-start").get_text()
                + "\n"
                + des.find("span", class_="description-more").get_text()
            )
            content["description"] = content["description"].replace("\xa0", "")
            # print("DESCRIPTION: ", content['description'])

            cities = des.find("p", class_="ville").get_text().strip()

            content["city"] = " ".join(re.findall("[a-zA-ZÀ-ȕ]+", cities))
            # print("CITY: ", content['city'])

            content["postal_code"] = re.findall("[0-9]+", cities)[-1]
            # print("POSTAL CODE: ", content['postal_code'])

            content["price"] = int(
                des.find("p", class_="prix")
                .find("strong")
                .get_text()
                .replace("\u202f", "")
                .replace("\xa0€", "")
                .split()[0]
            )
            # print("PRICE: ", content['price'])

            content["type"] = des.find("h3").get_text().split()[0]
            # print("TYPE: ", content['type'])

            dt = des.find("h3").find("strong").get_text().replace("s", "")
            # print("DT: ", dt)

            if "pièce" in dt and "m²" in dt:
                content["number_pieces"] = int(dt.split("pièce")[0])
                content["surface"] = float(dt.split("pièce")[1].split("m²")[0])
                # print("NUMBER PIECES: ", content['number_pieces'])
                # print("SURFACE: ", content['surface'])
            elif "pièce" in dt and "m²" not in dt:
                content["number_pieces"] = int(dt.split("pièce")[0])
                # print("NUMBER PIECES: ", content['number_pieces'])
            elif "pièce" not in dt and "m²" in dt:
                content["surface"] = float(dt.split("m²")[0])
                # print("SURFACE: ", content['surface'])

            data.append(content)

        if not data:
            break

        print("DATA: ", data)

        page += 1


if __name__ == "__main__":
    url = "https://www.citya.com/annonces/vente/appartement,maison?sort=b.dateMandat&direction=desc"
    page = 1
    scrapping(url, page)
