import requests

url = "https://catalog.onliner.by/sdapi/catalog.api/search/dram?limit=30"

amounts = []

for page_index in range(1, 100):
	new_url = f"{url}&page={page_index}"
	response = requests.get(new_url)
	products = response.json()["products"]
	for product in products:
		print(product["prices"]["price_min"]["amount"])
		amounts.append(float(product["prices"]["price_min"]["amount"]))
	print("---------------------------------------")

amounts.sort()

if len(amounts) > 0:
	print(amounts[0])