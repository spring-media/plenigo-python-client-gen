import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.customer_base_salutation import CustomerBaseSalutation
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.customer_miscellaneous_data import CustomerMiscellaneousData


T = TypeVar("T", bound="CustomerBase")


@_attrs_define
class CustomerBase:
    """
    Attributes:
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
        birthday (Union[None, Unset, datetime.datetime]): birthday of the customer with full-date notation as defined by
            <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for
            example, 2017-07-01
        miscellaneous_data (Union[Unset, CustomerMiscellaneousData]):
    """

    username: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    external_system_id: Union[Unset, str] = UNSET
    salutation: Union[Unset, CustomerBaseSalutation] = UNSET
    first_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    invoice_email: Union[Unset, str] = UNSET
    language: Union[Unset, str] = UNSET
    mobile_number: Union[Unset, str] = UNSET
    birthday: Union[None, Unset, datetime.datetime] = UNSET
    miscellaneous_data: Union[Unset, "CustomerMiscellaneousData"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
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
        if isinstance(self.birthday, Unset):
            birthday = UNSET
        elif isinstance(self.birthday, datetime.datetime):
            birthday = self.birthday.isoformat()
        else:
            birthday = self.birthday

        miscellaneous_data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.miscellaneous_data, Unset):
            miscellaneous_data = self.miscellaneous_data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.customer_miscellaneous_data import CustomerMiscellaneousData

        d = src_dict.copy()
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

        def _parse_birthday(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                birthday_type_0 = isoparse(data)

                return birthday_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        birthday = _parse_birthday(d.pop("birthday", UNSET))

        _miscellaneous_data = d.pop("miscellaneousData", UNSET)
        miscellaneous_data: Union[Unset, CustomerMiscellaneousData]
        if isinstance(_miscellaneous_data, Unset) or not _miscellaneous_data:
            miscellaneous_data = UNSET
        else:
            miscellaneous_data = CustomerMiscellaneousData.from_dict(_miscellaneous_data)

        customer_base = cls(
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
        )

        customer_base.additional_properties = d
        return customer_base

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
