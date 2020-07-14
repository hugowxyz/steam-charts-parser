import urllib.request
from bs4 import BeautifulSoup


# StackOverflow post for setting headers https://stackoverflow.com/questions/13055208/httperror-http-error-403-forbidden
# Using Bs4 documentation to learn https://www.crummy.com/software/BeautifulSoup/bs4/doc/


class Month:
    """
    Holds the data for each month
    """
    def __init__(self, game, month, avg_players, gain, percent_gain, peak):
        self.game = game
        self.month = month
        self.avgPlayers = avg_players
        self.gain = gain
        self.percentGain = percent_gain
        self.peak = peak

    def show(self):
        print("Month\t\t\tAverage Players\t\tPlayer Gain\t\tPercentage Gain\t\tPeak")
        print(f"{self.month}\t{self.avgPlayers}\t\t{self.gain}\t\t{self.percentGain}\t\t{self.peak}")

    def read(self):
        file = open(f'{self.game}.txt', 'r')
        to_return = file.readlines()
        file.close()
        return to_return

    def save(self):
        try:
            concurrent = self.read()
        except FileNotFoundError:
            concurrent = []

        file = open(f'{self.game}.txt', 'w')
        for toSplit in concurrent:
            split = toSplit.split(',')
            for toWrite in split:
                file.write(f"{toWrite}")
                if split.index(toWrite) != (len(split) - 1):
                    file.write(',')

        file.write(f"{self.month},")
        file.write(f"{self.avgPlayers},")
        file.write(f"{self.gain},")
        file.write(f"{self.percentGain},")
        file.write(f"{self.peak}")
        file.write("\n")
        file.close()


def main(args):
    # Setting the headers and making HTTP request for the website HTML
    header = {'User-Agent': 'Mozilla/5.0'}
    request = urllib.request.Request(args['url'], headers=header)

    # Receive the response in HTML form, response.read returns the HTML
    response = urllib.request.urlopen(request)
    html = response.read()

    # Use BeautifulSoup to parse the html and find the Table tags
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find_all('td')

    array = []
    data = []

    for tableData in table:
        if len(array) >= 5:
            record = Month(args['game'], array[0], array[1], array[2], array[3], array[4])
            record.save()
            data.append(record)
            array.clear()

        # text method returns innerHTML
        # strip() gets rid of whitespace
        item = tableData.text.strip()
        array.append(item)

toCall = [
    {
        'game': 'Dota2',
        'url': 'https://steamcharts.com/app/570'
    },
    {
        'game': 'PUBG',
        'url': 'https://steamcharts.com/app/578080'
    },
    {
        'game': 'Destiny2',
        'url': 'https://steamcharts.com/app/1085660'
    },
    {
        'game': 'GTAV',
        'url': 'https://steamcharts.com/app/271590'
    },
    {
        'game': 'TF2',
        'url': 'https://steamcharts.com/app/440'
    }
]

for arg in toCall:
    main(arg)