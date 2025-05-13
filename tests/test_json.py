import json

from gendiff.formatters.json import format_json


def test_format_json():
    data = {
        "name": "Alice",
        "age": 30,
        "city": "Wonderland",
        "skills": ["Python", "JavaScript", "C++"]
    }

    expected_output = json.dumps(data, indent=4, ensure_ascii=False)

    actual_output = format_json(data)
    assert actual_output == expected_output, (
        f"Expected:\n{expected_output}\n"
        f"But got:\n{actual_output}"
    )


if __name__ == "__main__":
    test_format_json()
    print("Test passed!")