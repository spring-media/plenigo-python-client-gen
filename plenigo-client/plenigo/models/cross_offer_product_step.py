import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.cross_offer_product_step_accounting_timespan import CrossOfferProductStepAccountingTimespan
from ..models.cross_offer_product_step_cancellation_timespan import CrossOfferProductStepCancellationTimespan
from ..models.cross_offer_product_step_duration_timespan import CrossOfferProductStepDurationTimespan
from ..models.cross_offer_product_step_term_timespan import CrossOfferProductStepTermTimespan
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.offer_translation import OfferTranslation
    from ..models.price_issue import PriceIssue
    from ..models.product_contract import ProductContract


T = TypeVar("T", bound="CrossOfferProductStep")


@_attrs_define
class CrossOfferProductStep:
    """
    Attributes:
        position (int): position inside the product
        created_date (Union[None, Unset, datetime.datetime]): Time the object was created in RFC 3339 format, e.g.,
            2021-08-30T17:32:28Z
        changed_date (Union[None, Unset, datetime.datetime]): Time the object was changed in RFC 3339 format, e.g.,
            2021-08-30T17:32:28Z
        translations (Union[Unset, List['OfferTranslation']]): translations associated with this product
        product_tag_ids (Union[Unset, List[int]]): tags associated with this product
        additional_product_contract_ids (Union[Unset, List[int]]): additioanl product contract ids with this product
        plenigo_step_id (Union[Unset, str]): unique id of the step within the product
        term_period (Union[Unset, int]): term time period
        term_timespan (Union[Unset, CrossOfferProductStepTermTimespan]): term timespan
        duration_period (Union[Unset, int]): duration period of the product step - can be 0 for no end time
        duration_timespan (Union[Unset, CrossOfferProductStepDurationTimespan]): duration timespan
        accounting_period (Union[Unset, int]): accounting period of the product step
        accounting_timespan (Union[Unset, CrossOfferProductStepAccountingTimespan]): accounting timespan
        cancellation_period (Union[Unset, int]): cancellation period of the product step
        cancellation_timespan (Union[Unset, CrossOfferProductStepCancellationTimespan]): cancellation timespan
        product_contract (Union[Unset, ProductContract]):
        price_issue (Union[Unset, PriceIssue]):
        additional_product_contracts (Union[Unset, List['ProductContract']]): additioanl product contract ids with this
            product
    """

    position: int
    created_date: Union[None, Unset, datetime.datetime] = UNSET
    changed_date: Union[None, Unset, datetime.datetime] = UNSET
    translations: Union[Unset, List["OfferTranslation"]] = UNSET
    product_tag_ids: Union[Unset, List[int]] = UNSET
    additional_product_contract_ids: Union[Unset, List[int]] = UNSET
    plenigo_step_id: Union[Unset, str] = UNSET
    term_period: Union[Unset, int] = UNSET
    term_timespan: Union[Unset, CrossOfferProductStepTermTimespan] = UNSET
    duration_period: Union[Unset, int] = UNSET
    duration_timespan: Union[Unset, CrossOfferProductStepDurationTimespan] = UNSET
    accounting_period: Union[Unset, int] = UNSET
    accounting_timespan: Union[Unset, CrossOfferProductStepAccountingTimespan] = UNSET
    cancellation_period: Union[Unset, int] = UNSET
    cancellation_timespan: Union[Unset, CrossOfferProductStepCancellationTimespan] = UNSET
    product_contract: Union[Unset, "ProductContract"] = UNSET
    price_issue: Union[Unset, "PriceIssue"] = UNSET
    additional_product_contracts: Union[Unset, List["ProductContract"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        position = self.position

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

        plenigo_step_id = self.plenigo_step_id

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

        product_contract: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.product_contract, Unset):
            product_contract = self.product_contract.to_dict()

        price_issue: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.price_issue, Unset):
            price_issue = self.price_issue.to_dict()

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
            }
        )
        if created_date is not UNSET:
            field_dict["createdDate"] = created_date
        if changed_date is not UNSET:
            field_dict["changedDate"] = changed_date
        if translations is not UNSET:
            field_dict["translations"] = translations
        if product_tag_ids is not UNSET:
            field_dict["productTagIds"] = product_tag_ids
        if additional_product_contract_ids is not UNSET:
            field_dict["additionalProductContractIds"] = additional_product_contract_ids
        if plenigo_step_id is not UNSET:
            field_dict["plenigoStepId"] = plenigo_step_id
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
        if product_contract is not UNSET:
            field_dict["productContract"] = product_contract
        if price_issue is not UNSET:
            field_dict["priceIssue"] = price_issue
        if additional_product_contracts is not UNSET:
            field_dict["additionalProductContracts"] = additional_product_contracts

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.offer_translation import OfferTranslation
        from ..models.price_issue import PriceIssue
        from ..models.product_contract import ProductContract

        d = src_dict.copy()
        position = d.pop("position")

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

        translations = []
        _translations = d.pop("translations", UNSET)
        for translations_item_data in _translations or []:
            translations_item = OfferTranslation.from_dict(translations_item_data)

            translations.append(translations_item)

        product_tag_ids = cast(List[int], d.pop("productTagIds", UNSET))

        additional_product_contract_ids = cast(List[int], d.pop("additionalProductContractIds", UNSET))

        plenigo_step_id = d.pop("plenigoStepId", UNSET)

        term_period = d.pop("termPeriod", UNSET)

        _term_timespan = d.pop("termTimespan", UNSET)
        term_timespan: Union[Unset, CrossOfferProductStepTermTimespan]
        if isinstance(_term_timespan, Unset):
            term_timespan = UNSET
        else:
            term_timespan = CrossOfferProductStepTermTimespan(_term_timespan)

        duration_period = d.pop("durationPeriod", UNSET)

        _duration_timespan = d.pop("durationTimespan", UNSET)
        duration_timespan: Union[Unset, CrossOfferProductStepDurationTimespan]
        if isinstance(_duration_timespan, Unset):
            duration_timespan = UNSET
        else:
            duration_timespan = CrossOfferProductStepDurationTimespan(_duration_timespan)

        accounting_period = d.pop("accountingPeriod", UNSET)

        _accounting_timespan = d.pop("accountingTimespan", UNSET)
        accounting_timespan: Union[Unset, CrossOfferProductStepAccountingTimespan]
        if isinstance(_accounting_timespan, Unset):
            accounting_timespan = UNSET
        else:
            accounting_timespan = CrossOfferProductStepAccountingTimespan(_accounting_timespan)

        cancellation_period = d.pop("cancellationPeriod", UNSET)

        _cancellation_timespan = d.pop("cancellationTimespan", UNSET)
        cancellation_timespan: Union[Unset, CrossOfferProductStepCancellationTimespan]
        if isinstance(_cancellation_timespan, Unset):
            cancellation_timespan = UNSET
        else:
            cancellation_timespan = CrossOfferProductStepCancellationTimespan(_cancellation_timespan)

        _product_contract = d.pop("productContract", UNSET)
        product_contract: Union[Unset, ProductContract]
        if isinstance(_product_contract, Unset):
            product_contract = UNSET
        else:
            product_contract = ProductContract.from_dict(_product_contract)

        _price_issue = d.pop("priceIssue", UNSET)
        price_issue: Union[Unset, PriceIssue]
        if isinstance(_price_issue, Unset):
            price_issue = UNSET
        else:
            price_issue = PriceIssue.from_dict(_price_issue)

        additional_product_contracts = []
        _additional_product_contracts = d.pop("additionalProductContracts", UNSET)
        for additional_product_contracts_item_data in _additional_product_contracts or []:
            additional_product_contracts_item = ProductContract.from_dict(additional_product_contracts_item_data)

            additional_product_contracts.append(additional_product_contracts_item)

        cross_offer_product_step = cls(
            position=position,
            created_date=created_date,
            changed_date=changed_date,
            translations=translations,
            product_tag_ids=product_tag_ids,
            additional_product_contract_ids=additional_product_contract_ids,
            plenigo_step_id=plenigo_step_id,
            term_period=term_period,
            term_timespan=term_timespan,
            duration_period=duration_period,
            duration_timespan=duration_timespan,
            accounting_period=accounting_period,
            accounting_timespan=accounting_timespan,
            cancellation_period=cancellation_period,
            cancellation_timespan=cancellation_timespan,
            product_contract=product_contract,
            price_issue=price_issue,
            additional_product_contracts=additional_product_contracts,
        )

        cross_offer_product_step.additional_properties = d
        return cross_offer_product_step

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
