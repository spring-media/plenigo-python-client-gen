from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.offer_product_step_base_cancellation_timespan import OfferProductStepBaseCancellationTimespan
from ..models.offer_product_step_base_term_timespan import OfferProductStepBaseTermTimespan
from ..types import UNSET, Unset

T = TypeVar("T", bound="OfferProductStepBase")


@attr.s(auto_attribs=True)
class OfferProductStepBase:
    """
    Attributes:
        position (int): position inside the product
        term_period (int): term time period
        term_timespan (OfferProductStepBaseTermTimespan): term time span
        duration_period (int): duration period of the product step - can be 0 for no end time
        accounting_period (int): accounting period of the product step
        cancellation_period (int): cancellation period of the product step
        cancellation_timespan (OfferProductStepBaseCancellationTimespan): cancellation timespan
        ivw_rule_id (Union[Unset, int]): id of the ivw rule associated with this product step
        credit_count (Union[Unset, int]): credit count added with this step
    """

    position: int
    term_period: int
    term_timespan: OfferProductStepBaseTermTimespan
    duration_period: int
    accounting_period: int
    cancellation_period: int
    cancellation_timespan: OfferProductStepBaseCancellationTimespan
    ivw_rule_id: Union[Unset, int] = UNSET
    credit_count: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        position = self.position
        term_period = self.term_period
        term_timespan = self.term_timespan.value

        duration_period = self.duration_period
        accounting_period = self.accounting_period
        cancellation_period = self.cancellation_period
        cancellation_timespan = self.cancellation_timespan.value

        ivw_rule_id = self.ivw_rule_id
        credit_count = self.credit_count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "position": position,
                "termPeriod": term_period,
                "termTimespan": term_timespan,
                "durationPeriod": duration_period,
                "accountingPeriod": accounting_period,
                "cancellationPeriod": cancellation_period,
                "cancellationTimespan": cancellation_timespan,
            }
        )
        if ivw_rule_id is not UNSET:
            field_dict["ivwRuleId"] = ivw_rule_id
        if credit_count is not UNSET:
            field_dict["creditCount"] = credit_count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        position = d.pop("position")

        term_period = d.pop("termPeriod")

        term_timespan = OfferProductStepBaseTermTimespan(d.pop("termTimespan"))

        duration_period = d.pop("durationPeriod")

        accounting_period = d.pop("accountingPeriod")

        cancellation_period = d.pop("cancellationPeriod")

        cancellation_timespan = OfferProductStepBaseCancellationTimespan(d.pop("cancellationTimespan"))

        ivw_rule_id = d.pop("ivwRuleId", UNSET)

        credit_count = d.pop("creditCount", UNSET)

        offer_product_step_base = cls(
            position=position,
            term_period=term_period,
            term_timespan=term_timespan,
            duration_period=duration_period,
            accounting_period=accounting_period,
            cancellation_period=cancellation_period,
            cancellation_timespan=cancellation_timespan,
            ivw_rule_id=ivw_rule_id,
            credit_count=credit_count,
        )

        offer_product_step_base.additional_properties = d
        return offer_product_step_base

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
