from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.corporate_account_user_code_status_status import CorporateAccountUserCodeStatusStatus

T = TypeVar("T", bound="CorporateAccountUserCodeStatus")


@_attrs_define
class CorporateAccountUserCodeStatus:
    """
    Attributes:
        corporate_account_id (int): unique id of the corporate account in the context of a company
        plenigo_offer_id (str): plenigo offer id of the corporate account
        status (CorporateAccountUserCodeStatusStatus): statuss of the corporate account user

            | Status    | Description
            |
            | --------- | --------------------------------------------------------------------------------------------------
            ----------------------------------|
            | ACTIVE    | customer is active and has access to the corporate account product
            |
            | INACTIVE  | customer is inactive and has no access to the corporate account product
            |
            | INVITED   | customer is invited to activate the corporate account user
            |
    """

    corporate_account_id: int
    plenigo_offer_id: str
    status: CorporateAccountUserCodeStatusStatus
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        corporate_account_id = self.corporate_account_id

        plenigo_offer_id = self.plenigo_offer_id

        status = self.status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "corporateAccountId": corporate_account_id,
                "plenigoOfferId": plenigo_offer_id,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        corporate_account_id = d.pop("corporateAccountId")

        plenigo_offer_id = d.pop("plenigoOfferId")

        status = CorporateAccountUserCodeStatusStatus(d.pop("status"))

        corporate_account_user_code_status = cls(
            corporate_account_id=corporate_account_id,
            plenigo_offer_id=plenigo_offer_id,
            status=status,
        )

        corporate_account_user_code_status.additional_properties = d
        return corporate_account_user_code_status

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
