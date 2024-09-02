import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.customer_base_salutation import CustomerBaseSalutation
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.additional_customer_data import AdditionalCustomerData
    from ..models.customer_address_creation import CustomerAddressCreation
    from ..models.customer_miscellaneous_data import CustomerMiscellaneousData


T = TypeVar("T", bound="CustomerCreation")


@_attrs_define
class CustomerCreation:
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
        pseudo_email (Union[Unset, bool]): flag indicating that email should be a pseudo email
        password (Union[Unset, str]): new password of the user - if left empty the old password will be kept
        processing_blocked (Union[Unset, bool]): Flag to indicate to third party systems that the customer is blocked
            for further processing and should not be used for advertisement, etc. Can be used in combination with the
            pseudoEmail flag to handle data protection requests without deletion of a customer.
        customer_id (Union[Unset, str]): unique id of the customer
        registration_source (Union[Unset, str]): domain, website, app or other source of the customer registration
        send_welcome_mail (Union[Unset, bool]): flag indicating if welcome mail for customer should be sent
        addresses (Union[Unset, List['CustomerAddressCreation']]): addresses that should be directly associated with the
            customer
        data (Union[Unset, AdditionalCustomerData]):
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
    pseudo_email: Union[Unset, bool] = UNSET
    password: Union[Unset, str] = UNSET
    processing_blocked: Union[Unset, bool] = UNSET
    customer_id: Union[Unset, str] = UNSET
    registration_source: Union[Unset, str] = UNSET
    send_welcome_mail: Union[Unset, bool] = UNSET
    addresses: Union[Unset, List["CustomerAddressCreation"]] = UNSET
    data: Union[Unset, "AdditionalCustomerData"] = UNSET
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
        if isinstance(self.birthday, Unset) or self.birthday is None:
            birthday = UNSET
        elif isinstance(self.birthday, datetime.datetime):
            birthday = self.birthday.isoformat()
        else:
            birthday = self.birthday

        miscellaneous_data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.miscellaneous_data, Unset):
            miscellaneous_data = self.miscellaneous_data.to_dict()

        pseudo_email = self.pseudo_email

        password = self.password

        processing_blocked = self.processing_blocked

        customer_id = self.customer_id

        registration_source = self.registration_source

        send_welcome_mail = self.send_welcome_mail

        addresses: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.addresses, Unset):
            addresses = []
            for addresses_item_data in self.addresses:
                addresses_item = addresses_item_data.to_dict()
                addresses.append(addresses_item)

        data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

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
        if pseudo_email is not UNSET:
            field_dict["pseudoEmail"] = pseudo_email
        if password is not UNSET:
            field_dict["password"] = password
        if processing_blocked is not UNSET:
            field_dict["processingBlocked"] = processing_blocked
        if customer_id is not UNSET:
            field_dict["customerId"] = customer_id
        if registration_source is not UNSET:
            field_dict["registrationSource"] = registration_source
        if send_welcome_mail is not UNSET:
            field_dict["sendWelcomeMail"] = send_welcome_mail
        if addresses is not UNSET:
            field_dict["addresses"] = addresses
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.additional_customer_data import AdditionalCustomerData
        from ..models.customer_address_creation import CustomerAddressCreation
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

            if data is None:
                return data

            if isinstance(data, Unset):
                return data

            # Try to parse the data as datetime.datetime
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

        pseudo_email = d.pop("pseudoEmail", UNSET)

        password = d.pop("password", UNSET)

        processing_blocked = d.pop("processingBlocked", UNSET)

        customer_id = d.pop("customerId", UNSET)

        registration_source = d.pop("registrationSource", UNSET)

        send_welcome_mail = d.pop("sendWelcomeMail", UNSET)

        addresses = []
        _addresses = d.pop("addresses", UNSET)
        for addresses_item_data in _addresses or []:
            addresses_item = CustomerAddressCreation.from_dict(addresses_item_data)

            addresses.append(addresses_item)

        _data = d.pop("data", UNSET)
        data: Union[Unset, AdditionalCustomerData]
        if isinstance(_data, Unset) or not _data:
            data = UNSET
        else:
            data = AdditionalCustomerData.from_dict(_data)

        customer_creation = cls(
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
            pseudo_email=pseudo_email,
            password=password,
            processing_blocked=processing_blocked,
            customer_id=customer_id,
            registration_source=registration_source,
            send_welcome_mail=send_welcome_mail,
            addresses=addresses,
            data=data,
        )

        customer_creation.additional_properties = d
        return customer_creation

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
