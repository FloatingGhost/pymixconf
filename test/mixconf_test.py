from pymixconf.mixconf import MixConf

def test_config_merge():
    tests = [
        ({"a": 1}, {}, {"a": 1}),
        ({"a": 1}, {"a": 2}, {"a":2}),
        ({"a": 1}, {"b": 2}, {"a": 1, "b": 2}),
        ({"a": {"b": 1}}, {"a": {"b": 2}}, {"a": {"b": 2}}),
        ({"a": {"b": 1}}, {"a": {"b": 2, "c": 3}}, {"a": {"b": 2, "c": 3}}),
        ({"a": 1}, None, {"a": 1}),
        (None, {"a": 1}, {"a": 1}),
        (None, {"a": {"b": 1}}, {"a": {"b": 1}})
    ]

    configurator = MixConf()
    for a, b, c in tests:
        print(a, b)
        assert configurator.merge_configs(a, b) == c
