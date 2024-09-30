import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.offer_product_step_accounting_timespan import OfferProductStepAccountingTimespan
from ..models.offer_product_step_cancellation_timespan import OfferProductStepCancellationTimespan
from ..models.offer_product_step_duration_timespan import OfferProductStepDurationTimespan
from ..models.offer_product_step_issue_based_cancellation_timespan import OfferProductStepIssueBasedCancellationTimespan
from ..models.offer_product_step_regular_based_cancellation_timespan import (
    OfferProductStepRegularBasedCancellationTimespan,
)
from ..models.offer_product_step_term_timespan import OfferProductStepTermTimespan
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.offer_translation import OfferTranslation
    from ..models.product_contract import ProductContract
    from ..models.product_tag import ProductTag


T = TypeVar("T", bound="OfferProductStep")


@_attrs_define
class OfferProductStep:
    """
    Attributes:
        position (int): position inside the product
        price_issue_id (int): id of the price issue associated with this step
        product_contract_id (Union[Unset, int]): id of the product contract associated with this step
        translations (Union[Unset, List['OfferTranslation']]): translations associated with this product
        product_tag_ids (Union[Unset, List[int]]): tags associated with this product
        additional_product_contract_ids (Union[Unset, List[int]]): additioanl product contract ids with this product
        created_date (Union[None, Unset, datetime.datetime]): Time the object was created in RFC 3339 format, e.g.,
            2021-08-30T17:32:28Z
        changed_date (Union[None, Unset, datetime.datetime]): Time the object was changed in RFC 3339 format, e.g.,
            2021-08-30T17:32:28Z
        plenigo_step_id (Union[Unset, str]): unique id of the step within the product
        amount (Union[Unset, int]): amount of issues
        chargeable_amount (Union[Unset, int]): amount of paid issues
        issue_based_cancellation_period (Union[Unset, int]): issue based cancellation period
        issue_based_cancellation_timespan (Union[Unset, OfferProductStepIssueBasedCancellationTimespan]): issue based
            cancellation timespan
        regular_based_cancellation_period (Union[Unset, int]): regular based cancellation period
        regular_based_cancellation_timespan (Union[Unset, OfferProductStepRegularBasedCancellationTimespan]): regular
            based cancellation timespan
        term_period (Union[Unset, int]): term time period
        term_timespan (Union[Unset, OfferProductStepTermTimespan]): term timespan
        duration_period (Union[Unset, int]): duration period of the product step - can be 0 for no end time
        duration_timespan (Union[Unset, OfferProductStepDurationTimespan]): duration timespan
        accounting_period (Union[Unset, int]): accounting period of the product step
        accounting_timespan (Union[Unset, OfferProductStepAccountingTimespan]): accounting timespan
        cancellation_period (Union[Unset, int]): cancellation period of the product step
        cancellation_timespan (Union[Unset, OfferProductStepCancellationTimespan]): cancellation timespan
        ivw_rule_id (Union[Unset, int]): id of the ivw rule associated with this product step
        credit_count (Union[Unset, int]): credit count added with this step
        product_tags (Union[Unset, List['ProductTag']]): tags associated with this product
        additional_product_contracts (Union[Unset, List['ProductContract']]): additioanl product contract ids with this
            product
    """

    position: int
    price_issue_id: int
    product_contract_id: Union[Unset, int] = UNSET
    translations: Union[Unset, List["OfferTranslation"]] = UNSET
    product_tag_ids: Union[Unset, List[int]] = UNSET
    additional_product_contract_ids: Union[Unset, List[int]] = UNSET
    created_date: Union[None, Unset, datetime.datetime] = UNSET
    changed_date: Union[None, Unset, datetime.datetime] = UNSET
    plenigo_step_id: Union[Unset, str] = UNSET
    amount: Union[Unset, int] = UNSET
    chargeable_amount: Union[Unset, int] = UNSET
    issue_based_cancellation_period: Union[Unset, int] = UNSET
    issue_based_cancellation_timespan: Union[Unset, OfferProductStepIssueBasedCancellationTimespan] = UNSET
    regular_based_cancellation_period: Union[Unset, int] = UNSET
    regular_based_cancellation_timespan: Union[Unset, OfferProductStepRegularBasedCancellationTimespan] = UNSET
    term_period: Union[Unset, int] = UNSET
    term_timespan: Union[Unset, OfferProductStepTermTimespan] = UNSET
    duration_period: Union[Unset, int] = UNSET
    duration_timespan: Union[Unset, OfferProductStepDurationTimespan] = UNSET
    accounting_period: Union[Unset, int] = UNSET
    accounting_timespan: Union[Unset, OfferProductStepAccountingTimespan] = UNSET
    cancellation_period: Union[Unset, int] = UNSET
    cancellation_timespan: Union[Unset, OfferProductStepCancellationTimespan] = UNSET
    ivw_rule_id: Union[Unset, int] = UNSET
    credit_count: Union[Unset, int] = UNSET
    product_tags: Union[Unset, List["ProductTag"]] = UNSET
    additional_product_contracts: Union[Unset, List["ProductContract"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        position = self.position

        price_issue_id = self.price_issue_id

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

        plenigo_step_id = self.plenigo_step_id

        amount = self.amount

        chargeable_amount = self.chargeable_amount

        issue_based_cancellation_period = self.issue_based_cancellation_period

        issue_based_cancellation_timespan: Union[Unset, str] = UNSET
        if not isinstance(self.issue_based_cancellation_timespan, Unset):
            issue_based_cancellation_timespan = self.issue_based_cancellation_timespan.value

        regular_based_cancellation_period = self.regular_based_cancellation_period

        regular_based_cancellation_timespan: Union[Unset, str] = UNSET
        if not isinstance(self.regular_based_cancellation_timespan, Unset):
            regular_based_cancellation_timespan = self.regular_based_cancellation_timespan.value

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

        ivw_rule_id = self.ivw_rule_id

        credit_count = self.credit_count

        product_tags: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.product_tags, Unset):
            product_tags = []
            for product_tags_item_data in self.product_tags:
                product_tags_item = product_tags_item_data.to_dict()
                product_tags.append(product_tags_item)

        additional_product_contracts: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.additional_product_contracts, Unset):
            additional_product_contracts = []
            for additional_product_contracts_item_data in self.additional_product_contracts:
                additional_product_contracts_item = additional_product_contracts_item_data.to_dict()
                additional_product_contracts.append(additional_product_contracts_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "position": position,
                "priceIssueId": price_issue_id,
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
        if created_date is not UNSET:
            field_dict["createdDate"] = created_date
        if changed_date is not UNSET:
            field_dict["changedDate"] = changed_date
        if plenigo_step_id is not UNSET:
            field_dict["plenigoStepId"] = plenigo_step_id
        if amount is not UNSET:
            field_dict["amount"] = amount
        if chargeable_amount is not UNSET:
            field_dict["chargeableAmount"] = chargeable_amount
        if issue_based_cancellation_period is not UNSET:
            field_dict["issueBasedCancellationPeriod"] = issue_based_cancellation_period
        if issue_based_cancellation_timespan is not UNSET:
            field_dict["issueBasedCancellationTimespan"] = issue_based_cancellation_timespan
        if regular_based_cancellation_period is not UNSET:
            field_dict["regularBasedCancellationPeriod"] = regular_based_cancellation_period
        if regular_based_cancellation_timespan is not UNSET:
            field_dict["regularBasedCancellationTimespan"] = regular_based_cancellation_timespan
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
        if ivw_rule_id is not UNSET:
            field_dict["ivwRuleId"] = ivw_rule_id
        if credit_count is not UNSET:
            field_dict["creditCount"] = credit_count
        if product_tags is not UNSET:
            field_dict["productTags"] = product_tags
        if additional_product_contracts is not UNSET:
            field_dict["additionalProductContracts"] = additional_product_contracts

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.offer_translation import OfferTranslation
        from ..models.product_contract import ProductContract
        from ..models.product_tag import ProductTag

        d = src_dict.copy()
        position = d.pop("position")

        price_issue_id = d.pop("priceIssueId")

        product_contract_id = d.pop("productContractId", UNSET)

        translations = []
        _translations = d.pop("translations", UNSET)
        for translations_item_data in _translations or []:
            translations_item = OfferTranslation.from_dict(translations_item_data)

            translations.append(translations_item)

        product_tag_ids = cast(List[int], d.pop("productTagIds", UNSET))

        additional_product_contract_ids = cast(List[int], d.pop("additionalProductContractIds", UNSET))

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
                created_date_type_0 = isoparse(data)

                return created_date_type_0
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
                changed_date_type_0 = isoparse(data)

                return changed_date_type_0
            except:  # noqa: E722
                pass

            return cast(Union[None, Unset, datetime.datetime], data)

        changed_date = _parse_changed_date(d.pop("changedDate", UNSET))

        plenigo_step_id = d.pop("plenigoStepId", UNSET)

        amount = d.pop("amount", UNSET)

        chargeable_amount = d.pop("chargeableAmount", UNSET)

        issue_based_cancellation_period = d.pop("issueBasedCancellationPeriod", UNSET)

        _issue_based_cancellation_timespan = d.pop("issueBasedCancellationTimespan", UNSET)
        issue_based_cancellation_timespan: Union[Unset, OfferProductStepIssueBasedCancellationTimespan]
        if isinstance(_issue_based_cancellation_timespan, Unset) or not _issue_based_cancellation_timespan:
            issue_based_cancellation_timespan = UNSET
        else:
            issue_based_cancellation_timespan = OfferProductStepIssueBasedCancellationTimespan(
                _issue_based_cancellation_timespan
            )

        regular_based_cancellation_period = d.pop("regularBasedCancellationPeriod", UNSET)

        _regular_based_cancellation_timespan = d.pop("regularBasedCancellationTimespan", UNSET)
        regular_based_cancellation_timespan: Union[Unset, OfferProductStepRegularBasedCancellationTimespan]
        if isinstance(_regular_based_cancellation_timespan, Unset) or not _regular_based_cancellation_timespan:
            regular_based_cancellation_timespan = UNSET
        else:
            regular_based_cancellation_timespan = OfferProductStepRegularBasedCancellationTimespan(
                _regular_based_cancellation_timespan
            )

        term_period = d.pop("termPeriod", UNSET)

        _term_timespan = d.pop("termTimespan", UNSET)
        term_timespan: Union[Unset, OfferProductStepTermTimespan]
        if isinstance(_term_timespan, Unset) or not _term_timespan:
            term_timespan = UNSET
        else:
            term_timespan = OfferProductStepTermTimespan(_term_timespan)

        duration_period = d.pop("durationPeriod", UNSET)

        _duration_timespan = d.pop("durationTimespan", UNSET)
        duration_timespan: Union[Unset, OfferProductStepDurationTimespan]
        if isinstance(_duration_timespan, Unset) or not _duration_timespan:
            duration_timespan = UNSET
        else:
            duration_timespan = OfferProductStepDurationTimespan(_duration_timespan)

        accounting_period = d.pop("accountingPeriod", UNSET)

        _accounting_timespan = d.pop("accountingTimespan", UNSET)
        accounting_timespan: Union[Unset, OfferProductStepAccountingTimespan]
        if isinstance(_accounting_timespan, Unset) or not _accounting_timespan:
            accounting_timespan = UNSET
        else:
            accounting_timespan = OfferProductStepAccountingTimespan(_accounting_timespan)

        cancellation_period = d.pop("cancellationPeriod", UNSET)

        _cancellation_timespan = d.pop("cancellationTimespan", UNSET)
        cancellation_timespan: Union[Unset, OfferProductStepCancellationTimespan]
        if isinstance(_cancellation_timespan, Unset) or not _cancellation_timespan:
            cancellation_timespan = UNSET
        else:
            cancellation_timespan = OfferProductStepCancellationTimespan(_cancellation_timespan)

        ivw_rule_id = d.pop("ivwRuleId", UNSET)

        credit_count = d.pop("creditCount", UNSET)

        product_tags = []
        _product_tags = d.pop("productTags", UNSET)
        for product_tags_item_data in _product_tags or []:
            product_tags_item = ProductTag.from_dict(product_tags_item_data)

            product_tags.append(product_tags_item)

        additional_product_contracts = []
        _additional_product_contracts = d.pop("additionalProductContracts", UNSET)
        for additional_product_contracts_item_data in _additional_product_contracts or []:
            additional_product_contracts_item = ProductContract.from_dict(additional_product_contracts_item_data)

            additional_product_contracts.append(additional_product_contracts_item)

        offer_product_step = cls(
            position=position,
            price_issue_id=price_issue_id,
            product_contract_id=product_contract_id,
            translations=translations,
            product_tag_ids=product_tag_ids,
            additional_product_contract_ids=additional_product_contract_ids,
            created_date=created_date,
            changed_date=changed_date,
            plenigo_step_id=plenigo_step_id,
            amount=amount,
            chargeable_amount=chargeable_amount,
            issue_based_cancellation_period=issue_based_cancellation_period,
            issue_based_cancellation_timespan=issue_based_cancellation_timespan,
            regular_based_cancellation_period=regular_based_cancellation_period,
            regular_based_cancellation_timespan=regular_based_cancellation_timespan,
            term_period=term_period,
            term_timespan=term_timespan,
            duration_period=duration_period,
            duration_timespan=duration_timespan,
            accounting_period=accounting_period,
            accounting_timespan=accounting_timespan,
            cancellation_period=cancellation_period,
            cancellation_timespan=cancellation_timespan,
            ivw_rule_id=ivw_rule_id,
            credit_count=credit_count,
            product_tags=product_tags,
            additional_product_contracts=additional_product_contracts,
        )

        offer_product_step.additional_properties = d
        return offer_product_step

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
