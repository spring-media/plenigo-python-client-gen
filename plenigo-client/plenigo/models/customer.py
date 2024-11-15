import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.customer_base_salutation import CustomerBaseSalutation
from ..models.customer_customer_marks_item import CustomerCustomerMarksItem
from ..models.customer_sso_login_providers_item import CustomerSsoLoginProvidersItem
from ..models.customer_status import CustomerStatus
from ..models.user_type import UserType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.customer_accepted_terms import CustomerAcceptedTerms
    from ..models.customer_miscellaneous_data import CustomerMiscellaneousData


T = TypeVar("T", bound="Customer")


@_attrs_define
class Customer:
    """
    Attributes:
        customer_id (str): unique id of the customer
        username (Union[Unset, str]): selected username of the customer that is unique for all users
        email (Union[Unset, str]): email address of the customer that is unique for all users
        external_system_id (Union[Unset, str]): external system id - can only be set if not set yet
        salutation (Union[Unset, CustomerBaseSalutation]): salutation to identify the correct designation of a customer
        first_name (Union[Unset, str]): first name of the customer - first name and last name or company name are
            required
        last_name (Union[Unset, str]): last name of the customer - first name and last name or company name are required
        invoice_email (Union[Unset, str]): email address of the customer where invoices should be sent to
        language (Union[Unset, str]): language of the customer - two letter language code according to <a
            href="https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes" target="_blank">ISO 639-1</a>
        mobile_number (Union[Unset, str]): mobile number of the customer formatted as <a
            href="https://en.wikipedia.org/wiki/E.164" target="_blank">E.164</a>
        birthday (Union[None, Unset, datetime.date]): birthday of the customer with full-date notation as defined by <a
            href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for example,
            2017-07-01
        miscellaneous_data (Union[Unset, CustomerMiscellaneousData]):
        created_date (Union[None, Unset, datetime.datetime]): time the object was created with time notation as defined
            by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for
            example, 17:32:28
        changed_date (Union[None, Unset, datetime.datetime]): time the object was changed with time notation as defined
            by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for
            example, 17:32:28
        created_by (Union[Unset, str]): id who created the object
        created_by_type (Union[Unset, UserType]): type of user who performs the action
        changed_by (Union[Unset, str]): id who changed the object
        changed_by_type (Union[Unset, UserType]): type of user who performs the action
        registration_source (Union[Unset, str]): source the user registration was started from
        registration_date (Union[None, Unset, datetime.datetime]): date the customer was registered with date-time
            notation as defined by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339,
            section 5.6</a>, for example, 2017-07-21T17:32:28Z
        age_verification_pin_enabled (Union[Unset, bool]): flag indicating that age verification pin is set
        status (Union[Unset, CustomerStatus]): status of the customer

            | Status      | Description
            |
            | ----------- | ------------------------------------------------------------------------------------------------
            ----------------------------------------------------------|
            | ACTIVATED   | customer is active and can log in and use full functionality
            |
            | BLOCKED     | customer is blocked and needs to reset his password to be able to log in again
            |
            | DEACTIVATED | customer is deactivated and cannot log in - the customer cannot change this state by himself and
            a log in attempt is handled like a false password log in |
            | DISABLED    | customer is disabled by plenigo and cannot be used anymore - please contact plenigo for further
            information (this status is currently not actively used)  |
        accepted_terms (Union[Unset, CustomerAcceptedTerms]):
        sso_login_providers (Union[Unset, List[CustomerSsoLoginProvidersItem]]):
        customer_marks (Union[Unset, List[CustomerCustomerMarksItem]]):
    """

    customer_id: str
    username: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    external_system_id: Union[Unset, str] = UNSET
    salutation: Union[Unset, CustomerBaseSalutation] = UNSET
    first_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    invoice_email: Union[Unset, str] = UNSET
    language: Union[Unset, str] = UNSET
    mobile_number: Union[Unset, str] = UNSET
    birthday: Union[None, Unset, datetime.date] = UNSET
    miscellaneous_data: Union[Unset, "CustomerMiscellaneousData"] = UNSET
    created_date: Union[None, Unset, datetime.datetime] = UNSET
    changed_date: Union[None, Unset, datetime.datetime] = UNSET
    created_by: Union[Unset, str] = UNSET
    created_by_type: Union[Unset, UserType] = UNSET
    changed_by: Union[Unset, str] = UNSET
    changed_by_type: Union[Unset, UserType] = UNSET
    registration_source: Union[Unset, str] = UNSET
    registration_date: Union[None, Unset, datetime.datetime] = UNSET
    age_verification_pin_enabled: Union[Unset, bool] = UNSET
    status: Union[Unset, CustomerStatus] = UNSET
    accepted_terms: Union[Unset, "CustomerAcceptedTerms"] = UNSET
    sso_login_providers: Union[Unset, List[CustomerSsoLoginProvidersItem]] = UNSET
    customer_marks: Union[Unset, List[CustomerCustomerMarksItem]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        customer_id = self.customer_id

        username = self.username

        email = self.email

        external_system_id = self.external_system_id

        salutation: Union[Unset, str] = UNSET
        if not isinstance(self.salutation, Unset):
            salutation = self.salutation.value

        first_name = self.first_name

        last_name = self.last_name

        invoice_email = self.invoice_email

        language = self.language

        mobile_number = self.mobile_number

        birthday: Union[None, Unset, str]
        if isinstance(self.birthday, Unset) or self.birthday is None:
            birthday = UNSET
        elif isinstance(self.birthday, datetime.date):
            birthday = self.birthday.isoformat()
        else:
            birthday = self.birthday

        miscellaneous_data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.miscellaneous_data, Unset):
            miscellaneous_data = self.miscellaneous_data.to_dict()

        created_date: Union[None, Unset, str]
        if isinstance(self.created_date, Unset) or self.created_date is None:
            created_date = UNSET
        elif isinstance(self.created_date, datetime.datetime):
            created_date = self.created_date.isoformat()
        else:
            created_date = self.created_date

        changed_date: Union[None, Unset, str]
        if isinstance(self.changed_date, Unset) or self.changed_date is None:
            changed_date = UNSET
        elif isinstance(self.changed_date, datetime.datetime):
            changed_date = self.changed_date.isoformat()
        else:
            changed_date = self.changed_date

        created_by = self.created_by

        created_by_type: Union[Unset, str] = UNSET
        if not isinstance(self.created_by_type, Unset):
            created_by_type = self.created_by_type.value

        changed_by = self.changed_by

        changed_by_type: Union[Unset, str] = UNSET
        if not isinstance(self.changed_by_type, Unset):
            changed_by_type = self.changed_by_type.value

        registration_source = self.registration_source

        registration_date: Union[None, Unset, str]
        if isinstance(self.registration_date, Unset) or self.registration_date is None:
            registration_date = UNSET
        elif isinstance(self.registration_date, datetime.datetime):
            registration_date = self.registration_date.isoformat()
        else:
            registration_date = self.registration_date

        age_verification_pin_enabled = self.age_verification_pin_enabled

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        accepted_terms: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.accepted_terms, Unset):
            accepted_terms = self.accepted_terms.to_dict()

        sso_login_providers: Union[Unset, List[str]] = UNSET
        if not isinstance(self.sso_login_providers, Unset):
            sso_login_providers = []
            for sso_login_providers_item_data in self.sso_login_providers:
                sso_login_providers_item = sso_login_providers_item_data.value
                sso_login_providers.append(sso_login_providers_item)

        customer_marks: Union[Unset, List[str]] = UNSET
        if not isinstance(self.customer_marks, Unset):
            customer_marks = []
            for customer_marks_item_data in self.customer_marks:
                customer_marks_item = customer_marks_item_data.value
                customer_marks.append(customer_marks_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "customerId": customer_id,
            }
        )
        if username is not UNSET:
            field_dict["username"] = username
        if email is not UNSET:
            field_dict["email"] = email
        if external_system_id is not UNSET:
            field_dict["externalSystemId"] = external_system_id
        if salutation is not UNSET:
            field_dict["salutation"] = salutation
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if invoice_email is not UNSET:
            field_dict["invoiceEmail"] = invoice_email
        if language is not UNSET:
            field_dict["language"] = language
        if mobile_number is not UNSET:
            field_dict["mobileNumber"] = mobile_number
        if birthday is not UNSET:
            field_dict["birthday"] = birthday
        if miscellaneous_data is not UNSET:
            field_dict["miscellaneousData"] = miscellaneous_data
        if created_date is not UNSET:
            field_dict["createdDate"] = created_date
        if changed_date is not UNSET:
            field_dict["changedDate"] = changed_date
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if created_by_type is not UNSET:
            field_dict["createdByType"] = created_by_type
        if changed_by is not UNSET:
            field_dict["changedBy"] = changed_by
        if changed_by_type is not UNSET:
            field_dict["changedByType"] = changed_by_type
        if registration_source is not UNSET:
            field_dict["registrationSource"] = registration_source
        if registration_date is not UNSET:
            field_dict["registrationDate"] = registration_date
        if age_verification_pin_enabled is not UNSET:
            field_dict["ageVerificationPinEnabled"] = age_verification_pin_enabled
        if status is not UNSET:
            field_dict["status"] = status
        if accepted_terms is not UNSET:
            field_dict["acceptedTerms"] = accepted_terms
        if sso_login_providers is not UNSET:
            field_dict["ssoLoginProviders"] = sso_login_providers
        if customer_marks is not UNSET:
            field_dict["customerMarks"] = customer_marks

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.customer_accepted_terms import CustomerAcceptedTerms
        from ..models.customer_miscellaneous_data import CustomerMiscellaneousData

        d = src_dict.copy()
        customer_id = d.pop("customerId")

        username = d.pop("username", UNSET)

        email = d.pop("email", UNSET)

        external_system_id = d.pop("externalSystemId", UNSET)

        _salutation = d.pop("salutation", UNSET)
        salutation: Union[Unset, CustomerBaseSalutation]
        if isinstance(_salutation, Unset) or not _salutation:
            salutation = UNSET
        else:
            salutation = CustomerBaseSalutation(_salutation)

        first_name = d.pop("firstName", UNSET)

        last_name = d.pop("lastName", UNSET)

        invoice_email = d.pop("invoiceEmail", UNSET)

        language = d.pop("language", UNSET)

        mobile_number = d.pop("mobileNumber", UNSET)

        def _parse_birthday(data: object) -> Union[None, Unset, datetime.date]:
            if data is None:
                return data

            if data is None:
                return data

            if isinstance(data, Unset):
                return data

            # Try to parse the data as datetime.date
            try:
                if not isinstance(data, str):
                    raise TypeError()
                birthday_type_0 = isoparse(data).date()

                return birthday_type_0
            except:  # noqa: E722
                pass

            return cast(Union[None, Unset, datetime.date], data)

        birthday = _parse_birthday(d.pop("birthday", UNSET))

        _miscellaneous_data = d.pop("miscellaneousData", UNSET)
        miscellaneous_data: Union[Unset, CustomerMiscellaneousData]
        if isinstance(_miscellaneous_data, Unset) or not _miscellaneous_data:
            miscellaneous_data = UNSET
        else:
            miscellaneous_data = CustomerMiscellaneousData.from_dict(_miscellaneous_data)

        def _parse_created_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data

            if data is None:
                return data

            if isinstance(data, Unset):
                return data

            # Try to parse the data as datetime.datetime
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_date_type_0 = isoparse(data)

                return created_date_type_0
            except:  # noqa: E722
                pass

            return cast(Union[None, Unset, datetime.datetime], data)

        created_date = _parse_created_date(d.pop("createdDate", UNSET))

        def _parse_changed_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data

            if data is None:
                return data

            if isinstance(data, Unset):
                return data

            # Try to parse the data as datetime.datetime
            try:
                if not isinstance(data, str):
                    raise TypeError()
                changed_date_type_0 = isoparse(data)

                return changed_date_type_0
            except:  # noqa: E722
                pass

            return cast(Union[None, Unset, datetime.datetime], data)

        changed_date = _parse_changed_date(d.pop("changedDate", UNSET))

        created_by = d.pop("createdBy", UNSET)

        _created_by_type = d.pop("createdByType", UNSET)
        created_by_type: Union[Unset, UserType]
        if isinstance(_created_by_type, Unset) or not _created_by_type:
            created_by_type = UNSET
        else:
            created_by_type = UserType(_created_by_type)

        changed_by = d.pop("changedBy", UNSET)

        _changed_by_type = d.pop("changedByType", UNSET)
        changed_by_type: Union[Unset, UserType]
        if isinstance(_changed_by_type, Unset) or not _changed_by_type:
            changed_by_type = UNSET
        else:
            changed_by_type = UserType(_changed_by_type)

        registration_source = d.pop("registrationSource", UNSET)

        def _parse_registration_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data

            if data is None:
                return data

            if isinstance(data, Unset):
                return data

            # Try to parse the data as datetime.datetime
            try:
                if not isinstance(data, str):
                    raise TypeError()
                registration_date_type_0 = isoparse(data)

                return registration_date_type_0
            except:  # noqa: E722
                pass

            return cast(Union[None, Unset, datetime.datetime], data)

        registration_date = _parse_registration_date(d.pop("registrationDate", UNSET))

        age_verification_pin_enabled = d.pop("ageVerificationPinEnabled", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, CustomerStatus]
        if isinstance(_status, Unset) or not _status:
            status = UNSET
        else:
            status = CustomerStatus(_status)

        _accepted_terms = d.pop("acceptedTerms", UNSET)
        accepted_terms: Union[Unset, CustomerAcceptedTerms]
        if isinstance(_accepted_terms, Unset) or not _accepted_terms:
            accepted_terms = UNSET
        else:
            accepted_terms = CustomerAcceptedTerms.from_dict(_accepted_terms)

        sso_login_providers = []
        _sso_login_providers = d.pop("ssoLoginProviders", UNSET)
        for sso_login_providers_item_data in _sso_login_providers or []:
            sso_login_providers_item = CustomerSsoLoginProvidersItem(sso_login_providers_item_data)

            sso_login_providers.append(sso_login_providers_item)

        customer_marks = []
        _customer_marks = d.pop("customerMarks", UNSET)
        for customer_marks_item_data in _customer_marks or []:
            customer_marks_item = CustomerCustomerMarksItem(customer_marks_item_data)

            customer_marks.append(customer_marks_item)

        customer = cls(
            customer_id=customer_id,
            username=username,
            email=email,
            external_system_id=external_system_id,
            salutation=salutation,
            first_name=first_name,
            last_name=last_name,
            invoice_email=invoice_email,
            language=language,
            mobile_number=mobile_number,
            birthday=birthday,
            miscellaneous_data=miscellaneous_data,
            created_date=created_date,
            changed_date=changed_date,
            created_by=created_by,
            created_by_type=created_by_type,
            changed_by=changed_by,
            changed_by_type=changed_by_type,
            registration_source=registration_source,
            registration_date=registration_date,
            age_verification_pin_enabled=age_verification_pin_enabled,
            status=status,
            accepted_terms=accepted_terms,
            sso_login_providers=sso_login_providers,
            customer_marks=customer_marks,
        )

        customer.additional_properties = d
        return customer

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
