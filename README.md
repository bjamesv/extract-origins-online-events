# Extract Origins-Online 2020 event details

# Usage
```
# Retrive all event pages (takes a minute or two)
wget --recursive --level=2 'https://gama.configio.com/ShoppingCart.aspx?srt=startdate'
# Prepare an empty CSV file
echo '"Event File", "Title", "Date", "Start Time", "End Time", "Description"' > events.csv
# Process into the events.CSV
find gama.configio.com/pd/*/* -exec python3 extract.py {} \; >> events.csv
```

# Testing
Unit tests are run via
```
python3 -m unittest discover .
```
