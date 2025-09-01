# scraper.py
from jobspy import scrape_jobs

def scrape_jobs_df(query, location, limit=30):
    jobs = scrape_jobs(
        site_name=["indeed"],   # you can also add ["linkedin", "glassdoor"]
        search_term=query,
        location=location,
        results_wanted=limit,
        country_indeed="UK",    # since your URL was uk.indeed.com
        verbose=0
    )
    return jobs  # returns a pandas DataFrame
