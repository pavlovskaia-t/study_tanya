import pytest
import logging
from homework11.homework_10 import log_event

class TestLogEvent:
    def test_success(self):
        log_event("Tom", "success")
        with open("login_system.log", "r") as f:
            contents = f.read()
        assert "Username: Tom, Status: success" in contents

    def test_expired(self):
        log_event("Tom", "expired")
        with open("login_system.log", "r") as f:
            contents = f.read()
        assert "Username: Tom, Status: expired" in contents

    def test_failed(self):
        log_event("Tom", "failed")
        with open("login_system.log", "r") as f:
            contents = f.read()
        assert "Username: Tom, Status: failed" in contents