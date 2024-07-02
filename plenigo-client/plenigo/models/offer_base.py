import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.offer_base_allowed_payment_methods_item import OfferBaseAllowedPaymentMethodsItem
from ..models.offer_base_managed_by import OfferBaseManagedBy
from ..models.offer_base_pdf_template_usage import OfferBasePdfTemplateUsage
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_base_date import ApiBaseDate
    from ..models.offer_connected_company_settings import OfferConnectedCompanySettings
    from ..models.offer_partner_settings import OfferPartnerSettings


T = TypeVar("T", bound="OfferBase")


@_attrs_define
class OfferBase:
    """
    Attributes:
        internal_title (str): internal title of the product group
        translations (List['ApiBaseDate']): translations associated with this product
        pause_able (Union[Unset, bool]): flag indicating if subscription is pause able
        invoice_address_mandatory (Union[Unset, bool]): flag indicating if invoice address must be provided by the
            customer
        delivery_address_mandatory (Union[Unset, bool]): flag indicating if delivery address must be provided by the
            customer
        multiple_purchases (Union[Unset, bool]): flag indicating if offer can be bought multiple times from the same
            customer
        misuse_rule_id (Union[Unset, int]): id of the misuse rule to apply
        fixed_start_date (Union[None, Unset, datetime.date]): fixed date the offer starts with
        issues_in_past (Union[Unset, int]): amount of issues that the user can select in the past - cannot be selected
            with fixed start date
        issues_in_future (Union[Unset, int]): amount of issues that the user can select in the future - cannot be
            selected with fixed start date
        archived (Union[Unset, bool]): flag indicating if offer is archived
        allowed_payment_methods (Union[Unset, List[OfferBaseAllowedPaymentMethodsItem]]): additional constraints to the
            payment methods if some of the selected payment methods cannot be used for this offer - there can be no more
            payment methods than selected in the global payment settings section
        connected_company_settings (Union[Unset, OfferConnectedCompanySettings]):
        leaf_id (Union[Unset, int]): id of the tree leaf this offer should be associated with
        external_billing (Union[Unset, bool]): indicates if payments are handled by plenigo or an external system
        customer_cancellation_blocked (Union[Unset, bool]): indicates if a subscription cannot be cancelled by a
            customer
        corporate_account_users (Union[Unset, int]): count of allowed corporate account users
        corporate_account_invitation_url (Union[Unset, str]): corporate account invitation url
        bonus_id (Union[Unset, int]): id of the bonus associated with this offer
        self_service_hint_tm_id (Union[Unset, int]): id of the text module used as self service hint
        managed_by (Union[Unset, OfferBaseManagedBy]): managed by of the given offer.
        pdf_template_usage (Union[Unset, OfferBasePdfTemplateUsage]): contains the pdf template to use with this offer
        partner_settings (Union[Unset, OfferPartnerSettings]):
    """

    internal_title: str
    translations: List["ApiBaseDate"]
    pause_able: Union[Unset, bool] = UNSET
    invoice_address_mandatory: Union[Unset, bool] = UNSET
    delivery_address_mandatory: Union[Unset, bool] = UNSET
    multiple_purchases: Union[Unset, bool] = UNSET
    misuse_rule_id: Union[Unset, int] = UNSET
    fixed_start_date: Union[None, Unset, datetime.date] = UNSET
    issues_in_past: Union[Unset, int] = UNSET
    issues_in_future: Union[Unset, int] = UNSET
    archived: Union[Unset, bool] = UNSET
    allowed_payment_methods: Union[Unset, List[OfferBaseAllowedPaymentMethodsItem]] = UNSET
    connected_company_settings: Union[Unset, "OfferConnectedCompanySettings"] = UNSET
    leaf_id: Union[Unset, int] = UNSET
    external_billing: Union[Unset, bool] = UNSET
    customer_cancellation_blocked: Union[Unset, bool] = UNSET
    corporate_account_users: Union[Unset, int] = UNSET
    corporate_account_invitation_url: Union[Unset, str] = UNSET
    bonus_id: Union[Unset, int] = UNSET
    self_service_hint_tm_id: Union[Unset, int] = UNSET
    managed_by: Union[Unset, OfferBaseManagedBy] = UNSET
    pdf_template_usage: Union[Unset, OfferBasePdfTemplateUsage] = UNSET
    partner_settings: Union[Unset, "OfferPartnerSettings"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        internal_title = self.internal_title

        translations = []
        for translations_item_data in self.translations:
            translations_item = translations_item_data.to_dict()
            translations.append(translations_item)

        pause_able = self.pause_able

        invoice_address_mandatory = self.invoice_address_mandatory

        delivery_address_mandatory = self.delivery_address_mandatory

        multiple_purchases = self.multiple_purchases

        misuse_rule_id = self.misuse_rule_id

        fixed_start_date: Union[None, Unset, str]
        if isinstance(self.fixed_start_date, Unset):
            fixed_start_date = UNSET
        elif isinstance(self.fixed_start_date, datetime.date):
            fixed_start_date = self.fixed_start_date.isoformat()
        else:
            fixed_start_date = self.fixed_start_date

        issues_in_past = self.issues_in_past

        issues_in_future = self.issues_in_future

        archived = self.archived

        allowed_payment_methods: Union[Unset, List[str]] = UNSET
        if not isinstance(self.allowed_payment_methods, Unset):
            allowed_payment_methods = []
            for allowed_payment_methods_item_data in self.allowed_payment_methods:
                allowed_payment_methods_item = allowed_payment_methods_item_data.value
                allowed_payment_methods.append(allowed_payment_methods_item)

        connected_company_settings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.connected_company_settings, Unset):
            connected_company_settings = self.connected_company_settings.to_dict()

        leaf_id = self.leaf_id

        external_billing = self.external_billing

        customer_cancellation_blocked = self.customer_cancellation_blocked

        corporate_account_users = self.corporate_account_users

        corporate_account_invitation_url = self.corporate_account_invitation_url

        bonus_id = self.bonus_id

        self_service_hint_tm_id = self.self_service_hint_tm_id

        managed_by: Union[Unset, str] = UNSET
        if not isinstance(self.managed_by, Unset):
            managed_by = self.managed_by.value

        pdf_template_usage: Union[Unset, str] = UNSET
        if not isinstance(self.pdf_template_usage, Unset):
            pdf_template_usage = self.pdf_template_usage.value

        partner_settings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.partner_settings, Unset):
            partner_settings = self.partner_settings.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "internalTitle": internal_title,
                "translations": translations,
            }
        )
        if pause_able is not UNSET:
            field_dict["pauseAble"] = pause_able
        if invoice_address_mandatory is not UNSET:
            field_dict["invoiceAddressMandatory"] = invoice_address_mandatory
        if delivery_address_mandatory is not UNSET:
            field_dict["deliveryAddressMandatory"] = delivery_address_mandatory
        if multiple_purchases is not UNSET:
            field_dict["multiplePurchases"] = multiple_purchases
        if misuse_rule_id is not UNSET:
            field_dict["misuseRuleId"] = misuse_rule_id
        if fixed_start_date is not UNSET:
            field_dict["fixedStartDate"] = fixed_start_date
        if issues_in_past is not UNSET:
            field_dict["issuesInPast"] = issues_in_past
        if issues_in_future is not UNSET:
            field_dict["issuesInFuture"] = issues_in_future
        if archived is not UNSET:
            field_dict["archived"] = archived
        if allowed_payment_methods is not UNSET:
            field_dict["allowedPaymentMethods"] = allowed_payment_methods
        if connected_company_settings is not UNSET:
            field_dict["connectedCompanySettings"] = connected_company_settings
        if leaf_id is not UNSET:
            field_dict["leafId"] = leaf_id
        if external_billing is not UNSET:
            field_dict["externalBilling"] = external_billing
        if customer_cancellation_blocked is not UNSET:
            field_dict["customerCancellationBlocked"] = customer_cancellation_blocked
        if corporate_account_users is not UNSET:
            field_dict["corporateAccountUsers"] = corporate_account_users
        if corporate_account_invitation_url is not UNSET:
            field_dict["corporateAccountInvitationUrl"] = corporate_account_invitation_url
        if bonus_id is not UNSET:
            field_dict["bonusId"] = bonus_id
        if self_service_hint_tm_id is not UNSET:
            field_dict["selfServiceHintTmId"] = self_service_hint_tm_id
        if managed_by is not UNSET:
            field_dict["managedBy"] = managed_by
        if pdf_template_usage is not UNSET:
            field_dict["pdfTemplateUsage"] = pdf_template_usage
        if partner_settings is not UNSET:
            field_dict["partnerSettings"] = partner_settings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_base_date import ApiBaseDate
        from ..models.offer_connected_company_settings import OfferConnectedCompanySettings
        from ..models.offer_partner_settings import OfferPartnerSettings

        d = src_dict.copy()
        internal_title = d.pop("internalTitle")

        translations = []
        _translations = d.pop("translations")
        for translations_item_data in _translations:
            translations_item = ApiBaseDate.from_dict(translations_item_data)

            translations.append(translations_item)

        pause_able = d.pop("pauseAble", UNSET)

        invoice_address_mandatory = d.pop("invoiceAddressMandatory", UNSET)

        delivery_address_mandatory = d.pop("deliveryAddressMandatory", UNSET)

        multiple_purchases = d.pop("multiplePurchases", UNSET)

        misuse_rule_id = d.pop("misuseRuleId", UNSET)

        def _parse_fixed_start_date(data: object) -> Union[None, Unset, datetime.date]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                fixed_start_date_type_1 = isoparse(data).date()

                return fixed_start_date_type_1
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.date], data)

        fixed_start_date = _parse_fixed_start_date(d.pop("fixedStartDate", UNSET))

        issues_in_past = d.pop("issuesInPast", UNSET)

        issues_in_future = d.pop("issuesInFuture", UNSET)

        archived = d.pop("archived", UNSET)

        allowed_payment_methods = []
        _allowed_payment_methods = d.pop("allowedPaymentMethods", UNSET)
        for allowed_payment_methods_item_data in _allowed_payment_methods or []:
            allowed_payment_methods_item = OfferBaseAllowedPaymentMethodsItem(allowed_payment_methods_item_data)

            allowed_payment_methods.append(allowed_payment_methods_item)

        _connected_company_settings = d.pop("connectedCompanySettings", UNSET)
        connected_company_settings: Union[Unset, OfferConnectedCompanySettings]
        if isinstance(_connected_company_settings, Unset):
            connected_company_settings = UNSET
        else:
            connected_company_settings = OfferConnectedCompanySettings.from_dict(_connected_company_settings)

        leaf_id = d.pop("leafId", UNSET)

        external_billing = d.pop("externalBilling", UNSET)

        customer_cancellation_blocked = d.pop("customerCancellationBlocked", UNSET)

        corporate_account_users = d.pop("corporateAccountUsers", UNSET)

        corporate_account_invitation_url = d.pop("corporateAccountInvitationUrl", UNSET)

        bonus_id = d.pop("bonusId", UNSET)

        self_service_hint_tm_id = d.pop("selfServiceHintTmId", UNSET)

        _managed_by = d.pop("managedBy", UNSET)
        managed_by: Union[Unset, OfferBaseManagedBy]
        if isinstance(_managed_by, Unset):
            managed_by = UNSET
        else:
            managed_by = OfferBaseManagedBy(_managed_by)

        _pdf_template_usage = d.pop("pdfTemplateUsage", UNSET)
        pdf_template_usage: Union[Unset, OfferBasePdfTemplateUsage]
        if isinstance(_pdf_template_usage, Unset):
            pdf_template_usage = UNSET
        else:
            pdf_template_usage = OfferBasePdfTemplateUsage(_pdf_template_usage)

        _partner_settings = d.pop("partnerSettings", UNSET)
        partner_settings: Union[Unset, OfferPartnerSettings]
        if isinstance(_partner_settings, Unset):
            partner_settings = UNSET
        else:
            partner_settings = OfferPartnerSettings.from_dict(_partner_settings)

        offer_base = cls(
            internal_title=internal_title,
            translations=translations,
            pause_able=pause_able,
            invoice_address_mandatory=invoice_address_mandatory,
            delivery_address_mandatory=delivery_address_mandatory,
            multiple_purchases=multiple_purchases,
            misuse_rule_id=misuse_rule_id,
            fixed_start_date=fixed_start_date,
            issues_in_past=issues_in_past,
            issues_in_future=issues_in_future,
            archived=archived,
            allowed_payment_methods=allowed_payment_methods,
            connected_company_settings=connected_company_settings,
            leaf_id=leaf_id,
            external_billing=external_billing,
            customer_cancellation_blocked=customer_cancellation_blocked,
            corporate_account_users=corporate_account_users,
            corporate_account_invitation_url=corporate_account_invitation_url,
            bonus_id=bonus_id,
            self_service_hint_tm_id=self_service_hint_tm_id,
            managed_by=managed_by,
            pdf_template_usage=pdf_template_usage,
            partner_settings=partner_settings,
        )

        offer_base.additional_properties = d
        return offer_base

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
