import pytest

from simulant import simulant

mock_data = {
    "search_contact": [
        {
            "args": {"email": "ilya@beda.software"},
            "response": {
                "total": 1,
                "results": [
                    {
                        "id": "5901",
                        "properties": {
                            "createdate": "2021-06-21T05:12:14.718Z",
                            "email": "ilya@beda.software",
                            "firstname": "Ilya1",
                            "hs_object_id": "5901",
                            "lastmodifieddate": "2021-06-23T08:46:02.119Z",
                            "lastname": "Beda1",
                        },
                        "createdAt": "2021-06-21T05:12:14.718Z",
                        "updatedAt": "2021-06-23T08:46:02.119Z",
                        "archived": False,
                    }
                ],
            },
        }
    ],
    "load_contact": [
        {
            "args": "5901",
            "response": {
                "id": "5901",
                "properties": {
                    "createdate": "2021-06-21T05:12:14.718Z",
                    "email": "ilya@beda.software",
                    "firstname": "Ilya1",
                    "hs_object_id": "5901",
                    "lastmodifieddate": "2021-06-23T08:46:02.119Z",
                    "lastname": "Beda1",
                },
                "createdAt": "2021-06-21T05:12:14.718Z",
                "updatedAt": "2021-06-23T08:46:02.119Z",
                "archived": False,
            },
        }
    ],
}


def test_simulant():
    s = simulant.Simulant(async_mode=False)
    s.load(mock_data)

    with pytest.raises(AttributeError):
        s.unknown("foo")

    assert s.load_contact("5901")["properties"]["email"] == "ilya@beda.software"

    assert s.search_contact({"email": "ilya@beda.software"})["total"] == 1
