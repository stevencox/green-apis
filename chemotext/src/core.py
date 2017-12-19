from greent.service import ServiceContext
from greent.chemotext import Chemotext

class SupportControllerImpl:
    """ Implemnetation of the logic to invoke the Chemotext databse. 
    This is woven into the generated swagger code using a custom template.
    Since the integration is naming convention driven, change the name of this class
    along with the API specification.
    """    
    def __init__(self):
        """ Create a GreenT service context. Initialize the Chemotext service with that context."""
        self.service_context = ServiceContext ()
        self.chemotext = Chemotext (self.service_context)

    def get_support (self, search_string_a, search_string_b, limit=100):
        """ Get supporting articles for relationships between two MeSH terms. 
        :param search_string_a: First search term.
        :param search_string_b: Second search term.
        :param limit: Limit on size of result set.

        :rtype: List[str]
        """
        response = self.chemotext.query (
            query="MATCH (d:Term)-[r1]-(a:Art)-[r2]-(t:Term) WHERE d.name=~'%s' AND t.name=~'%s' RETURN a LIMIT %d" % (
                search_string_a, search_string_b, limit))
        articles = []
        for result in response['results']:
            for data in result['data']:
                articles += data['row']
        return articles
