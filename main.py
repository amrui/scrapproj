
from bs4 import BeautifulSoup

with open("blank/index.html", encoding="UTF-8") as file:
    src = file.read()
# print(src)

soup = BeautifulSoup(src, "lxml")

# find_all_spans_in_user_info = soup.find(class_="user__info").find_all("span")
# #print(find_all_spans_in_user_info)
#
# for item in find_all_spans_in_user_info:
#     print(item.text)

# user_links = soup.find("div", class_="social__networks").find("ul").find_all("a")
#
# for item in user_links:
#     item_text = item.text
#     item_url = item.get("href")
#     print(f"{item_url}: {item_text}")

post_div = soup.find(class_="post__title").find("h3")
print(post_div)