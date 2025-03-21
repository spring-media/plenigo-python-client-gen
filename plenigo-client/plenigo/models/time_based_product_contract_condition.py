from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.time_based_product_contract_condition_accounting_timespan import (
    TimeBasedProductContractConditionAccountingTimespan,
)
from ..models.time_based_product_contract_condition_cancellation_timespan import (
    TimeBasedProductContractConditionCancellationTimespan,
)
from ..models.time_based_product_contract_condition_duration_timespan import (
    TimeBasedProductContractConditionDurationTimespan,
)
from ..models.time_based_product_contract_condition_term_timespan import TimeBasedProductContractConditionTermTimespan
from ..models.time_based_product_contract_condition_time_based_contract_type import (
    TimeBasedProductContractConditionTimeBasedContractType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.multiuser_conditions import MultiuserConditions


T = TypeVar("T", bound="TimeBasedProductContractCondition")


@_attrs_define
class TimeBasedProductContractCondition:
    """
    Attributes:
        term_period (Union[Unset, int]): term time period
        term_timespan (Union[Unset, TimeBasedProductContractConditionTermTimespan]): term timespan
        duration_period (Union[Unset, int]): duration period of the product step - can be 0 for no end time
        duration_timespan (Union[Unset, TimeBasedProductContractConditionDurationTimespan]): duration timespan
        accounting_period (Union[Unset, int]): accounting period of the product step
        accounting_timespan (Union[Unset, TimeBasedProductContractConditionAccountingTimespan]): accounting timespan
        cancellation_period (Union[Unset, int]): cancellation period of the product step
        cancellation_timespan (Union[Unset, TimeBasedProductContractConditionCancellationTimespan]): cancellation
            timespan
        time_based_contract_type (Union[Unset, TimeBasedProductContractConditionTimeBasedContractType]): time based
            contract type
        multiuser_conditions (Union[Unset, MultiuserConditions]):
    """

    term_period: Union[Unset, int] = UNSET
    term_timespan: Union[Unset, TimeBasedProductContractConditionTermTimespan] = UNSET
    duration_period: Union[Unset, int] = UNSET
    duration_timespan: Union[Unset, TimeBasedProductContractConditionDurationTimespan] = UNSET
    accounting_period: Union[Unset, int] = UNSET
    accounting_timespan: Union[Unset, TimeBasedProductContractConditionAccountingTimespan] = UNSET
    cancellation_period: Union[Unset, int] = UNSET
    cancellation_timespan: Union[Unset, TimeBasedProductContractConditionCancellationTimespan] = UNSET
    time_based_contract_type: Union[Unset, TimeBasedProductContractConditionTimeBasedContractType] = UNSET
    multiuser_conditions: Union[Unset, "MultiuserConditions"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        term_period = self.term_period

        term_timespan: Union[Unset, str] = UNSET
        if not isinstance(self.term_timespan, Unset):
            term_timespan = self.term_timespan.value

        duration_period = self.duration_period

        duration_timespan: Union[Unset, str] = UNSET
        if not isinstance(self.duration_timespan, Unset):
            duration_timespan = self.duration_timespan.value

        accounting_period = self.accounting_period

        accounting_timespan: Union[Unset, str] = UNSET
        if not isinstance(self.accounting_timespan, Unset):
            accounting_timespan = self.accounting_timespan.value

        cancellation_period = self.cancellation_period

        cancellation_timespan: Union[Unset, str] = UNSET
        if not isinstance(self.cancellation_timespan, Unset):
            cancellation_timespan = self.cancellation_timespan.value

        time_based_contract_type: Union[Unset, str] = UNSET
        if not isinstance(self.time_based_contract_type, Unset):
            time_based_contract_type = self.time_based_contract_type.value

        multiuser_conditions: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.multiuser_conditions, Unset):
            multiuser_conditions = self.multiuser_conditions.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if term_period is not UNSET:
            field_dict["termPeriod"] = term_period
        if term_timespan is not UNSET:
            field_dict["termTimespan"] = term_timespan
        if duration_period is not UNSET:
            field_dict["durationPeriod"] = duration_period
        if duration_timespan is not UNSET:
            field_dict["durationTimespan"] = duration_timespan
        if accounting_period is not UNSET:
            field_dict["accountingPeriod"] = accounting_period
        if accounting_timespan is not UNSET:
            field_dict["accountingTimespan"] = accounting_timespan
        if cancellation_period is not UNSET:
            field_dict["cancellationPeriod"] = cancellation_period
        if cancellation_timespan is not UNSET:
            field_dict["cancellationTimespan"] = cancellation_timespan
        if time_based_contract_type is not UNSET:
            field_dict["timeBasedContractType"] = time_based_contract_type
        if multiuser_conditions is not UNSET:
            field_dict["multiuserConditions"] = multiuser_conditions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.multiuser_conditions import MultiuserConditions

        d = src_dict.copy()
        term_period = d.pop("termPeriod", UNSET)

        _term_timespan = d.pop("termTimespan", UNSET)
        term_timespan: Union[Unset, TimeBasedProductContractConditionTermTimespan]
        if isinstance(_term_timespan, Unset) or not _term_timespan:
            term_timespan = UNSET
        else:
            term_timespan = TimeBasedProductContractConditionTermTimespan(_term_timespan)

        duration_period = d.pop("durationPeriod", UNSET)

        _duration_timespan = d.pop("durationTimespan", UNSET)
        duration_timespan: Union[Unset, TimeBasedProductContractConditionDurationTimespan]
        if isinstance(_duration_timespan, Unset) or not _duration_timespan:
            duration_timespan = UNSET
        else:
            duration_timespan = TimeBasedProductContractConditionDurationTimespan(_duration_timespan)

        accounting_period = d.pop("accountingPeriod", UNSET)

        _accounting_timespan = d.pop("accountingTimespan", UNSET)
        accounting_timespan: Union[Unset, TimeBasedProductContractConditionAccountingTimespan]
        if isinstance(_accounting_timespan, Unset) or not _accounting_timespan:
            accounting_timespan = UNSET
        else:
            accounting_timespan = TimeBasedProductContractConditionAccountingTimespan(_accounting_timespan)

        cancellation_period = d.pop("cancellationPeriod", UNSET)

        _cancellation_timespan = d.pop("cancellationTimespan", UNSET)
        cancellation_timespan: Union[Unset, TimeBasedProductContractConditionCancellationTimespan]
        if isinstance(_cancellation_timespan, Unset) or not _cancellation_timespan:
            cancellation_timespan = UNSET
        else:
            cancellation_timespan = TimeBasedProductContractConditionCancellationTimespan(_cancellation_timespan)

        _time_based_contract_type = d.pop("timeBasedContractType", UNSET)
        time_based_contract_type: Union[Unset, TimeBasedProductContractConditionTimeBasedContractType]
        if isinstance(_time_based_contract_type, Unset) or not _time_based_contract_type:
            time_based_contract_type = UNSET
        else:
            time_based_contract_type = TimeBasedProductContractConditionTimeBasedContractType(_time_based_contract_type)

        _multiuser_conditions = d.pop("multiuserConditions", UNSET)
        multiuser_conditions: Union[Unset, MultiuserConditions]
        if isinstance(_multiuser_conditions, Unset) or not _multiuser_conditions:
            multiuser_conditions = UNSET
        else:
            multiuser_conditions = MultiuserConditions.from_dict(_multiuser_conditions)

        time_based_product_contract_condition = cls(
            term_period=term_period,
            term_timespan=term_timespan,
            duration_period=duration_period,
            duration_timespan=duration_timespan,
            accounting_period=accounting_period,
            accounting_timespan=accounting_timespan,
            cancellation_period=cancellation_period,
            cancellation_timespan=cancellation_timespan,
            time_based_contract_type=time_based_contract_type,
            multiuser_conditions=multiuser_conditions,
        )

        time_based_product_contract_condition.additional_properties = d
        return time_based_product_contract_condition

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
