<a href="https://"><img src="https://img.shields.io/static/v1?label=LicenSe&message=MIT&color=2ea44f&style=for-the-badge" alt="LicenSe - MIT"></a>
# scraping-products
Scraping project with python. to scrap JLood products.

## Description:
- The app ask the user to input an url of page of products from JLood website.
- Then the project scrap the page and store the parducts names and prices.

## Install and Running the project:
### Installation:
You can install the project by clone the repository in your computer by typing this line in your terminal:
```
git clone https://github.com/Ahmed101Mohammed/scraping-products.git
```

### Run the project:
```
pip install requests
pip install lxml
pip install bs4
```
copy the lines above and paste them in the project enviroment terminal to install these libraries.
Then write this line in the terminal:
```
python3 main.py
```
## How to use:
When you run the project this is the screen that you will show:
![Url asking screen](https://github.com/Ahmed101Mohammed/scraping-products/blob/main/photos_to_exeplain/ask-for-url.png)

Then you need to enter an email form [JLood website](https://jlood.com/), like you see in the image down:
![Put url screen](https://github.com/Ahmed101Mohammed/scraping-products/blob/main/photos_to_exeplain/put-url.png)

When you **Press Enter Button** the program will run with **Wait Screen**:
![Wait Screen](https://github.com/Ahmed101Mohammed/scraping-products/blob/main/photos_to_exeplain/wait-screen.png)

When the program finish its work and store the data in products.sqlite database then the sentence **"Done, Explore product.sqlite file"** will appear:
![done sentence](https://github.com/Ahmed101Mohammed/scraping-products/blob/main/photos_to_exeplain/done-screen.png)

> Note! to open **products.sqlite** file you can't open with text editore, you need to have **sqlite browser** app, install it to open your database.
