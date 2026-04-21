import pytest
from utils import excel_reader
from utils.execute_keyword import KeywordExecutor

# Path to your Excel file (.xls))
EXCEL_PATH = r"C:\Users\USER\PycharmProjects\GuviDatanKeywdDriven_OrangeHRM\testdata\orangehrm_teststeps.xlsx"


@pytest.mark.parametrize("user_row", excel_reader.get_login_data(EXCEL_PATH))
def test_orangehrm_login_workflow(user_row):

    executor = KeywordExecutor()
    steps = excel_reader.get_test_steps(EXCEL_PATH)
    status = "Passed"  # Default status

    try:
        for step in steps:
            #current user's credentials
            executor.execute(step, user_row)

    except Exception as e:
        print(f"\n[ERROR] Test failed for {user_row['Username']}: {e}")
        status = "Failed"

    finally:
        # Update Excel with Date, Time, and Status
        excel_reader.update_excel_result(
            EXCEL_PATH,
            user_row['Test_id'],
            user_row['Username'],
            status
        )


        if executor.keywords.driver:
            executor.keywords.close_browser()

    # Final assertion
    assert status == "Passed", f"Login test failed for user: {user_row['Username']}"


if __name__ == "__main__":
    pytest.main(["-v", "--html=report.html"])

