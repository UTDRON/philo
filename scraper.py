from google_play_scraper import Sort, reviews
import json

def fetch_reviews(app_id, max_count_per_call=200, max_pages=50):
    """
    Fetch all reviews for a given app_id, safely handling continuation tokens.
    Returns a list of reviews (dicts with 'score' and 'content').
    """
    all_reviews = []
    continuation_token = None
    pages = 0

    while True:
        result, continuation_token = reviews(
            app_id,
            lang='en',
            country='us',
            sort=Sort.NEWEST,
            count=max_count_per_call,
            continuation_token=continuation_token
        )
        all_reviews.extend(result)
        pages += 1

        if not continuation_token or pages >= max_pages:
            break

    return all_reviews


def filter_reviews(all_reviews, max_per_rating=15, min_length=100):
    """
    Filters reviews: keeps max_per_rating per star rating, and only reviews longer than min_length.
    """
    counts = [0, 0, 0, 0, 0]
    final = []

    for r in all_reviews:
        score = r['score']
        content = r['content']

        if 1 <= score <= 5 and len(content) > min_length and counts[score-1] < max_per_rating:
            final.append({"rating": score, "review": content})
            counts[score-1] += 1

    return final, counts


def save_reviews(final_reviews, filename):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(final_reviews, f, indent=2, ensure_ascii=False)
    print(f"Saved {len(final_reviews)} reviews to {filename}")


khan_app_id = 'no.mobitroll.kahoot.android'
print("Fetching Kahoot reviews...")
khan_all = fetch_reviews(khan_app_id)
khan_final, khan_counts = filter_reviews(khan_all)
print("Counts per rating:", khan_counts)
save_reviews(khan_final, "kahoot_reviews.json")


