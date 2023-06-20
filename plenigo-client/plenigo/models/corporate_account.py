from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.access_right_item_data import AccessRightItemData
    from ..models.corporate_account_user_creation import CorporateAccountUserCreation


T = TypeVar("T", bound="CorporateAccount")


@attr.s(auto_attribs=True)
class CorporateAccount:
    """
    Attributes:
        corporate_account_id (int): unique id of the corporate account in the context of a company
        customer_id (str): unique id of the customer the corporate account belongs to
        title (str): title of the corporate account
        plenigo_offer_id (str): plenigo offer id of the corporate account
        users_amount (Union[Unset, int]): max amount of users allowed in this corporate account
        users (Union[Unset, List['CorporateAccountUserCreation']]):
        access_right_items (Union[Unset, List['AccessRightItemData']]):
    """

    corporate_account_id: int
    customer_id: str
    title: str
    plenigo_offer_id: str
    users_amount: Union[Unset, int] = UNSET
    users: Union[Unset, List["CorporateAccountUserCreation"]] = UNSET
    access_right_items: Union[Unset, List["AccessRightItemData"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        corporate_account_id = self.corporate_account_id
        customer_id = self.customer_id
        title = self.title
        plenigo_offer_id = self.plenigo_offer_id
        users_amount = self.users_amount
        users: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.users, Unset):
            users = []
            for users_item_data in self.users:
                users_item = users_item_data.to_dict()

                users.append(users_item)

        access_right_items: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.access_right_items, Unset):
            access_right_items = []
            for access_right_items_item_data in self.access_right_items:
                access_right_items_item = access_right_items_item_data.to_dict()

                access_right_items.append(access_right_items_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "corporateAccountId": corporate_account_id,
                "customerId": customer_id,
                "title": title,
                "plenigoOfferId": plenigo_offer_id,
            }
        )
        if users_amount is not UNSET:
            field_dict["usersAmount"] = users_amount
        if users is not UNSET:
            field_dict["users"] = users
        if access_right_items is not UNSET:
            field_dict["accessRightItems"] = access_right_items

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.access_right_item_data import AccessRightItemData
        from ..models.corporate_account_user_creation import CorporateAccountUserCreation

        d = src_dict.copy()
        corporate_account_id = d.pop("corporateAccountId")

        customer_id = d.pop("customerId")

        title = d.pop("title")

        plenigo_offer_id = d.pop("plenigoOfferId")

        users_amount = d.pop("usersAmount", UNSET)

        users = []
        _users = d.pop("users", UNSET)
        for users_item_data in _users or []:
            users_item = CorporateAccountUserCreation.from_dict(users_item_data)

            users.append(users_item)

        access_right_items = []
        _access_right_items = d.pop("accessRightItems", UNSET)
        for access_right_items_item_data in _access_right_items or []:
            access_right_items_item = AccessRightItemData.from_dict(access_right_items_item_data)

            access_right_items.append(access_right_items_item)

        corporate_account = cls(
            corporate_account_id=corporate_account_id,
            customer_id=customer_id,
            title=title,
            plenigo_offer_id=plenigo_offer_id,
            users_amount=users_amount,
            users=users,
            access_right_items=access_right_items,
        )

        corporate_account.additional_properties = d
        return corporate_account

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
