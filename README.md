## Beer Recommendation Engine: Do I have a beer for you.

This project folder will include:
* A section for cleaning and visualization of data.
 * Data_cleaning.ipynb : Amelioration of bad values in review_profilename and brewery_name found in beer_reviews.csv
 * Cleaning_pt2.ipynb : Amelioration of bad values in beer_abv found in beer_reviews.csv
 * Beer_description_review_style_verification.ipynb : Verifying style variables match between beer_review.csv and beer_description.csv
* Logistic Regression Rating Prediction
 * Logistic_regression_rating_prediction.ipynb : Includes a histogram of all review_* items and Cumalative Distribution Functions (CDFs) between review_appearance, aroma, taste, palate and review_overall to look at linear relationships. Also includes multiple logistic regressions to look at individual feature predictive models and combined
* Recommendation models that suggests beer styles or individual beers to users/consumers based on their tastes.
* Project wrap up, which may include pdfs or slidedecks to present findings.
 * Project report

A unique use case is for clients similar to https://www.firstdraftmn.com/ or https://www.tapsocietymn.com/. These bars allows customers choose from a variety of taps that they pour themselves. A recommendation engine behind the concept could cater to novice drinkers in helping to narrow the selection down. Additional benefits may include reducing waste of beer, and reducing beer decision time. Customers may have a better idea of beer they may like, and instead of trying a large number of beers before choosing, they may only try a few. Possible additional benefits may come from larger pours of beers, increase profits.

Data is available upon sign up: (csv format)
https://data.world/socialmediadata/beeradvocate (data is provided by beeradvocate)
(1,586,614 observations, 13 features: brewery_id, brewery_name, review_time, review_overall, review_aroma, review_appearance, review_profilename, beer_style, review_palate, review_taste, beer_name)

