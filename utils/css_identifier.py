import openai
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

def identify_css_selectors(html_content):
    """
    Uses LLM (OpenAI) to dynamically identify CSS selectors for extracting reviews.
    """
    prompt = f"""
    Analyze the following HTML content and identify the CSS selectors for extracting:
    - Review Container
    - Review Title
    - Review Body
    - Review Rating
    - Reviewer Name
    - Pagination Next Button (if present)
    
    Provide the result in JSON format with keys:
    "review_container", "title", "body", "rating", "reviewer", "pagination_next".

    HTML Content:
    ```
    {html_content[:2000]}  # Send the first 2000 characters to avoid token limits
    ```
    """
    logging.info("Sending request to OpenAI to identify CSS selectors.")
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=300,
            temperature=0.5
        )
        logging.info(f"LLM Response: {response.choices[0].text.strip()}")
        return eval(response.choices[0].text.strip())
    except Exception as e:
        logging.error(f"Error from OpenAI: {e}")
        return {
            "review_container": None,
            "title": None,
            "body": None,
            "rating": None,
            "reviewer": None,
            "pagination_next": None,
        }
