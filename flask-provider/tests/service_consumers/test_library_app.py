from pact_test import state
from pact_test import pact_uri
from pact_test import has_pact_with
from pact_test import ServiceConsumerTest


@has_pact_with('Library App')
@pact_uri('/Users/kalimaha/Desktop/pact-test/tests/resources/pact_files/simple.json')
class TestLibraryApp(ServiceConsumerTest):

    @state('the breakfast is available')
    def test_get_book(self):
        pass
