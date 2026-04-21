import pytest


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # This hook helps capture if the test passed or failed
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture
def test_status(request):
    yield
    # This runs after the test completes
    report = getattr(request.node, "rep_call", None)
    if report:
        return "PASS" if report.passed else "FAIL"
    return "FAIL"

# import pytest
#
# @pytest.fixture(scope="function")
#
# def getcredentials(iteration, scope="function"):
#
#     currvalue = iteration["Username"]
#     return currvalue
#
#
# @pytest.fixture(scope="function")
# def check_status(request):
#     yield
#     # This code runs AFTER the test (teardown)
#     # Access the report stored by the hook
#     report = getattr(request.node, "rep_call", None)
#
#     if report and report.failed:
#         return report.failed
#         print(f"\nTest {request.node.nodeid} FAILED!")
#         # Example: Perform logic like taking a screenshot here
#     elif report and report.passed:
#         return report.passed
#         print(f"\nTest {request.node.nodeid} PASSED!")