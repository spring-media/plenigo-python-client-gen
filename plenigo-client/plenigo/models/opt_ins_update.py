from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.opt_ins_update_opt_ins import OptInsUpdateOptIns


T = TypeVar("T", bound="OptInsUpdate")


@attr.s(auto_attribs=True)
class OptInsUpdate:
    """
    Attributes:
        opt_ins (Union[Unset, OptInsUpdateOptIns]):
    """

    opt_ins: Union[Unset, "OptInsUpdateOptIns"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        opt_ins: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.opt_ins, Unset):
            opt_ins = self.opt_ins.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if opt_ins is not UNSET:
            field_dict["optIns"] = opt_ins

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.opt_ins_update_opt_ins import OptInsUpdateOptIns

        d = src_dict.copy()
        _opt_ins = d.pop("optIns", UNSET)
        opt_ins: Union[Unset, OptInsUpdateOptIns]
        if isinstance(_opt_ins, Unset):
            opt_ins = UNSET
        else:
            opt_ins = OptInsUpdateOptIns.from_dict(_opt_ins)

        opt_ins_update = cls(
            opt_ins=opt_ins,
        )

        opt_ins_update.additional_properties = d
        return opt_ins_update

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
