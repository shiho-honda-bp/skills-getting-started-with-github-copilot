def test_get_activities_returns_expected_structure(client):
    # Arrange

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    body = response.json()
    assert isinstance(body, dict)
    assert "Chess Club" in body

    required_keys = {"description", "schedule", "max_participants", "participants"}
    for activity in body.values():
        assert required_keys.issubset(activity.keys())
        assert isinstance(activity["participants"], list)
