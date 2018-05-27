# coding: utf-8

"""
    OpenDota API

    # Introduction The OpenDota API provides Dota 2 related data including advanced match data extracted from match replays. Please keep request rate to approximately 1/s.  **Begining 4/22/2018, the OpenDota API will be limited to 50,000 free calls per month.** We'll be offering a Premium Tier with unlimited API calls and higher rate limits. Check out the [API page](https://www.opendota.com/api-keys) to learn more. 

    OpenAPI spec version: 17.6.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import od_python
from od_python.rest import ApiException
from od_python.apis.players_api import PlayersApi


class TestPlayersApi(unittest.TestCase):
    """ PlayersApi unit test stubs """

    def setUp(self):
        self.api = od_python.apis.players_api.PlayersApi()

    def tearDown(self):
        pass

    def test_players_account_id_counts_get(self):
        """
        Test case for players_account_id_counts_get

        GET /players/{account_id}/counts
        """
        pass

    def test_players_account_id_get(self):
        """
        Test case for players_account_id_get

        GET /players/{account_id}
        """
        pass

    def test_players_account_id_heroes_get(self):
        """
        Test case for players_account_id_heroes_get

        GET /players/{account_id}/heroes
        """
        pass

    def test_players_account_id_histograms_field_get(self):
        """
        Test case for players_account_id_histograms_field_get

        GET /players/{account_id}/histograms
        """
        pass

    def test_players_account_id_matches_get(self):
        """
        Test case for players_account_id_matches_get

        GET /players/{account_id}/matches
        """
        pass

    def test_players_account_id_peers_get(self):
        """
        Test case for players_account_id_peers_get

        GET /players/{account_id}/peers
        """
        pass

    def test_players_account_id_pros_get(self):
        """
        Test case for players_account_id_pros_get

        GET /players/{account_id}/pros
        """
        pass

    def test_players_account_id_rankings_get(self):
        """
        Test case for players_account_id_rankings_get

        GET /players/{account_id}/rankings
        """
        pass

    def test_players_account_id_ratings_get(self):
        """
        Test case for players_account_id_ratings_get

        GET /players/{account_id}/ratings
        """
        pass

    def test_players_account_id_recent_matches_get(self):
        """
        Test case for players_account_id_recent_matches_get

        GET /players/{account_id}/recentMatches
        """
        pass

    def test_players_account_id_refresh_post(self):
        """
        Test case for players_account_id_refresh_post

        POST /players/{account_id}/refresh
        """
        pass

    def test_players_account_id_totals_get(self):
        """
        Test case for players_account_id_totals_get

        GET /players/{account_id}/totals
        """
        pass

    def test_players_account_id_wardmap_get(self):
        """
        Test case for players_account_id_wardmap_get

        GET /players/{account_id}/wardmap
        """
        pass

    def test_players_account_id_wl_get(self):
        """
        Test case for players_account_id_wl_get

        GET /players/{account_id}/wl
        """
        pass

    def test_players_account_id_wordcloud_get(self):
        """
        Test case for players_account_id_wordcloud_get

        GET /players/{account_id}/wordcloud
        """
        pass


if __name__ == '__main__':
    unittest.main()
