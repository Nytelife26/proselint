"""Test garner.dates."""
from proselint import logger
from proselint.checks.dates_times import dates

from .check import Check


class TestCheck(Check):
    """Test class for garner.dates."""

    __test__ = True

    def test_50s_hyphenation(self):
        """Find unneeded hyphen in 50's."""
        text = """The 50's were swell."""
        results = dates.check_decade_apostrophes_short(text)
        assert len(results) == 1

    def test_50_Cent_hyphenation(self):
        """Don't flag 50's when it refers to 50 Cent's manager."""
        text = """
            Dr. Dre suggested to 50's manager that he look into signing
            Eminem to the G-Unit record label.
        """
        results = dates.check_decade_apostrophes_short(text)
        assert len(results) == 0

    def test_dash_and_from(self):
        """Test garner.check_dash_and_from."""
        text = """From 1999-2002, Sally served as chair of the committee."""
        results = dates.check_dash_and_from(text)
        logger.info(results)
        assert len(results) == 1
