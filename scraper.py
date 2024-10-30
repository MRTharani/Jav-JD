from bs4 import BeautifulSoup
from pyrogram import Client
from playwright.async_api import async_playwright


async def create_browser_context(p, user_agent):
    """Create a browser context with the specified User-Agent."""
    browser = await p.chromium.launch(headless=True)
    context = await browser.new_context(user_agent=user_agent)
    return browser, context

async def fetch_page_content(context, url):
    """Navigate to the URL and fetch the page content."""
    page = await context.new_page()
    await page.goto(url)
    await page.wait_for_load_state('networkidle')
    content = await page.content()
    await page.close()
    return content

def parse_html(html_content):
    """Parse HTML content and extract all links."""
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup.find_all('a', href=True)

def filter_links(links, base_url):
    """Filter links based on the base URL and suffix."""
    return [link['href'] for link in links]

async def fetch_page(url):
    """Main function to fetch page and return filtered links."""
    async with async_playwright() as p:
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
        base_url = 'https://missav.com/'
        browser, context = await create_browser_context(p, user_agent)
        page_content = await fetch_page_content(context, url)
        links = parse_html(page_content)
        await browser.close()
        return links

  
