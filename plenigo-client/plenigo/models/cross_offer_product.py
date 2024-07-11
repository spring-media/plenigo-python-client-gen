import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.cross_offer_product_product_type import CrossOfferProductProductType
from ..models.cross_offer_product_tax_type import CrossOfferProductTaxType
from ..models.cross_offer_product_voucher_validity_timespan import CrossOfferProductVoucherValidityTimespan
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cost_center import CostCenter
    from ..models.cross_offer_product_additional_data import CrossOfferProductAdditionalData
    from ..models.cross_offer_product_data import CrossOfferProductData
    from ..models.cross_offer_product_step import CrossOfferProductStep
    from ..models.offer_translation import OfferTranslation
    from ..models.price_issue import PriceIssue


T = TypeVar("T", bound="CrossOfferProduct")


@_attrs_define
class CrossOfferProduct:
    """
    Attributes:
        position (int): order position within the offer - must start with one and be in order
        tax_type (CrossOfferProductTaxType): tax type product is associated with
        product_type (CrossOfferProductProductType): defines the type of product
        amount (int): amount of goods represented by this product
        translations (List['OfferTranslation']): translations associated with this product
        plenigo_product_id (str): unique id of the product within the offer
        created_date (Union[None, Unset, datetime.datetime]): Time the object was created in RFC 3339 format, e.g.,
            2021-08-30T17:32:28Z
        changed_date (Union[None, Unset, datetime.datetime]): Time the object was changed in RFC 3339 format, e.g.,
            2021-08-30T17:32:28Z
        internal_title (Union[Unset, str]): internal title of the product
        subscription (Union[Unset, bool]): flag indicating if product represents a subscription
        validity_time (Union[Unset, int]): validity time of this product in days
        validity_end_time (Union[None, Unset, datetime.datetime]): date the this product validity will be end
        cost_center (Union[Unset, CostCenter]):
        voucher_target_plenigo_offer_id (Union[Unset, str]): plenigo offer id of the target offer - required with
            product type VOUCHER_SALE
        voucher_validity_time (Union[Unset, int]): validity time of the voucher based on timespan
        voucher_validity_timespan (Union[Unset, CrossOfferProductVoucherValidityTimespan]): date the this product
            validity will be end
        additional_data (Union[Unset, CrossOfferProductAdditionalData]):
        data (Union[Unset, CrossOfferProductData]): additional data field
        price_issue (Union[Unset, PriceIssue]):
        option (Union[Unset, bool]): flag indicating if product is an option in a basket
        steps (Union[Unset, List['CrossOfferProductStep']]): steps associated with this product - mandatory field for
            subscriptions
    """

    position: int
    tax_type: CrossOfferProductTaxType
    product_type: CrossOfferProductProductType
    amount: int
    translations: List["OfferTranslation"]
    plenigo_product_id: str
    created_date: Union[None, Unset, datetime.datetime] = UNSET
    changed_date: Union[None, Unset, datetime.datetime] = UNSET
    internal_title: Union[Unset, str] = UNSET
    subscription: Union[Unset, bool] = UNSET
    validity_time: Union[Unset, int] = UNSET
    validity_end_time: Union[None, Unset, datetime.datetime] = UNSET
    cost_center: Union[Unset, "CostCenter"] = UNSET
    voucher_target_plenigo_offer_id: Union[Unset, str] = UNSET
    voucher_validity_time: Union[Unset, int] = UNSET
    voucher_validity_timespan: Union[Unset, CrossOfferProductVoucherValidityTimespan] = UNSET
    additional_data: Union[Unset, "CrossOfferProductAdditionalData"] = UNSET
    data: Union[Unset, "CrossOfferProductData"] = UNSET
    price_issue: Union[Unset, "PriceIssue"] = UNSET
    option: Union[Unset, bool] = UNSET
    steps: Union[Unset, List["CrossOfferProductStep"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        position = self.position

        tax_type = self.tax_type.value

        product_type = self.product_type.value

        amount = self.amount

        translations = []
        for translations_item_data in self.translations:
            translations_item = translations_item_data.to_dict()
            translations.append(translations_item)

        plenigo_product_id = self.plenigo_product_id

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

        internal_title = self.internal_title

        subscription = self.subscription

        validity_time = self.validity_time

        validity_end_time: Union[None, Unset, str]
        if isinstance(self.validity_end_time, Unset):
            validity_end_time = UNSET
        elif isinstance(self.validity_end_time, datetime.datetime):
            validity_end_time = self.validity_end_time.isoformat()
        else:
            validity_end_time = self.validity_end_time

        cost_center: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.cost_center, Unset):
            cost_center = self.cost_center.to_dict()

        voucher_target_plenigo_offer_id = self.voucher_target_plenigo_offer_id

        voucher_validity_time = self.voucher_validity_time

        voucher_validity_timespan: Union[Unset, str] = UNSET
        if not isinstance(self.voucher_validity_timespan, Unset):
            voucher_validity_timespan = self.voucher_validity_timespan.value

        additional_data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.additional_data, Unset):
            additional_data = self.additional_data.to_dict()

        data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        price_issue: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.price_issue, Unset):
            price_issue = self.price_issue.to_dict()

        option = self.option

        steps: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.steps, Unset):
            steps = []
            for steps_item_data in self.steps:
                steps_item = steps_item_data.to_dict()
                steps.append(steps_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "position": position,
                "taxType": tax_type,
                "productType": product_type,
                "amount": amount,
                "translations": translations,
                "plenigoProductId": plenigo_product_id,
            }
        )
        if created_date is not UNSET:
            field_dict["createdDate"] = created_date
        if changed_date is not UNSET:
            field_dict["changedDate"] = changed_date
        if internal_title is not UNSET:
            field_dict["internalTitle"] = internal_title
        if subscription is not UNSET:
            field_dict["subscription"] = subscription
        if validity_time is not UNSET:
            field_dict["validityTime"] = validity_time
        if validity_end_time is not UNSET:
            field_dict["validityEndTime"] = validity_end_time
        if cost_center is not UNSET:
            field_dict["costCenter"] = cost_center
        if voucher_target_plenigo_offer_id is not UNSET:
            field_dict["voucherTargetPlenigoOfferId"] = voucher_target_plenigo_offer_id
        if voucher_validity_time is not UNSET:
            field_dict["voucherValidityTime"] = voucher_validity_time
        if voucher_validity_timespan is not UNSET:
            field_dict["voucherValidityTimespan"] = voucher_validity_timespan
        if additional_data is not UNSET:
            field_dict["additionalData"] = additional_data
        if data is not UNSET:
            field_dict["data"] = data
        if price_issue is not UNSET:
            field_dict["priceIssue"] = price_issue
        if option is not UNSET:
            field_dict["option"] = option
        if steps is not UNSET:
            field_dict["steps"] = steps

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.cost_center import CostCenter
        from ..models.cross_offer_product_additional_data import CrossOfferProductAdditionalData
        from ..models.cross_offer_product_data import CrossOfferProductData
        from ..models.cross_offer_product_step import CrossOfferProductStep
        from ..models.offer_translation import OfferTranslation
        from ..models.price_issue import PriceIssue

        d = src_dict.copy()
        position = d.pop("position")

        tax_type = CrossOfferProductTaxType(d.pop("taxType"))

        product_type = CrossOfferProductProductType(d.pop("productType"))

        amount = d.pop("amount")

        translations = []
        _translations = d.pop("translations")
        for translations_item_data in _translations:
            translations_item = OfferTranslation.from_dict(translations_item_data)

            translations.append(translations_item)

        plenigo_product_id = d.pop("plenigoProductId")

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

        internal_title = d.pop("internalTitle", UNSET)

        subscription = d.pop("subscription", UNSET)

        validity_time = d.pop("validityTime", UNSET)

        def _parse_validity_end_time(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                validity_end_time_type_0 = isoparse(data)

                return validity_end_time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        validity_end_time = _parse_validity_end_time(d.pop("validityEndTime", UNSET))

        _cost_center = d.pop("costCenter", UNSET)
        cost_center: Union[Unset, CostCenter]
        if isinstance(_cost_center, Unset):
            cost_center = UNSET
        else:
            cost_center = CostCenter.from_dict(_cost_center)

        voucher_target_plenigo_offer_id = d.pop("voucherTargetPlenigoOfferId", UNSET)

        voucher_validity_time = d.pop("voucherValidityTime", UNSET)

        _voucher_validity_timespan = d.pop("voucherValidityTimespan", UNSET)
        voucher_validity_timespan: Union[Unset, CrossOfferProductVoucherValidityTimespan]
        if isinstance(_voucher_validity_timespan, Unset):
            voucher_validity_timespan = UNSET
        else:
            voucher_validity_timespan = CrossOfferProductVoucherValidityTimespan(_voucher_validity_timespan)

        _additional_data = d.pop("additionalData", UNSET)
        additional_data: Union[Unset, CrossOfferProductAdditionalData]
        if isinstance(_additional_data, Unset):
            additional_data = UNSET
        else:
            additional_data = CrossOfferProductAdditionalData.from_dict(_additional_data)

        _data = d.pop("data", UNSET)
        data: Union[Unset, CrossOfferProductData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = CrossOfferProductData.from_dict(_data)

        _price_issue = d.pop("priceIssue", UNSET)
        price_issue: Union[Unset, PriceIssue]
        if isinstance(_price_issue, Unset):
            price_issue = UNSET
        else:
            price_issue = PriceIssue.from_dict(_price_issue)

        option = d.pop("option", UNSET)

        steps = []
        _steps = d.pop("steps", UNSET)
        for steps_item_data in _steps or []:
            steps_item = CrossOfferProductStep.from_dict(steps_item_data)

            steps.append(steps_item)

        cross_offer_product = cls(
            position=position,
            tax_type=tax_type,
            product_type=product_type,
            amount=amount,
            translations=translations,
            plenigo_product_id=plenigo_product_id,
            created_date=created_date,
            changed_date=changed_date,
            internal_title=internal_title,
            subscription=subscription,
            validity_time=validity_time,
            validity_end_time=validity_end_time,
            cost_center=cost_center,
            voucher_target_plenigo_offer_id=voucher_target_plenigo_offer_id,
            voucher_validity_time=voucher_validity_time,
            voucher_validity_timespan=voucher_validity_timespan,
            additional_data=additional_data,
            data=data,
            price_issue=price_issue,
            option=option,
            steps=steps,
        )

        cross_offer_product.additional_properties = d
        return cross_offer_product

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
