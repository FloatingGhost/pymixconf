from pymixconf.jsonconf import JSONConf
import os


def test_yamlconf():
    loader = JSONConf(config_directory="test/fixtures", environment_key="TEST_ENV")
    os.environ["TEST_ENV"] = "dev"
    data = loader.load_config()
    expected = {
        "flask": {
            "port": 7000
        },
        "logging": {
            "level": "INFO"
        },
        "custom": {
            "users": {
                "enabled": True,
                "admins": ["steve"]
            }
        }
    }
    print(data)
    assert data == expected
