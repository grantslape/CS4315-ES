import requests
import json


def main():
    with open('review.json', 'r') as file:
        counter = 1
        url = 'http://localhost:45000/reviews/{}'
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

        for line in file:
            review = json.loads(line)
            resp = requests.put(url.format(counter), headers=headers, data=json.dumps(review))
            if resp.status_code > 201:
                print('failure: {}'.format(resp.json()))

            counter += 1


if __name__ == '__main__':
    main()
