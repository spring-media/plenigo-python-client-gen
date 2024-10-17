from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.offer_translation import OfferTranslation


T = TypeVar("T", bound="OfferProductStepCreation")


@_attrs_define
class OfferProductStepCreation:
    """
    Attributes:
        position (int): position inside the product
        product_contract_id (Union[Unset, int]): id of the product contract associated with this step
        translations (Union[Unset, List['OfferTranslation']]): translations associated with this product
        product_tag_ids (Union[Unset, List[int]]): tags associated with this product
        additional_product_contract_ids (Union[Unset, List[int]]): additioanl product contract ids with this product
    """

    position: int
    product_contract_id: Union[Unset, int] = UNSET
    translations: Union[Unset, List["OfferTranslation"]] = UNSET
    product_tag_ids: Union[Unset, List[int]] = UNSET
    additional_product_contract_ids: Union[Unset, List[int]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        position = self.position

        product_contract_id = self.product_contract_id

        translations: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.translations, Unset):
            translations = []
            for translations_item_data in self.translations:
                translations_item = translations_item_data.to_dict()
                translations.append(translations_item)

        product_tag_ids: Union[Unset, List[int]] = UNSET
        if not isinstance(self.product_tag_ids, Unset):
            product_tag_ids = self.product_tag_ids

        additional_product_contract_ids: Union[Unset, List[int]] = UNSET
        if not isinstance(self.additional_product_contract_ids, Unset):
            additional_product_contract_ids = self.additional_product_contract_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "position": position,
            }
        )
        if product_contract_id is not UNSET:
            field_dict["productContractId"] = product_contract_id
        if translations is not UNSET:
            field_dict["translations"] = translations
        if product_tag_ids is not UNSET:
            field_dict["productTagIds"] = product_tag_ids
        if additional_product_contract_ids is not UNSET:
            field_dict["additionalProductContractIds"] = additional_product_contract_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.offer_translation import OfferTranslation

        d = src_dict.copy()
        position = d.pop("position")

        product_contract_id = d.pop("productContractId", UNSET)

        translations = []
        _translations = d.pop("translations", UNSET)
        for translations_item_data in _translations or []:
            translations_item = OfferTranslation.from_dict(translations_item_data)

            translations.append(translations_item)

        product_tag_ids = cast(List[int], d.pop("productTagIds", UNSET))

        additional_product_contract_ids = cast(List[int], d.pop("additionalProductContractIds", UNSET))

        offer_product_step_creation = cls(
            position=position,
            product_contract_id=product_contract_id,
            translations=translations,
            product_tag_ids=product_tag_ids,
            additional_product_contract_ids=additional_product_contract_ids,
        )

        offer_product_step_creation.additional_properties = d
        return offer_product_step_creation

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
