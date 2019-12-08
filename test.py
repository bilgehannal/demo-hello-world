import message


def test_message():
    warning = "Message should be 'Hello World'"
    assert "Hello" in message.get_message(), warning


if __name__ == "__main__":
    test_message()
    print("Everything passed")
