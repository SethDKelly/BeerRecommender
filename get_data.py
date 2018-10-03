def get_data() :
    
    import pandas as pd
    
    csv_beer = pd.read_csv("/home/grimoire/Projects/BeerRatings/rating_update.csv")
    beer_ratings = pd.DataFrame(csv_beer)
    
    return beer_ratings
