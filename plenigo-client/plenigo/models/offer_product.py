import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.offer_product_base_product_type import OfferProductBaseProductType
from ..models.offer_product_base_tax_type import OfferProductBaseTaxType
from ..models.offer_product_base_voucher_validity_timespan import OfferProductBaseVoucherValidityTimespan
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_base_date import ApiBaseDate
    from ..models.offer_product_base_additional_data import OfferProductBaseAdditionalData
    from ..models.offer_product_base_data import OfferProductBaseData
    from ..models.offer_product_step import OfferProductStep
    from ..models.product_tag import ProductTag


T = TypeVar("T", bound="OfferProduct")


@_attrs_define
class OfferProduct:
    """
    Attributes:
        position (int): order position within the offer - must start with one and be in order
        tax_type (OfferProductBaseTaxType): tax type product is associated with
        product_type (OfferProductBaseProductType): defines the type of product
        amount (int): amount of goods represented by this product
        access_right_id (int): id of the access right associated with this product
        plenigo_product_id (str): unique id of the product within the offer
        internal_title (Union[Unset, str]): internal title of the product
        subscription (Union[Unset, bool]): flag indicating if product represents a subscription
        delivery_list_id (Union[Unset, int]): id of the delivery list to use
        validity_time (Union[Unset, int]): validity time of this product in days
        validity_end_time (Union[None, Unset, datetime.datetime]): date the this product validity will be end
        cost_center_id (Union[Unset, int]): id of the cost center associated with this product
        ledger_id (Union[Unset, int]): id of the ledger associated with this product
        ivw_rule_id (Union[Unset, int]): id of the ivw rule associated with this product
        voucher_target_plenigo_offer_id (Union[Unset, str]): plenigo offer id of the target offer - required with
            product type VOUCHER_SALE
        voucher_template_id (Union[Unset, int]): id of the voucher template to use - required with product type
            VOUCHER_SALE
        voucher_validity_time (Union[Unset, int]): validity time of the voucher based on timespan
        voucher_validity_timespan (Union[Unset, OfferProductBaseVoucherValidityTimespan]): date the this product
            validity will be end
        additional_data (Union[Unset, OfferProductBaseAdditionalData]):
        data (Union[Unset, OfferProductBaseData]): additional data field
        price_issue_id (Union[Unset, int]): id of the price issue associated with this product
        shipping_cost_price_issue_id (Union[Unset, int]): id of the shipping cost price issue associated with this
            product
        credit_count_walled_id (Union[Unset, int]): id of the credit card wallet associated with this credit count
            wallet
        credit_count (Union[Unset, int]): credit count added with this product
        option (Union[Unset, bool]): flag indicating if product is an option in a basket
        translations (Union[Unset, List['ApiBaseDate']]): translations associated with this product
        created_date (Union[None, Unset, datetime.datetime]): time the object was created with time notation as defined
            by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for
            example, 17:32:28
        changed_date (Union[None, Unset, datetime.datetime]): time the object was changed with time notation as defined
            by <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">RFC 3339, section 5.6</a>, for
            example, 17:32:28
        steps (Union[Unset, List['OfferProductStep']]): steps associated with this product - mandatory field for
            subscriptions
        product_tags (Union[Unset, List['ProductTag']]): tags associated with this product
    """

    position: int
    tax_type: OfferProductBaseTaxType
    product_type: OfferProductBaseProductType
    amount: int
    access_right_id: int
    plenigo_product_id: str
    internal_title: Union[Unset, str] = UNSET
    subscription: Union[Unset, bool] = UNSET
    delivery_list_id: Union[Unset, int] = UNSET
    validity_time: Union[Unset, int] = UNSET
    validity_end_time: Union[None, Unset, datetime.datetime] = UNSET
    cost_center_id: Union[Unset, int] = UNSET
    ledger_id: Union[Unset, int] = UNSET
    ivw_rule_id: Union[Unset, int] = UNSET
    voucher_target_plenigo_offer_id: Union[Unset, str] = UNSET
    voucher_template_id: Union[Unset, int] = UNSET
    voucher_validity_time: Union[Unset, int] = UNSET
    voucher_validity_timespan: Union[Unset, OfferProductBaseVoucherValidityTimespan] = UNSET
    additional_data: Union[Unset, "OfferProductBaseAdditionalData"] = UNSET
    data: Union[Unset, "OfferProductBaseData"] = UNSET
    price_issue_id: Union[Unset, int] = UNSET
    shipping_cost_price_issue_id: Union[Unset, int] = UNSET
    credit_count_walled_id: Union[Unset, int] = UNSET
    credit_count: Union[Unset, int] = UNSET
    option: Union[Unset, bool] = UNSET
    translations: Union[Unset, List["ApiBaseDate"]] = UNSET
    created_date: Union[None, Unset, datetime.datetime] = UNSET
    changed_date: Union[None, Unset, datetime.datetime] = UNSET
    steps: Union[Unset, List["OfferProductStep"]] = UNSET
    product_tags: Union[Unset, List["ProductTag"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        position = self.position

        tax_type = self.tax_type.value

        product_type = self.product_type.value

        amount = self.amount

        access_right_id = self.access_right_id

        plenigo_product_id = self.plenigo_product_id

        internal_title = self.internal_title

        subscription = self.subscription

        delivery_list_id = self.delivery_list_id

        validity_time = self.validity_time

        validity_end_time: Union[None, Unset, str]
        if isinstance(self.validity_end_time, Unset) or self.validity_end_time is None:
            validity_end_time = UNSET
        elif isinstance(self.validity_end_time, datetime.datetime):
            validity_end_time = self.validity_end_time.isoformat()
        else:
            validity_end_time = self.validity_end_time

        cost_center_id = self.cost_center_id

        ledger_id = self.ledger_id

        ivw_rule_id = self.ivw_rule_id

        voucher_target_plenigo_offer_id = self.voucher_target_plenigo_offer_id

        voucher_template_id = self.voucher_template_id

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

        price_issue_id = self.price_issue_id

        shipping_cost_price_issue_id = self.shipping_cost_price_issue_id

        credit_count_walled_id = self.credit_count_walled_id

        credit_count = self.credit_count

        option = self.option

        translations: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.translations, Unset):
            translations = []
            for translations_item_data in self.translations:
                translations_item = translations_item_data.to_dict()
                translations.append(translations_item)

        created_date: Union[None, Unset, str]
        if isinstance(self.created_date, Unset) or self.created_date is None:
            created_date = UNSET
        elif isinstance(self.created_date, datetime.datetime):
            created_date = self.created_date.isoformat()
        else:
            created_date = self.created_date

        changed_date: Union[None, Unset, str]
        if isinstance(self.changed_date, Unset) or self.changed_date is None:
            changed_date = UNSET
        elif isinstance(self.changed_date, datetime.datetime):
            changed_date = self.changed_date.isoformat()
        else:
            changed_date = self.changed_date

        steps: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.steps, Unset):
            steps = []
            for steps_item_data in self.steps:
                steps_item = steps_item_data.to_dict()
                steps.append(steps_item)

        product_tags: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.product_tags, Unset):
            product_tags = []
            for product_tags_item_data in self.product_tags:
                product_tags_item = product_tags_item_data.to_dict()
                product_tags.append(product_tags_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "position": position,
                "taxType": tax_type,
                "productType": product_type,
                "amount": amount,
                "accessRightId": access_right_id,
                "plenigoProductId": plenigo_product_id,
            }
        )
        if internal_title is not UNSET:
            field_dict["internalTitle"] = internal_title
        if subscription is not UNSET:
            field_dict["subscription"] = subscription
        if delivery_list_id is not UNSET:
            field_dict["deliveryListId"] = delivery_list_id
        if validity_time is not UNSET:
            field_dict["validityTime"] = validity_time
        if validity_end_time is not UNSET:
            field_dict["validityEndTime"] = validity_end_time
        if cost_center_id is not UNSET:
            field_dict["costCenterId"] = cost_center_id
        if ledger_id is not UNSET:
            field_dict["ledgerId"] = ledger_id
        if ivw_rule_id is not UNSET:
            field_dict["ivwRuleId"] = ivw_rule_id
        if voucher_target_plenigo_offer_id is not UNSET:
            field_dict["voucherTargetPlenigoOfferId"] = voucher_target_plenigo_offer_id
        if voucher_template_id is not UNSET:
            field_dict["voucherTemplateId"] = voucher_template_id
        if voucher_validity_time is not UNSET:
            field_dict["voucherValidityTime"] = voucher_validity_time
        if voucher_validity_timespan is not UNSET:
            field_dict["voucherValidityTimespan"] = voucher_validity_timespan
        if additional_data is not UNSET:
            field_dict["additionalData"] = additional_data
        if data is not UNSET:
            field_dict["data"] = data
        if price_issue_id is not UNSET:
            field_dict["priceIssueId"] = price_issue_id
        if shipping_cost_price_issue_id is not UNSET:
            field_dict["shippingCostPriceIssueId"] = shipping_cost_price_issue_id
        if credit_count_walled_id is not UNSET:
            field_dict["creditCountWalledId"] = credit_count_walled_id
        if credit_count is not UNSET:
            field_dict["creditCount"] = credit_count
        if option is not UNSET:
            field_dict["option"] = option
        if translations is not UNSET:
            field_dict["translations"] = translations
        if created_date is not UNSET:
            field_dict["createdDate"] = created_date
        if changed_date is not UNSET:
            field_dict["changedDate"] = changed_date
        if steps is not UNSET:
            field_dict["steps"] = steps
        if product_tags is not UNSET:
            field_dict["productTags"] = product_tags

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_base_date import ApiBaseDate
        from ..models.offer_product_base_additional_data import OfferProductBaseAdditionalData
        from ..models.offer_product_base_data import OfferProductBaseData
        from ..models.offer_product_step import OfferProductStep
        from ..models.product_tag import ProductTag

        d = src_dict.copy()
        position = d.pop("position")

        tax_type = OfferProductBaseTaxType(d.pop("taxType"))

        product_type = OfferProductBaseProductType(d.pop("productType"))

        amount = d.pop("amount")

        access_right_id = d.pop("accessRightId")

        plenigo_product_id = d.pop("plenigoProductId")

        internal_title = d.pop("internalTitle", UNSET)

        subscription = d.pop("subscription", UNSET)

        delivery_list_id = d.pop("deliveryListId", UNSET)

        validity_time = d.pop("validityTime", UNSET)

        def _parse_validity_end_time(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data

            if data is None:
                return data

            if isinstance(data, Unset):
                return data

            # Try to parse the data as datetime.datetime
            try:
                if not isinstance(data, str):
                    raise TypeError()
                validity_end_time_type_1 = isoparse(data)

                return validity_end_time_type_1
            except:  # noqa: E722
                pass

            return cast(Union[None, Unset, datetime.datetime], data)

        validity_end_time = _parse_validity_end_time(d.pop("validityEndTime", UNSET))

        cost_center_id = d.pop("costCenterId", UNSET)

        ledger_id = d.pop("ledgerId", UNSET)

        ivw_rule_id = d.pop("ivwRuleId", UNSET)

        voucher_target_plenigo_offer_id = d.pop("voucherTargetPlenigoOfferId", UNSET)

        voucher_template_id = d.pop("voucherTemplateId", UNSET)

        voucher_validity_time = d.pop("voucherValidityTime", UNSET)

        _voucher_validity_timespan = d.pop("voucherValidityTimespan", UNSET)
        voucher_validity_timespan: Union[Unset, OfferProductBaseVoucherValidityTimespan]
        if isinstance(_voucher_validity_timespan, Unset) or not _voucher_validity_timespan:
            voucher_validity_timespan = UNSET
        else:
            voucher_validity_timespan = OfferProductBaseVoucherValidityTimespan(_voucher_validity_timespan)

        _additional_data = d.pop("additionalData", UNSET)
        additional_data: Union[Unset, OfferProductBaseAdditionalData]
        if isinstance(_additional_data, Unset) or not _additional_data:
            additional_data = UNSET
        else:
            additional_data = OfferProductBaseAdditionalData.from_dict(_additional_data)

        _data = d.pop("data", UNSET)
        data: Union[Unset, OfferProductBaseData]
        if isinstance(_data, Unset) or not _data:
            data = UNSET
        else:
            data = OfferProductBaseData.from_dict(_data)

        price_issue_id = d.pop("priceIssueId", UNSET)

        shipping_cost_price_issue_id = d.pop("shippingCostPriceIssueId", UNSET)

        credit_count_walled_id = d.pop("creditCountWalledId", UNSET)

        credit_count = d.pop("creditCount", UNSET)

        option = d.pop("option", UNSET)

        translations = []
        _translations = d.pop("translations", UNSET)
        for translations_item_data in _translations or []:
            translations_item = ApiBaseDate.from_dict(translations_item_data)

            translations.append(translations_item)

        def _parse_created_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data

            if data is None:
                return data

            if isinstance(data, Unset):
                return data

            # Try to parse the data as datetime.datetime
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_date_type_1 = isoparse(data)

                return created_date_type_1
            except:  # noqa: E722
                pass

            return cast(Union[None, Unset, datetime.datetime], data)

        created_date = _parse_created_date(d.pop("createdDate", UNSET))

        def _parse_changed_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data

            if data is None:
                return data

            if isinstance(data, Unset):
                return data

            # Try to parse the data as datetime.datetime
            try:
                if not isinstance(data, str):
                    raise TypeError()
                changed_date_type_1 = isoparse(data)

                return changed_date_type_1
            except:  # noqa: E722
                pass

            return cast(Union[None, Unset, datetime.datetime], data)

        changed_date = _parse_changed_date(d.pop("changedDate", UNSET))

        steps = []
        _steps = d.pop("steps", UNSET)
        for steps_item_data in _steps or []:
            steps_item = OfferProductStep.from_dict(steps_item_data)

            steps.append(steps_item)

        product_tags = []
        _product_tags = d.pop("productTags", UNSET)
        for product_tags_item_data in _product_tags or []:
            product_tags_item = ProductTag.from_dict(product_tags_item_data)

            product_tags.append(product_tags_item)

        offer_product = cls(
            position=position,
            tax_type=tax_type,
            product_type=product_type,
            amount=amount,
            access_right_id=access_right_id,
            plenigo_product_id=plenigo_product_id,
            internal_title=internal_title,
            subscription=subscription,
            delivery_list_id=delivery_list_id,
            validity_time=validity_time,
            validity_end_time=validity_end_time,
            cost_center_id=cost_center_id,
            ledger_id=ledger_id,
            ivw_rule_id=ivw_rule_id,
            voucher_target_plenigo_offer_id=voucher_target_plenigo_offer_id,
            voucher_template_id=voucher_template_id,
            voucher_validity_time=voucher_validity_time,
            voucher_validity_timespan=voucher_validity_timespan,
            additional_data=additional_data,
            data=data,
            price_issue_id=price_issue_id,
            shipping_cost_price_issue_id=shipping_cost_price_issue_id,
            credit_count_walled_id=credit_count_walled_id,
            credit_count=credit_count,
            option=option,
            translations=translations,
            created_date=created_date,
            changed_date=changed_date,
            steps=steps,
            product_tags=product_tags,
        )

        offer_product.additional_properties = d
        return offer_product

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
