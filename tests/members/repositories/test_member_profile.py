import pytest
from uuid import uuid1
from unittest.mock import MagicMock
from assertpy import assert_that
from faker import Faker
from faker.providers import phone_number, person
from sqlalchemy.orm import Session
from domain.members.models import MemberProfileDO, MemberId
from apps.repositories.members import MemberProfileRepository
from domain.members.repositories import IMemberProfileRepository
from infrastructures.persistences.sqlalchemy.models.members import MemberProfile


class TestMemberProfileRepository(object):

    @pytest.fixture(autouse=True, scope="function")
    def setup(self):
        self._faker: Faker = Faker("zh_TW")
        self._faker.add_provider(phone_number)
        self._faker.add_provider(person)

    def assert_do(self, actual_do: MemberProfileDO, expected_do: MemberProfileDO) -> None:
        assert_that(actual_do.id).is_equal_to(expected_do.id)
        assert_that(actual_do.family_name).is_equal_to(expected_do.family_name)
        assert_that(actual_do.given_name).is_equal_to(expected_do.given_name)
        assert_that(actual_do.identity_no).is_equal_to(expected_do.identity_no)
        assert_that(actual_do.cellphone).is_equal_to(expected_do.cellphone)

    def test_save_member_profile_success(self):
        # ARRANGE
        stub_session = MagicMock(spec_set=Session)
        stub_session.add = MagicMock()
        stub_session.flush = MagicMock()
        member_profile_repository = MemberProfileRepository(stub_session)

        member_do = MemberProfileDO(
            id=MagicMock(spec_set=MemberId),
            identity_no=MagicMock(spec_set=str),
            cellphone=MagicMock(spec_set=str),
            family_name=MagicMock(spec_set=str),
            given_name=MagicMock(spec_set=str)
        )
        # ACT
        result = member_profile_repository.save(member_do)

        # ASSERT
        assert_that(stub_session.add.called).is_true()
        assert_that(stub_session.flush.called).is_true()

    def test_get_member_profile_when_given_member_id(self):
        # ARRANGE
        member_id = MemberId(uuid1())
        identity = "A115454673"
        family_name = self._faker.last_name()
        given_name = self._faker.first_name()
        cellphone = self._faker.phone_number()

        expected_do = MemberProfileDO(
            id=member_id,
            identity_no=identity,
            family_name=family_name,
            given_name=given_name,
            cellphone=cellphone
        )

        fake_member_profile = MemberProfile(
            id=str(member_id),
            identity_no=identity,
            family_name=family_name,
            given_name=given_name,
            cellphone=cellphone
        )
        stub_session = MagicMock(spec_set=Session)
        stub_session.query.return_value \
            .filter.return_value \
            .scalar.return_value = fake_member_profile

        # ACT
        member_profile_repository = MemberProfileRepository(stub_session)
        actual_do = member_profile_repository.get_by(member_id)

        # ASSERT
        self.assert_do(actual_do, expected_do)
