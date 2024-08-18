import re
import pandas as pd

def dms_to_decimal(dms_str):
    # Regular expression to match the DMS format
    pattern = r'([+-])(\d+)° (\d+)′?\'? (\d+\.?\d*)″?"?'
    
    # Extract components using regex
    match = re.match(pattern, dms_str)
    if not match:
        raise ValueError("Invalid DMS format")
    
    sign, degrees, minutes, seconds = match.groups()
    
    # Convert to decimal degrees
    decimal = int(degrees) + int(minutes)/60 + float(seconds)/3600
    
    # Apply sign
    if sign == '-':
        decimal = -decimal
    
    return round(decimal, 6)

def get_table(url):
    tables = pd.read_html(url)
    df = tables[-1]
    df.dropna(subset=['Latitude','Longitude'],inplace=True,how='all')
    df['Latitude'] = df['Latitude'].apply(dms_to_decimal)
    df['Longitude'] = df['Longitude'].apply(dms_to_decimal)
    
    return df