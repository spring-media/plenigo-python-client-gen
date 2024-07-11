from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.corporate_account_user_creation_salutation import CorporateAccountUserCreationSalutation

T = TypeVar("T", bound="CorporateAccountUserCreation")


@_attrs_define
class CorporateAccountUserCreation:
    """
    Attributes:
        email (str): email address of the customer that should belong to this corporate account user
        salutation (CorporateAccountUserCreationSalutation): salutation to identify the correct designation of a
            customer
        first_name (str): first name of the customer - first name and last name or company name are required
        last_name (str): last name of the customer - first name and last name or company name are required
    """

    email: str
    salutation: CorporateAccountUserCreationSalutation
    first_name: str
    last_name: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        email = self.email

        salutation = self.salutation.value

        first_name = self.first_name

        last_name = self.last_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
                "salutation": salutation,
                "firstName": first_name,
                "lastName": last_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        email = d.pop("email")

        salutation = CorporateAccountUserCreationSalutation(d.pop("salutation"))

        first_name = d.pop("firstName")

        last_name = d.pop("lastName")

        corporate_account_user_creation = cls(
            email=email,
            salutation=salutation,
            first_name=first_name,
            last_name=last_name,
        )

        corporate_account_user_creation.additional_properties = d
        return corporate_account_user_creation

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
