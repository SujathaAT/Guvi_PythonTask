import yaml


def yaml_load():
    User_details = []
    with open("C:\\Users\\USER\\PycharmProjects\\ZenPortalPlaywright\\testdata\\zenportal.yaml", "r") as f:
        creds =  yaml.safe_load(f)

        login_data = creds['user']

        email = login_data['email']
        pwd = login_data['password']
        return email+":" +pwd
