def calcParams():
    years = [2000, 2002, 2005, 2007, 2010]
    unemployment_rates = [6.5, 7.0, 7.4, 8.2, 9.0]
    mean_x = sum(years) / len(years)
    mean_y = sum(unemployment_rates) / len(unemployment_rates)
    numerator = sum((x - mean_x) * (y - mean_y) for x, y in zip(years, unemployment_rates))
    denominator = sum((x - mean_x) ** 2 for x in years)
    slope = numerator / denominator
    intercept = mean_y - slope * mean_x
    print(f"Równanie regresji liniowej: y = {slope:.3f}x + {intercept:.3f}")

    def predict_unemployment(year):
        return slope * year + intercept

    predicted_rate_2011 = predict_unemployment(2011)
    print(f"Przewidywany procent bezrobocia w roku 2011: {predicted_rate_2011:.3f}%")
    return slope, intercept
