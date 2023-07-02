from rest_framework import viewsets
from rest_framework.response import Response
from .naics_search import search_naics

class NaicsSearchView(viewsets.ViewSet):
    def list(self, request):
        query = request.query_params.get('search', '')  # change 'query' to 'search'
        results = search_naics(query)
        return Response(results)