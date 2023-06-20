from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.bonus_availability import BonusAvailability
from ..models.bonus_delivery_condition import BonusDeliveryCondition
from ..models.bonus_receiver import BonusReceiver
from ..models.bonus_tax_type import BonusTaxType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.addon_translation import AddonTranslation


T = TypeVar("T", bound="Bonus")


@attr.s(auto_attribs=True)
class Bonus:
    """
    Attributes:
        availability (BonusAvailability): availability of the bonus Example: AVAILABLE.
        delivery_condition (BonusDeliveryCondition): delivery condition for the bonus Example: AFTER_PAYMENT.
        internal_title (str): internal title of the bonus Example: Teacup.
        access_right_id (Union[Unset, int]): optional access right associated with the bonus Example: 223001.
        archived (Union[Unset, bool]): flag indicating if bonus is archived Example: True.
        tax_type (Union[Unset, BonusTaxType]):
        bonus_id (Union[Unset, int]): unique id of the image within the contract company Example: 123400.
        cost_center_id (Union[Unset, int]): optional cost center associated with the bonus Example: 123001.
        delivery_address_mandatory (Union[Unset, bool]): flag indicating if delivery address is required Example: True.
        delivery_amount (Union[Unset, int]): delivery amount Example: 1.
        description (Union[Unset, str]): description of the bonus Example: The cheapest teacup we have in stock..
        invoice_address_mandatory (Union[Unset, bool]): flag indicating if invoice address is required Example: True.
        plenigo_bonus_id (Union[Unset, str]): plenigo bonus id to identify the bonus during checkout Example:
            BO_12345678901234567.
        price_issue_id (Union[Unset, int]): optional price issue associated with the bonus Example: 323001.
        receiver (Union[Unset, BonusReceiver]): receiver of the bonus Example: PAYER.
        translations (Union[Unset, None, List['AddonTranslation']]): translations of the bonus
    """

    availability: BonusAvailability
    delivery_condition: BonusDeliveryCondition
    internal_title: str
    access_right_id: Union[Unset, int] = UNSET
    archived: Union[Unset, bool] = UNSET
    tax_type: Union[Unset, BonusTaxType] = UNSET
    bonus_id: Union[Unset, int] = UNSET
    cost_center_id: Union[Unset, int] = UNSET
    delivery_address_mandatory: Union[Unset, bool] = UNSET
    delivery_amount: Union[Unset, int] = UNSET
    description: Union[Unset, str] = UNSET
    invoice_address_mandatory: Union[Unset, bool] = UNSET
    plenigo_bonus_id: Union[Unset, str] = UNSET
    price_issue_id: Union[Unset, int] = UNSET
    receiver: Union[Unset, BonusReceiver] = UNSET
    translations: Union[Unset, None, List["AddonTranslation"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        availability = self.availability.value

        delivery_condition = self.delivery_condition.value

        internal_title = self.internal_title
        access_right_id = self.access_right_id
        archived = self.archived
        tax_type: Union[Unset, str] = UNSET
        if not isinstance(self.tax_type, Unset):
            tax_type = self.tax_type.value

        bonus_id = self.bonus_id
        cost_center_id = self.cost_center_id
        delivery_address_mandatory = self.delivery_address_mandatory
        delivery_amount = self.delivery_amount
        description = self.description
        invoice_address_mandatory = self.invoice_address_mandatory
        plenigo_bonus_id = self.plenigo_bonus_id
        price_issue_id = self.price_issue_id
        receiver: Union[Unset, str] = UNSET
        if not isinstance(self.receiver, Unset):
            receiver = self.receiver.value

        translations: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.translations, Unset):
            if self.translations is None:
                translations = None
            else:
                translations = []
                for translations_item_data in self.translations:
                    translations_item = translations_item_data.to_dict()

                    translations.append(translations_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "availability": availability,
                "deliveryCondition": delivery_condition,
                "internalTitle": internal_title,
            }
        )
        if access_right_id is not UNSET:
            field_dict["accessRightId"] = access_right_id
        if archived is not UNSET:
            field_dict["archived"] = archived
        if tax_type is not UNSET:
            field_dict["taxType"] = tax_type
        if bonus_id is not UNSET:
            field_dict["bonusId"] = bonus_id
        if cost_center_id is not UNSET:
            field_dict["costCenterId"] = cost_center_id
        if delivery_address_mandatory is not UNSET:
            field_dict["deliveryAddressMandatory"] = delivery_address_mandatory
        if delivery_amount is not UNSET:
            field_dict["deliveryAmount"] = delivery_amount
        if description is not UNSET:
            field_dict["description"] = description
        if invoice_address_mandatory is not UNSET:
            field_dict["invoiceAddressMandatory"] = invoice_address_mandatory
        if plenigo_bonus_id is not UNSET:
            field_dict["plenigoBonusId"] = plenigo_bonus_id
        if price_issue_id is not UNSET:
            field_dict["priceIssueId"] = price_issue_id
        if receiver is not UNSET:
            field_dict["receiver"] = receiver
        if translations is not UNSET:
            field_dict["translations"] = translations

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.addon_translation import AddonTranslation

        d = src_dict.copy()
        availability = BonusAvailability(d.pop("availability"))

        delivery_condition = BonusDeliveryCondition(d.pop("deliveryCondition"))

        internal_title = d.pop("internalTitle")

        access_right_id = d.pop("accessRightId", UNSET)

        archived = d.pop("archived", UNSET)

        _tax_type = d.pop("taxType", UNSET)
        tax_type: Union[Unset, BonusTaxType]
        if isinstance(_tax_type, Unset):
            tax_type = UNSET
        else:
            tax_type = BonusTaxType(_tax_type)

        bonus_id = d.pop("bonusId", UNSET)

        cost_center_id = d.pop("costCenterId", UNSET)

        delivery_address_mandatory = d.pop("deliveryAddressMandatory", UNSET)

        delivery_amount = d.pop("deliveryAmount", UNSET)

        description = d.pop("description", UNSET)

        invoice_address_mandatory = d.pop("invoiceAddressMandatory", UNSET)

        plenigo_bonus_id = d.pop("plenigoBonusId", UNSET)

        price_issue_id = d.pop("priceIssueId", UNSET)

        _receiver = d.pop("receiver", UNSET)
        receiver: Union[Unset, BonusReceiver]
        if isinstance(_receiver, Unset):
            receiver = UNSET
        else:
            receiver = BonusReceiver(_receiver)

        translations = []
        _translations = d.pop("translations", UNSET)
        for translations_item_data in _translations or []:
            translations_item = AddonTranslation.from_dict(translations_item_data)

            translations.append(translations_item)

        bonus = cls(
            availability=availability,
            delivery_condition=delivery_condition,
            internal_title=internal_title,
            access_right_id=access_right_id,
            archived=archived,
            tax_type=tax_type,
            bonus_id=bonus_id,
            cost_center_id=cost_center_id,
            delivery_address_mandatory=delivery_address_mandatory,
            delivery_amount=delivery_amount,
            description=description,
            invoice_address_mandatory=invoice_address_mandatory,
            plenigo_bonus_id=plenigo_bonus_id,
            price_issue_id=price_issue_id,
            receiver=receiver,
            translations=translations,
        )

        bonus.additional_properties = d
        return bonus

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
