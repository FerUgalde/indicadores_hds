from datetime import datetime

def create_period_choices():
    current_year = datetime.now().year
    five_years_ago = current_year - 5
    periods = []


    for i in range(five_years_ago, current_year):
        period_before_mid_year = f"{i} - 1"
        period_1key = f"{i}1"
        period_after_mid_year = f"{i} - 2"
        period_2key = f"{i}2"
        periods.append((int(period_1key), period_before_mid_year))
        periods.append((int(period_2key), period_after_mid_year))

    return periods
