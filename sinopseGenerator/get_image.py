from playwright.sync_api import sync_playwright
import time

from requests import head

def get_image_by_sinopsys(text):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless= False)
        page = browser.new_page()
        page.set_default_timeout(0)
        page.goto('https://replicate.com/pixray/text2image')
        page.locator("[name='prompts']").fill(text)
        page.locator("button[type='submit']").click()
        running = True
        counting = 0
        while running:
            time.sleep(1)
            if page.locator("[alt = 'output']"):
                running = False
            counting += 1
            if(counting == 30):
                print("Cancelando")
                page.locator("button:has_text('Cancel'").click()
                page.locator("button[type='submit']").click()
        print("gerando imagem")
        time.sleep(180)
        href = "https://replicate.com" + page.locator(f"[alt = 'output']").get_attribute('src')
        return href