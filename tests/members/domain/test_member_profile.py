from assertpy import assert_that
import pytest
from uuid import uuid1
from faker import Faker
from faker.providers import phone_number, person
from domain.members.models import MemberProfileDO, MemberId


class TestMemberProfileDO(object):

    @pytest.fixture(autouse=True, scope="function")
    def setup(self):
        self._fake: Faker = Faker("zh_TW")
        self._fake.add_provider(phone_number)
        self._fake.add_provider(person)

    def assert_do(self, actual_do: MemberProfileDO, expected_do: MemberProfileDO) -> None:
        assert_that(actual_do.id).is_equal_to(expected_do.id)
        assert_that(actual_do.family_name).is_equal_to(expected_do.family_name)
        assert_that(actual_do.given_name).is_equal_to(expected_do.given_name)
        assert_that(actual_do.identity_no).is_equal_to(expected_do.identity_no)
        assert_that(actual_do.cellphone).is_equal_to(expected_do.cellphone)

    def test_member_created(self) -> None:
        # Arrange
        member_id = MemberId(uuid1())
        identity = "A115454673"
        family_name = self._fake.last_name()
        given_name = self._fake.first_name()
        cellphone = self._fake.phone_number()

        actual_do = MemberProfileDO(
            id=member_id,
            identity_no=identity,
            cellphone=cellphone,
            family_name=family_name,
            given_name=given_name,
        )

        assert_that(actual_do.id).is_equal_to(member_id)
        assert_that(actual_do.identity_no).is_equal_to(identity)
        assert_that(actual_do.family_name).is_equal_to(family_name)
        assert_that(actual_do.given_name).is_equal_to(given_name)
        assert_that(actual_do.cellphone).is_equal_to(cellphone)
