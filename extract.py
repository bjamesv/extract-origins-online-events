import sys
import fileinput

def print_csv_line(event_html):
    """
    Return string representing comma separated event Title,Date,Start Time,End Time, Description

    >>> test_string1 = '''<html> \
    <!-- fake tags --> \
	<title> \
	Learn to Play Pizza \
    </title> \
    <!-- fake tags --> \
           <div class="calendar" title="Start Date: 6/19/2020"> \
    <!-- fake tags --> \
              <div class="grid align-middle clock" title="Start Time: 12:00 PM"> \
    <!-- more fake tags --> \
              <div class="grid align-middle clock" title="End Time: 12:30 PM"> \
    <!-- additional fake tags --> \
           <div class="product-short-description"> \
											Learn to play the upcoming family game Pizza. We'll be teaching and playing through a whole game online. \
		   </div> \
    </html>'''
    >>> print_csv_line(test_string1)
    '"Learn to Play Pizza", "6/19/2020", "12:00 PM", "12:30 PM", "Learn to play the upcoming family game Pizza. We'll be teaching and playing through a whole game online."'
    """
    def extract (text, before_string, after_string):
        garbage, matched, remainder = event_html.partition(before_string)
        if matched != before_string:
            raise ValueError('before_string "{}" not found in event'.format(before_string))
        raw_extract, matched, remainder = remainder.partition(after_string)
        if matched != after_string:
            raise ValueError('after_string "{}" not found in event'.format(after_string))
        return raw_extract.strip()
    # extract
    title = extract(event_html, '<title>', '</title>')
    date = extract(event_html, 'Start Date: ', '">')
    try:
        start = extract(event_html, 'Start Time: ', '">')
        end = extract(event_html, 'End Time: ', '">')
    except ValueError as e:
        start, end = "", ""
    description = extract(event_html, 'product-short-description">', '</div>')
    values = [title, date, start, end, description]
    return '"'+'", "'.join(values)+'"' #fake CSV line

if __name__ == '__main__':
    # get text from either stdin or the filename specified on the command line
    event_html=''.join(fileinput.input())
    event_filename = '"event-filename-not-provided", '
    if sys.argv[1:]:
        event_filename = '"{}", '.format(sys.argv[1])
    try:
        print(event_filename+print_csv_line(event_html))
    except ValueError as e:
        raise ValueError("{} {}".format(e, event_filename))
