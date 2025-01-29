from playwright.sync_api import sync_playwright

def scrape_whey_price(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto(url, wait_until="domcontentloaded")

        try:
            page.wait_for_selector("text='Aceitar todas'", timeout=5000)
            page.click("text='Aceitar todas'")
            print("Cookies accepted!")
        except:
            print("No cookie banner found or timeout reached.")

        # Wait for fully loaded page
        page.wait_for_load_state("networkidle")

        try:
            page.wait_for_selector("text='2Kg'", timeout=5000)
            page.click("text='2Kg'")
            print("Clicked '2Kg' button!")
        except:
            print("No '2Kg' button found or timeout reached.")

        # Extract the value of 'data-price-unit' which contains the value we seek
        try:
            price_value = page.get_attribute(".product-price-16688", "data-price-unit")
            print(f"Extracted price value: {round(float(price_value), 2)}€")
        except Exception as e:
            print(f"Error extracting price value: {e}")

        page.screenshot(path="screenshot.png", full_page=True)
        print("Screenshot saved as 'screenshot.png'")

        # Save page source to a file
        with open("page_dump.html", "w", encoding="utf-8") as f:
            f.write(page.content())
        print("Page source saved as 'page_dump.html'")

        browser.close()

scrape_whey_price("https://www.hsnstore.pt/marcas/sport-series/evowhey-protein")
