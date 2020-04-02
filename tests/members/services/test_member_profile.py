import pytest
from uuid import uuid1
from functools import wraps
from unittest.mock import MagicMock
from unittest.mock import patch
from assertpy import assert_that
from faker import Faker
from faker.providers import phone_number, person
from apps.datacontracts.commands.members import CreateMemberCmd, GetMemberByIdCmd
from apps.datacontracts.results.members import MemberProfileRst
from apps.repositories.members import MemberProfileRepository
from domain.members.models import MemberProfileDO, MemberId
from infrastructures.persistences.sqlalchemy import middlewares


def fake_transaction_scope(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as ex:
            raise ex
    return decorator


class TestMemberProfileService(object):

    @pytest.fixture(autouse=True, scope="function")
    def setup(self):
        self._faker: Faker = Faker("zh_TW")
        self._faker.add_provider(phone_number)
        self._faker.add_provider(person)

    def test_create_member_profile_when_given_create_data(self):
        # ARRANGE
        member_id = MemberId(uuid1())
        identity = "A115454673"
        family_name = self._faker.last_name()
        given_name = self._faker.first_name()
        cellphone = self._faker.phone_number()

        command = CreateMemberCmd(
            identity_no=identity,
            cellphone=cellphone,
            family_name=family_name,
            given_name=given_name,

        )

        expected_result = MemberProfileRst(
            member_id=str(member_id),
            identity_no=identity,
            family_name=family_name,
            given_name=given_name,
            cellphone=cellphone,
        )

        stub_repository = MagicMock(spec_set=MemberProfileRepository)
        stub_repository.save = MagicMock()
        stub_repository.generate_id = MagicMock(return_value=member_id)

        # Mock transaction_scope
        # NOTE: 如果要 Mock 裝飾器，需要透過 module 載入來 Mock 原本的裝飾器方法/類別，然後再載入要使用的對象類別/方法
        middlewares.transaction_scope = MagicMock(side_effect=fake_transaction_scope)
        from apps.services.members import MemberProfileService
        # Initialize
        member_profile_service = MemberProfileService()
        member_profile_service._member_profile_repository = stub_repository

        # ACT
        actual_result = member_profile_service.create(command)

        # ASSERT
        assert_that(actual_result.member_id).is_equal_to(expected_result.member_id)
        assert_that(actual_result.identity_no).is_equal_to(expected_result.identity_no)
        assert_that(actual_result.cellphone).is_equal_to(expected_result.cellphone)
        assert_that(actual_result.family_name).is_equal_to(expected_result.family_name)
        assert_that(actual_result.given_name).is_equal_to(expected_result.given_name)

    def test_get_member_profile_when_given_member_id(self):
        # ARRANGE
        member_id = MemberId(uuid1())
        identity = "A115454673"
        family_name = self._faker.last_name()
        given_name = self._faker.first_name()
        cellphone = self._faker.phone_number()

        command = GetMemberByIdCmd(member_id=str(member_id))

        member_do = MemberProfileDO(
            id=member_id,
            identity_no=identity,
            family_name=family_name,
            given_name=given_name,
            cellphone=cellphone,
        )

        expected_result = MemberProfileRst(
            member_id=str(member_id),
            identity_no=identity,
            family_name=family_name,
            given_name=given_name,
            cellphone=cellphone,
        )

        stub_repository = MagicMock(spec_set=MemberProfileRepository)
        stub_repository.get_by = MagicMock(return_value=member_do)

        from apps.services.members import MemberProfileService
        member_profile_service = MemberProfileService()
        member_profile_service._member_profile_repository = stub_repository
        # ACT
        actual_result = member_profile_service.get(command) 

        # ASSERT
        assert_that(actual_result.member_id).is_equal_to(expected_result.member_id)
        assert_that(actual_result.identity_no).is_equal_to(expected_result.identity_no)
        assert_that(actual_result.cellphone).is_equal_to(expected_result.cellphone)
        assert_that(actual_result.family_name).is_equal_to(expected_result.family_name)
        assert_that(actual_result.given_name).is_equal_to(expected_result.given_name)
