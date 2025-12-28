import yaml


def yaml_load():
    User_details = []
    with open("C:\\Users\\USER\\PycharmProjects\\Guvi_POM_ZenPortalAuthentication\\utiils\\Zen_data.yaml", "r") as f:
        creds =  yaml.safe_load(f)

        login_data = creds['user']

        email = login_data['email']
        pwd = login_data['password']
        return email+":" +pwd


def fetch_creds():
    get_creds = yaml_load()
    print(get_creds)

    creds = get_creds.split(":")
    fetch_creds = (creds[0], creds[1])