from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.opt_ins_opt_ins import OptInsOptIns


T = TypeVar("T", bound="OptIns")


@attr.s(auto_attribs=True)
class OptIns:
    """
    Attributes:
        customer_id (Union[Unset, str]): id of the customer the login attempt is done for
        opt_ins (Union[Unset, OptInsOptIns]):
    """

    customer_id: Union[Unset, str] = UNSET
    opt_ins: Union[Unset, "OptInsOptIns"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        customer_id = self.customer_id
        opt_ins: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.opt_ins, Unset):
            opt_ins = self.opt_ins.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if customer_id is not UNSET:
            field_dict["customerId"] = customer_id
        if opt_ins is not UNSET:
            field_dict["optIns"] = opt_ins

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.opt_ins_opt_ins import OptInsOptIns

        d = src_dict.copy()
        customer_id = d.pop("customerId", UNSET)

        _opt_ins = d.pop("optIns", UNSET)
        opt_ins: Union[Unset, OptInsOptIns]
        if isinstance(_opt_ins, Unset):
            opt_ins = UNSET
        else:
            opt_ins = OptInsOptIns.from_dict(_opt_ins)

        opt_ins = cls(
            customer_id=customer_id,
            opt_ins=opt_ins,
        )

        opt_ins.additional_properties = d
        return opt_ins

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
