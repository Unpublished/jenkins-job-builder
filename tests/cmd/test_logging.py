import importlib
import logging
import pytest
import sys

from jenkins_jobs.cli import entry


def test_no_basic_config_on_import(monkeypatch, mocker):
    """
    Verify that JJB does not initialize logging upon import
    """

    module_name = "jenkins_jobs.cli.entry"

    monkeypatch.delitem(sys.modules, module_name, raising=False)

    mocked_basic_config = mocker.patch.object(logging, "basicConfig")

    importlib.import_module(module_name)

    mocked_basic_config.assert_not_called()


def test_main_logs_info(monkeypatch, caplog):
    """
    Verify that entry.main() still outputs INFO messages.
    """

    monkeypatch.setattr(sys, "argv", ["jenkins-jobs", "list"])

    with pytest.raises(IOError):
        entry.main()

    assert any(record.levelno == logging.INFO for record in caplog.records)
