from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SubscriptionConnectedOfferInfo")


@_attrs_define
class SubscriptionConnectedOfferInfo:
    """
    Attributes:
        contract_company_id (str): id of the contract company the subscription is connected to
        company_id (str): id of the company the subscription is connected to
        plenigo_offer_id (str): the connected plenigo offer id the subscription is connected to
        customer_id (Union[Unset, str]): id of the customer the subscription is connected to
    """

    contract_company_id: str
    company_id: str
    plenigo_offer_id: str
    customer_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        contract_company_id = self.contract_company_id

        company_id = self.company_id

        plenigo_offer_id = self.plenigo_offer_id

        customer_id = self.customer_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "contractCompanyId": contract_company_id,
                "companyId": company_id,
                "plenigoOfferId": plenigo_offer_id,
            }
        )
        if customer_id is not UNSET:
            field_dict["customerId"] = customer_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        contract_company_id = d.pop("contractCompanyId")

        company_id = d.pop("companyId")

        plenigo_offer_id = d.pop("plenigoOfferId")

        customer_id = d.pop("customerId", UNSET)

        subscription_connected_offer_info = cls(
            contract_company_id=contract_company_id,
            company_id=company_id,
            plenigo_offer_id=plenigo_offer_id,
            customer_id=customer_id,
        )

        subscription_connected_offer_info.additional_properties = d
        return subscription_connected_offer_info

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
