This is a light weight script to automatically refresh and purchase item from Best Buy using Python3.6 and Selenium.

Set up env:
1. Create conda environment with python 3.6 `conda create -n myenv python=3.6` (if you don't have anaconda, use `virtualenv` instead).
2. Install selenium `conda install selenium` in the new environment (use `pip` if without anaconda).
3. Download ChromeDriver according to your Chrome version from http://chromedriver.storage.googleapis.com/index.html.
4. Find your python path using `which python` and move the `chromedriver.exe` to the same folder.

Before you run:
1. Make sure that you have your shipping address, and payment method (credit card) saved on your Best Buy profile.
2. Set your login_url, item_url, uid, upassword, and cvv in the bestbuy.py script.

The script is last updated on 2020-04-04. This method relies heavily on the xpath and class and is subject to change upon site updates.

TODO:
- bug: sometimes fail to refresh after a while
