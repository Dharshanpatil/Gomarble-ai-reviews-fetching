from fastapi import FastAPI, HTTPException
from scraper.playwright_scraper import scrape_reviews

app = FastAPI()

@app.get("/api/reviews")
async def get_reviews(url: str):
    try:
        reviews_data = await scrape_reviews(url)
        return reviews_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
