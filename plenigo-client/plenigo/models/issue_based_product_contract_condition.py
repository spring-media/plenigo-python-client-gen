from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.issue_based_product_contract_condition_cancellation_period_timespan import (
    IssueBasedProductContractConditionCancellationPeriodTimespan,
)
from ..models.issue_based_product_contract_condition_cancellation_type import (
    IssueBasedProductContractConditionCancellationType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="IssueBasedProductContractCondition")


@_attrs_define
class IssueBasedProductContractCondition:
    """
    Attributes:
        deliveries (int): amount of issues included in payment period
        chargeable_deliveries (int): amount of paid issues included in payment period
        cancellation_type (IssueBasedProductContractConditionCancellationType): cancellation type
        cancellation_period (int): issue based cancellation period of the contract
        cancellation_period_timespan (IssueBasedProductContractConditionCancellationPeriodTimespan): issue based
            cancellation timespan of the contract
        auto_renewal_delivery (Union[Unset, bool]): flag indicating if last step of an offer should be auto renewal
    """

    deliveries: int
    chargeable_deliveries: int
    cancellation_type: IssueBasedProductContractConditionCancellationType
    cancellation_period: int
    cancellation_period_timespan: IssueBasedProductContractConditionCancellationPeriodTimespan
    auto_renewal_delivery: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        deliveries = self.deliveries

        chargeable_deliveries = self.chargeable_deliveries

        cancellation_type = self.cancellation_type.value

        cancellation_period = self.cancellation_period

        cancellation_period_timespan = self.cancellation_period_timespan.value

        auto_renewal_delivery = self.auto_renewal_delivery

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "deliveries": deliveries,
                "chargeableDeliveries": chargeable_deliveries,
                "cancellationType": cancellation_type,
                "cancellationPeriod": cancellation_period,
                "cancellationPeriodTimespan": cancellation_period_timespan,
            }
        )
        if auto_renewal_delivery is not UNSET:
            field_dict["autoRenewalDelivery"] = auto_renewal_delivery

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        deliveries = d.pop("deliveries")

        chargeable_deliveries = d.pop("chargeableDeliveries")

        cancellation_type = IssueBasedProductContractConditionCancellationType(d.pop("cancellationType"))

        cancellation_period = d.pop("cancellationPeriod")

        cancellation_period_timespan = IssueBasedProductContractConditionCancellationPeriodTimespan(
            d.pop("cancellationPeriodTimespan")
        )

        auto_renewal_delivery = d.pop("autoRenewalDelivery", UNSET)

        issue_based_product_contract_condition = cls(
            deliveries=deliveries,
            chargeable_deliveries=chargeable_deliveries,
            cancellation_type=cancellation_type,
            cancellation_period=cancellation_period,
            cancellation_period_timespan=cancellation_period_timespan,
            auto_renewal_delivery=auto_renewal_delivery,
        )

        issue_based_product_contract_condition.additional_properties = d
        return issue_based_product_contract_condition

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
