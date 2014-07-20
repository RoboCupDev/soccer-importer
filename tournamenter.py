#!/usr/bin/env python

import requests
import json

class Tournamenter(object):

    teams = {}
    url = ''
    password = ''
    session = None

    def __init__(self, url, password=''):

        self.url = url
        self.password = password

        self.session = requests.Session()

        if password != '':
            if not (self.login(password)):
                raise ValueError("Wrong password or URL")

    def login(self, password):
        r = self.session.post(self.url + '/login', {'password': password})
        return False if 'Wrong Password' in r.content else True


    def add_team(self, name, country):
        r = self.session.post(self.url + '/teams',
                json.dumps({
                    "name": name,
                    "country": country}
                ),
                headers={'content-type': 'application/json'})

        if r.status_code != 201:
            r.content

        return r.json()

    def find_group_id(self, name):
        r = self.session.post(self.url + '/groups/find',
                json.dumps({
                    "name": name
                }),
                headers={'content-type': 'application/json'})

        out = r.json()

        if len(out) == 0:
            return None

        return out[0]['id']


    def load_teams(self):
        r = self.session.get(self.url + '/teams')
        for item in r.json():
            self.teams[item['name']] = item

    def team_info(self, name):
        if not (name in self.teams):
            self.load_teams()

        return self.teams[name]

    def add_match(self, teamA, teamB, day, field, time, group,
            state="scheduled"):

        if type(teamA) != int:
            teamA = self.team_info(teamA)['id']
        if type(teamB) != int:
            teamB = self.team_info(teamB)['id']
        if type(group) != int:
            group = self.find_group_id(group)

        r = self.session.post(self.url + '/matches', json.dumps({
                'teamAId': teamA,
                'teamBId': teamB,
                'groupId': group,
                'day': day,
                'field': field,
                'hour': time,
                'state': state
            }), headers={'content-type': 'application/json'})

        if r.status_code != 201:
            return r.content

        return r.json()

    def find_match_id(self, teamA, teamB, field, day):

        if type(teamA) != int:
            teamA = self.team_info(teamA)['id']
        if type(teamB) != int:
            teamB = self.team_info(teamB)['id']

        r = self.session.post(self.url + '/matches/find', json.dumps({
                'teamAId': teamA,
                'teamBId': teamB,
                'field': field,
                'day': day
            }), headers={'content-type': 'application/json'})


        out = r.json()

        if len(out) == 0:
            return None

        return r.json()[0]['id']


    def update_match(self, teamA, teamB, field, day, teamAScore, teamBScore,
            state="scheduled"):
        if type(teamA) != int:
            teamA = self.team_info(teamA)['id']
        if type(teamB) != int:
            teamB = self.team_info(teamB)['id']

        id = self.find_match_id(teamA, teamB, field, day)

        r =  self.session.post(self.url + '/matches/update', json.dumps({
                'teamAId': teamA,
                'teamBId': teamB,
                'field': field,
                'day': day,
                'teamAScore': teamAScore,
                'teamBScore': teamBScore,
                'id': id,
                'state': state
            }), headers={'content-type': 'application/json'})

        if r.status_code != 200:
            return r.content

        return r.json()

if __name__ == "__main__":
    t = Tournamenter('http://localhost:1337', '12345')
    t.add_match("Brazil", "Argentina", "1", "A", "12:00", 'testing group')

    print(t.find_match_id("Brazil", "Argentina", "A", 1))

    t.update_match("Brazil", "Argentina", "A", 1, 5, 4)

