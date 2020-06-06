# Extract Origins-Online 2020 event details

[Origins Game Fair](http://originsgamefair.com) is running a three day online table-top gaming expo, but retrieving event dates & times requires clicking on individual event titles across multiple pages of events. Best I could manage to view was the titles & descriptions split into 11 separate pages, ordered by date (additional individual clicks required to view *which* date an event is on).

Extract-origins-online-events provides a simple Python module (`extract.py`) to consolidate all event data into a single, browseable spreadsheet file (`events.csv`) using `python3`, `wget`, `seq` & `bash`.

## Usage
```
# 1) Retrieve events on all pages [170MB; takes about 7 minutes to run]
for PAGE in `seq 1 10`; do wget --recursive --level=1 'https://gama.configio.com/ShoppingCart.aspx?srt=startdate&pg='$PAGE; done

# 2) Prepare an empty CSV file
echo '"Event File", "Title", "Date", "Start Time", "End Time", "Description"' > events.csv

# 3) Process into the events.CSV
find gama.configio.com/pd/*/* -exec python3 extract.py {} \; >> events.csv

# 4) Clean up
rm -Rf gama.configio.com/
```

## Testing
Unit tests are run via
```
python3 -m unittest discover .
```

#### Copyright (C) 2020 bjamesv
