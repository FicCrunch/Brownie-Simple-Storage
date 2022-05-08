from brownie import SimpleStorage, accounts, network, config


def test_deploy():
    # Arrange
    account = accounts[0]

    # Act
    simple_storage = SimpleStorage.deploy({"from": account})
    starting_value = simple_storage.retrieve()
    expected = 0

    # Assert
    assert starting_value == expected


def test_updating_storage():

    #  arrange
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})

    # act
    expected = 15
    simple_storage.store(expected, {"from": account})

    # assert
    assert expected == simple_storage.retrieve()
