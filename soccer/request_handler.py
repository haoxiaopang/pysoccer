import requests
from .exceptions import APIErrorException
from soccer.data import LEAGUE_LISTS, urls
import json

__all__ = ['RequestHandler']

class RequestHandler(object):

    BASE_URL = urls['base']
    SEASON_URL = urls['season']

    def __init__(self, headers, league_ids, team_names):
        self.headers = headers
        self.league_ids = league_ids
        self.team_names = team_names

    def _get(self, url):
        """Handles api.football-data.org requests"""
        req = requests.get(RequestHandler.BASE_URL + url, headers=self.headers)
        if req.status_code == requests.codes.ok:
            return req

        if req.status_code == requests.codes.bad:
            raise APIErrorException('Invalid request. Check parameters.')

        if req.status_code == requests.codes.forbidden:
            raise APIErrorException('This resource is restricted')

        if req.status_code == requests.codes.not_found:
            raise APIErrorException('This resource does not exist. Check parameters')

        if req.status_code == requests.codes.too_many_requests:
            raise APIErrorException('You have exceeded your allowed requests per minute/day')

    def _get_by_season(self, url):
        """Handles api.football-data.org requests"""
        req = requests.get(RequestHandler.SEASON_URL + url, headers=self.headers)

        if req.status_code == requests.codes.ok:
            return req

        if req.status_code == requests.codes.bad:
            raise APIErrorException('Invalid request. Check parameters.')

        if req.status_code == requests.codes.forbidden:
            raise APIErrorException('This resource is restricted')

        if req.status_code == requests.codes.not_found:
            raise APIErrorException('This resource does not exist. Check parameters')

        if req.status_code == requests.codes.too_many_requests:
            raise APIErrorException('You have exceeded your allowed requests per minute/day')


    def get_league(self, league):
        league_id = self.league_ids[league]
        return self._get('competitions/{id}'.format(id=league_id))

    def get_leagues(self):
        return self._get('competitions')

    def get_leagues_by_season(self, season):
        return self._get_by_season('soccerseasons?season={season}'
                            .format(season=season))

    def get_standings(self, league):
        """Queries the API and gets the standings for a particular league"""
        league_id = self.league_ids[league]
        return self._get('competitions/{id}/leagueTable'.format(id=league_id))

    def get_standings_by_matchday(self, league, md):
        """Queries the API and gets the standings for a particular league"""
        league_id = self.league_ids[league]
        return self._get('competitions/{id}/leagueTable?matchday={md}'
                            .format(id=league_id,md=md))

    def get_teams(self, league):
        league_id = self.league_ids[league]
        return self._get('competitions/{id}/teams'.format(id=league_id))

    def get_players(self, team):
        team_id = self.team_names[team]
        return self._get('teams/{id}/players'.format(id=team_id))

    def get_fixtures(self):
        return self._get('fixtures')

    def get_fixtures_by_tf(self, tf):
        return self._get('fixtures?timeFrame={tf}'.format(tf=tf))

    def get_fixtures_by_league(self, league):
        league_id = self.league_ids[league]
        return self._get('competitions/{id}/fixtures'.format(id=league_id))

    def get_fixtures_by_md_league(self, md, league):
        league_id = self.league_ids[league]
        return self._get('competitions/{id}/fixtures?matchday={md}'
                            .format(id=league_id, md=md))


    def get_fixtures_by_tf_league(self, tf, league):
        league_id = self.league_ids[league]
        return self._get('competitions/{id}/fixtures?timeFrame={tf}'
                            .format(id=league_id,tf=tf))

    def get_fixtures_by_md_tf_league(self, md, tf, league):
        league_id = self.league_ids[league]
        return self._get('competitions/{id}/fixtures?matchday={md}&timeFrame={tf}'
                            .format(id=league_id, md=md, tf=tf))

    def get_fixtures_by_team(self, team):
        team_id = self.team_names[team]
        return self._get('teams/{id}/fixtures'.format(id=team_id))

    def get_fixtures_by_id(self, id, h2h):
        return self._get('fixtures/{id}?head2head={h2h}'.format(id=id, h2h=h2h))

    def get_lists(self):
        return LEAGUE_LISTS

    def jsonify(self,data):
        return json.dumps(data, sort_keys=True, indent=4, ensure_ascii=False)
