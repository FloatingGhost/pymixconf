from pymixconf.yamlconf import YamlConf
import os


def test_yamlconf():
    loader = YamlConf(config_directory="test/fixtures", environment_key="TEST_ENV")
    os.environ["TEST_ENV"] = "dev"
    data = loader.load_config()
    expected = {
        "flask": {
            "port": 6000
        },
        "logging": {
            "level": "INFO"
        },
        "custom": {
            "users": {
                "enabled": True,
                "admins": ["dave"]
            }
        }
    }
    print(data)
    assert data == expected
