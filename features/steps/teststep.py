@given(u'i am on the page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given i am on the page')


@when(u'i have thi precondition')
def step_impl(context):
    raise NotImplementedError(u'STEP: When i have thi precondition')


@then(u'this should appear')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then this should appear')