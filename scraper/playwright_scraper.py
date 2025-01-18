import logging
from urllib.parse import unquote
from playwright.async_api import async_playwright
from utils.css_identifier import identify_css_selectors

# Configure logging
logging.basicConfig(level=logging.INFO)

async def scrape_reviews(url):
    try:
        # Decode the URL
        decoded_url = unquote(url)
        logging.info(f"Decoded URL: {decoded_url}")

        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()

            # Navigate to the decoded URL
            await page.goto(decoded_url, wait_until="load")
            logging.info("Page loaded successfully.")

            # Extract HTML content
            html_content = await page.content()

            # Use LLM to identify CSS selectors
            css_selectors = identify_css_selectors(html_content)
            logging.info(f"Identified CSS Selectors: {css_selectors}")

            # Validate CSS selectors
            if not css_selectors["review_container"]:
                raise Exception("Review container selector not found.")

            # Extract reviews
            reviews = []
            review_containers = await page.query_selector_all(css_selectors["review_container"])
            logging.info(f"Found {len(review_containers)} reviews.")

            for container in review_containers:
                review = {
                    "title": await (await container.query_selector(css_selectors.get("title"))).inner_text() if css_selectors.get("title") else None,
                    "body": await (await container.query_selector(css_selectors.get("body"))).inner_text() if css_selectors.get("body") else None,
                    "rating": await (await container.query_selector(css_selectors.get("rating"))).inner_text() if css_selectors.get("rating") else None,
                    "reviewer": await (await container.query_selector(css_selectors.get("reviewer"))).inner_text() if css_selectors.get("reviewer") else None,
                }
                reviews.append(review)

            # Handle pagination
            while True:
                next_button = await page.query_selector(css_selectors.get("pagination_next"))
                if next_button:
                    logging.info("Navigating to next page of reviews.")
                    await next_button.click()
                    await page.wait_for_load_state("domcontentloaded")
                    new_review_containers = await page.query_selector_all(css_selectors["review_container"])
                    for container in new_review_containers:
                        review = {
                            "title": await (await container.query_selector(css_selectors.get("title"))).inner_text() if css_selectors.get("title") else None,
                            "body": await (await container.query_selector(css_selectors.get("body"))).inner_text() if css_selectors.get("body") else None,
                            "rating": await (await container.query_selector(css_selectors.get("rating"))).inner_text() if css_selectors.get("rating") else None,
                            "reviewer": await (await container.query_selector(css_selectors.get("reviewer"))).inner_text() if css_selectors.get("reviewer") else None,
                        }
                        reviews.append(review)
                else:
                    break

            await browser.close()
            return {"reviews_count": len(reviews), "reviews": reviews}

    except Exception as e:
        logging.error(f"Error occurred: {e}")
        raise e
