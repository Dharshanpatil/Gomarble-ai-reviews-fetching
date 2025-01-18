import React, { useState } from "react";
import axios from "axios";

function App() {
  const [url, setUrl] = useState("");
  const [reviews, setReviews] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const fetchReviews = async () => {
    setLoading(true);
    setError(null);
    setReviews([]);
    try {
      const response = await axios.get("http://127.0.0.1:8000/api/reviews", {
        params: { url },
      });
      setReviews(response.data.reviews);
    } catch (err) {
      setError("Error fetching reviews. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>Product Review Scraper</h1>
      <input
        type="text"
        placeholder="Enter product page URL"
        value={url}
        onChange={(e) => setUrl(e.target.value)}
        style={{ width: "80%", padding: "10px", margin: "10px 0" }}
      />
      <button onClick={fetchReviews} style={{ padding: "10px 20px" }}>
        {loading ? "Fetching..." : "Fetch Reviews"}
      </button>
      {error && <p style={{ color: "red" }}>{error}</p>}
      <div style={{ marginTop: "20px" }}>
        {reviews.length > 0 ? (
          reviews.map((review, index) => (
            <div key={index} style={{ marginBottom: "20px" }}>
              <h3>{review.title || "No Title"}</h3>
              <p><strong>Reviewer:</strong> {review.reviewer || "Anonymous"}</p>
              <p><strong>Rating:</strong> {review.rating || "No Rating"}</p>
              <p>{review.body || "No Review Body"}</p>
            </div>
          ))
        ) : (
          <p>No reviews to display</p>
        )}
      </div>
    </div>
  );
}

export default App;
