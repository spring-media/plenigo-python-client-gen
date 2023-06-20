from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address_base import AddressBase


T = TypeVar("T", bound="CustomerRegistrationCreation")


@attr.s(auto_attribs=True)
class CustomerRegistrationCreation:
    """
    Attributes:
        email (str): email of the new customer
        password (str): password of the new customer
        language (str): language of the new customer
        username (Union[Unset, str]): username of the new customer
        mobile_number (Union[Unset, str]): mobile number of the new customer
        ip_address (Union[Unset, str]): IP address of the new customer
        customer_notification (Union[Unset, bool]): flag indicating if a mail or SMS should be send to the customer.
        first_name (Union[Unset, str]): first name of the new customer
        last_name (Union[Unset, str]): last name of the new customer
        verification_url (Union[Unset, str]): url to verify registration - if provided two parameters are added to the
            url (token and step) and it is passed to the registration mail.
            This way the application that embeds the plenigo registration from can handle a user verification via link
            instead of a token process.
        invoice_address (Union[Unset, AddressBase]):
        delivery_address (Union[Unset, AddressBase]):
    """

    email: str
    password: str
    language: str
    username: Union[Unset, str] = UNSET
    mobile_number: Union[Unset, str] = UNSET
    ip_address: Union[Unset, str] = UNSET
    customer_notification: Union[Unset, bool] = UNSET
    first_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    verification_url: Union[Unset, str] = UNSET
    invoice_address: Union[Unset, "AddressBase"] = UNSET
    delivery_address: Union[Unset, "AddressBase"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        email = self.email
        password = self.password
        language = self.language
        username = self.username
        mobile_number = self.mobile_number
        ip_address = self.ip_address
        customer_notification = self.customer_notification
        first_name = self.first_name
        last_name = self.last_name
        verification_url = self.verification_url
        invoice_address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.invoice_address, Unset):
            invoice_address = self.invoice_address.to_dict()

        delivery_address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.delivery_address, Unset):
            delivery_address = self.delivery_address.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
                "password": password,
                "language": language,
            }
        )
        if username is not UNSET:
            field_dict["username"] = username
        if mobile_number is not UNSET:
            field_dict["mobileNumber"] = mobile_number
        if ip_address is not UNSET:
            field_dict["ipAddress"] = ip_address
        if customer_notification is not UNSET:
            field_dict["customerNotification"] = customer_notification
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if verification_url is not UNSET:
            field_dict["verificationUrl"] = verification_url
        if invoice_address is not UNSET:
            field_dict["invoiceAddress"] = invoice_address
        if delivery_address is not UNSET:
            field_dict["deliveryAddress"] = delivery_address

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.address_base import AddressBase

        d = src_dict.copy()
        email = d.pop("email")

        password = d.pop("password")

        language = d.pop("language")

        username = d.pop("username", UNSET)

        mobile_number = d.pop("mobileNumber", UNSET)

        ip_address = d.pop("ipAddress", UNSET)

        customer_notification = d.pop("customerNotification", UNSET)

        first_name = d.pop("firstName", UNSET)

        last_name = d.pop("lastName", UNSET)

        verification_url = d.pop("verificationUrl", UNSET)

        _invoice_address = d.pop("invoiceAddress", UNSET)
        invoice_address: Union[Unset, AddressBase]
        if isinstance(_invoice_address, Unset):
            invoice_address = UNSET
        else:
            invoice_address = AddressBase.from_dict(_invoice_address)

        _delivery_address = d.pop("deliveryAddress", UNSET)
        delivery_address: Union[Unset, AddressBase]
        if isinstance(_delivery_address, Unset):
            delivery_address = UNSET
        else:
            delivery_address = AddressBase.from_dict(_delivery_address)

        customer_registration_creation = cls(
            email=email,
            password=password,
            language=language,
            username=username,
            mobile_number=mobile_number,
            ip_address=ip_address,
            customer_notification=customer_notification,
            first_name=first_name,
            last_name=last_name,
            verification_url=verification_url,
            invoice_address=invoice_address,
            delivery_address=delivery_address,
        )

        customer_registration_creation.additional_properties = d
        return customer_registration_creation

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
