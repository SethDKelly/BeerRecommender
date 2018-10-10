def get_data() :
    
    import pandas as pd
    
    # rating_update is the original data 'beer_review.csv' with beer_style updated
    # The updates change beer_style to match the styles that are given in 'beer_description.csv'

    csv_beer = pd.read_csv("/home/grimoire/Projects/BeerRatings/rating_update.csv")
    beer_ratings = pd.DataFrame(csv_beer)
    
    return beer_ratings
