import yaml

path = "data.yml"


def get_data(path):
    f = yaml.safe_load(open(path))
    print(f)


get_data(path)
