import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.api_base_changed_by_type import ApiBaseChangedByType
from ..models.api_base_created_by_type import ApiBaseCreatedByType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.access_right_item_data import AccessRightItemData
    from ..models.corporate_account_user import CorporateAccountUser


T = TypeVar("T", bound="CorporateAccount")


@_attrs_define
class CorporateAccount:
    """
    Attributes:
        corporate_account_id (int): unique id of the corporate account in the context of a company
        customer_id (str): unique id of the customer the corporate account belongs to
        title (str): title of the corporate account
        plenigo_offer_id (str): plenigo offer id of the corporate account
        created_date (Union[None, Unset, datetime.datetime]): Time the object was created in RFC 3339 format, e.g.,
            2021-08-30T17:32:28Z
        changed_date (Union[None, Unset, datetime.datetime]): Time the object was changed in RFC 3339 format, e.g.,
            2021-08-30T17:32:28Z
        created_by (Union[Unset, str]): ID of who created the object
        created_by_type (Union[Unset, ApiBaseCreatedByType]): Type of creator
        changed_by (Union[Unset, str]): ID of who changed the object
        changed_by_type (Union[Unset, ApiBaseChangedByType]): Type of changer
        users_amount (Union[Unset, int]): max amount of users allowed in this corporate account
        users (Union[Unset, List['CorporateAccountUser']]):
        access_right_items (Union[Unset, List['AccessRightItemData']]):
    """

    corporate_account_id: int
    customer_id: str
    title: str
    plenigo_offer_id: str
    created_date: Union[None, Unset, datetime.datetime] = UNSET
    changed_date: Union[None, Unset, datetime.datetime] = UNSET
    created_by: Union[Unset, str] = UNSET
    created_by_type: Union[Unset, ApiBaseCreatedByType] = UNSET
    changed_by: Union[Unset, str] = UNSET
    changed_by_type: Union[Unset, ApiBaseChangedByType] = UNSET
    users_amount: Union[Unset, int] = UNSET
    users: Union[Unset, List["CorporateAccountUser"]] = UNSET
    access_right_items: Union[Unset, List["AccessRightItemData"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        corporate_account_id = self.corporate_account_id

        customer_id = self.customer_id

        title = self.title

        plenigo_offer_id = self.plenigo_offer_id

        created_date: Union[None, Unset, str]
        if isinstance(self.created_date, Unset):
            created_date = UNSET
        elif isinstance(self.created_date, datetime.datetime):
            created_date = self.created_date.isoformat()
        else:
            created_date = self.created_date

        changed_date: Union[None, Unset, str]
        if isinstance(self.changed_date, Unset):
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
        from ..models.corporate_account_user import CorporateAccountUser

        d = src_dict.copy()
        corporate_account_id = d.pop("corporateAccountId")

        customer_id = d.pop("customerId")

        title = d.pop("title")

        plenigo_offer_id = d.pop("plenigoOfferId")

        def _parse_created_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
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
            if isinstance(data, Unset):
                return data
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
        created_by_type: Union[Unset, ApiBaseCreatedByType]
        if isinstance(_created_by_type, Unset) or not _created_by_type:
            created_by_type = UNSET
        else:
            created_by_type = ApiBaseCreatedByType(_created_by_type)

        changed_by = d.pop("changedBy", UNSET)

        _changed_by_type = d.pop("changedByType", UNSET)
        changed_by_type: Union[Unset, ApiBaseChangedByType]
        if isinstance(_changed_by_type, Unset) or not _changed_by_type:
            changed_by_type = UNSET
        else:
            changed_by_type = ApiBaseChangedByType(_changed_by_type)

        users_amount = d.pop("usersAmount", UNSET)

        users = []
        _users = d.pop("users", UNSET)
        for users_item_data in _users or []:
            users_item = CorporateAccountUser.from_dict(users_item_data)

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
            created_date=created_date,
            changed_date=changed_date,
            created_by=created_by,
            created_by_type=created_by_type,
            changed_by=changed_by,
            changed_by_type=changed_by_type,
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
