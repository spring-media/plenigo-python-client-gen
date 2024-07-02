from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address_base import AddressBase


T = TypeVar("T", bound="CustomerLoginIdentifierRegistration")


@_attrs_define
class CustomerLoginIdentifierRegistration:
    """
    Attributes:
        username (Union[Unset, str]): username of the new customer
        email (Union[Unset, str]): email of the new customer
        password (Union[Unset, str]): password of the new customer
        language (Union[Unset, str]): language of the new customer
        mobile_number (Union[Unset, str]): mobile number of the new customer
        ip_address (Union[Unset, str]): IP address of the new customer
        customer_notification (Union[Unset, bool]): flag indicating if a mail or SMS should be send to the customer
        first_name (Union[Unset, str]): first name of the new customer
        last_name (Union[Unset, str]): last name of the new customer
        invoice_address (Union[Unset, AddressBase]):
        delivery_address (Union[Unset, AddressBase]):
        customer_id (Union[Unset, str]): customer id of the existing customer
        subscription_id (Union[Unset, int]): subscription id of the existing subscription - if also a customer id is
            provided the customer id must match the invoice customer
            id of the subscription
        postcode (Union[Unset, str]): postcode of a customer's address - if multiple address information are requested
            all must belong to one address
        street (Union[Unset, str]): street of a customer's address - if multiple address information are requested all
            must belong to one address
        street_number (Union[Unset, str]): street number of a customer's address - if multiple address information are
            requested all must belong to one address
        city (Union[Unset, str]): city of a customer's address - if multiple address information are requested all must
            belong to one address
    """

    username: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    password: Union[Unset, str] = UNSET
    language: Union[Unset, str] = UNSET
    mobile_number: Union[Unset, str] = UNSET
    ip_address: Union[Unset, str] = UNSET
    customer_notification: Union[Unset, bool] = UNSET
    first_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    invoice_address: Union[Unset, "AddressBase"] = UNSET
    delivery_address: Union[Unset, "AddressBase"] = UNSET
    customer_id: Union[Unset, str] = UNSET
    subscription_id: Union[Unset, int] = UNSET
    postcode: Union[Unset, str] = UNSET
    street: Union[Unset, str] = UNSET
    street_number: Union[Unset, str] = UNSET
    city: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        username = self.username

        email = self.email

        password = self.password

        language = self.language

        mobile_number = self.mobile_number

        ip_address = self.ip_address

        customer_notification = self.customer_notification

        first_name = self.first_name

        last_name = self.last_name

        invoice_address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.invoice_address, Unset):
            invoice_address = self.invoice_address.to_dict()

        delivery_address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.delivery_address, Unset):
            delivery_address = self.delivery_address.to_dict()

        customer_id = self.customer_id

        subscription_id = self.subscription_id

        postcode = self.postcode

        street = self.street

        street_number = self.street_number

        city = self.city

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if username is not UNSET:
            field_dict["username"] = username
        if email is not UNSET:
            field_dict["email"] = email
        if password is not UNSET:
            field_dict["password"] = password
        if language is not UNSET:
            field_dict["language"] = language
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
        if invoice_address is not UNSET:
            field_dict["invoiceAddress"] = invoice_address
        if delivery_address is not UNSET:
            field_dict["deliveryAddress"] = delivery_address
        if customer_id is not UNSET:
            field_dict["customerId"] = customer_id
        if subscription_id is not UNSET:
            field_dict["subscriptionId"] = subscription_id
        if postcode is not UNSET:
            field_dict["postcode"] = postcode
        if street is not UNSET:
            field_dict["street"] = street
        if street_number is not UNSET:
            field_dict["streetNumber"] = street_number
        if city is not UNSET:
            field_dict["city"] = city

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.address_base import AddressBase

        d = src_dict.copy()
        username = d.pop("username", UNSET)

        email = d.pop("email", UNSET)

        password = d.pop("password", UNSET)

        language = d.pop("language", UNSET)

        mobile_number = d.pop("mobileNumber", UNSET)

        ip_address = d.pop("ipAddress", UNSET)

        customer_notification = d.pop("customerNotification", UNSET)

        first_name = d.pop("firstName", UNSET)

        last_name = d.pop("lastName", UNSET)

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

        customer_id = d.pop("customerId", UNSET)

        subscription_id = d.pop("subscriptionId", UNSET)

        postcode = d.pop("postcode", UNSET)

        street = d.pop("street", UNSET)

        street_number = d.pop("streetNumber", UNSET)

        city = d.pop("city", UNSET)

        customer_login_identifier_registration = cls(
            username=username,
            email=email,
            password=password,
            language=language,
            mobile_number=mobile_number,
            ip_address=ip_address,
            customer_notification=customer_notification,
            first_name=first_name,
            last_name=last_name,
            invoice_address=invoice_address,
            delivery_address=delivery_address,
            customer_id=customer_id,
            subscription_id=subscription_id,
            postcode=postcode,
            street=street,
            street_number=street_number,
            city=city,
        )

        customer_login_identifier_registration.additional_properties = d
        return customer_login_identifier_registration

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
