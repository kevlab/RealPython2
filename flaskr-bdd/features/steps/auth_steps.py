from behave import *

@given(u'flaskr is setup')
def flask_is_setup(context):
    assert context.client
