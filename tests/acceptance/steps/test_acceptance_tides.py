from pytest_bdd import scenario, given, when, then


@scenario('tides.feature', 'Hello')
def test_api_connection():
    pass


@given('an API exists in the environment')
def api_exists():
    obj = {'hello': 'hi'}
    return obj


@when('a user requests data from admiralty api')
def attempt_connection(api):
    api.get("bye") == 'hi'


@then('the library successfully communicates with the third party API')
def successful_connection_response(api):
    assert api.get('bye') == 'hi'
