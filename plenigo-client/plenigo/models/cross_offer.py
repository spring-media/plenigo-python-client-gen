import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.api_base_changed_by_type import ApiBaseChangedByType
from ..models.api_base_created_by_type import ApiBaseCreatedByType
from ..models.cross_offer_allowed_payment_methods_item import CrossOfferAllowedPaymentMethodsItem
from ..models.cross_offer_managed_by import CrossOfferManagedBy
from ..models.cross_offer_pdf_template_usage import CrossOfferPdfTemplateUsage
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cross_offer_product import CrossOfferProduct
    from ..models.cross_offer_product_group import CrossOfferProductGroup
    from ..models.offer_connected_company_settings import OfferConnectedCompanySettings
    from ..models.offer_partner_settings import OfferPartnerSettings
    from ..models.offer_translation import OfferTranslation
    from ..models.product_tag import ProductTag


T = TypeVar("T", bound="CrossOffer")


@_attrs_define
class CrossOffer:
    """
    Attributes:
        internal_title (str): internal title of the product group
        translations (List['OfferTranslation']): translations associated with this product
        plenigo_offer_id (str): unique id of the offer within a company
        created_date (Union[None, Unset, datetime.datetime]): Time the object was created in RFC 3339 format, e.g.,
            2021-08-30T17:32:28Z
        changed_date (Union[None, Unset, datetime.datetime]): Time the object was changed in RFC 3339 format, e.g.,
            2021-08-30T17:32:28Z
        created_by (Union[Unset, str]): ID of who created the object
        created_by_type (Union[Unset, ApiBaseCreatedByType]): Type of creator
        changed_by (Union[Unset, str]): ID of who changed the object
        changed_by_type (Union[Unset, ApiBaseChangedByType]): Type of changer
        pause_able (Union[Unset, bool]): flag indicating if subscription is pause able
        invoice_address_mandatory (Union[Unset, bool]): flag indicating if invoice address must be provided by the
            customer
        delivery_address_mandatory (Union[Unset, bool]): flag indicating if delivery address must be provided by the
            customer
        multiple_purchases (Union[Unset, bool]): flag indicating if offer can be bought multiple times from the same
            customer
        fixed_start_date (Union[None, Unset, datetime.date]): fixed date the offer starts with
        issues_in_past (Union[Unset, int]): amount of issues that the user can select in the past - cannot be selected
            with fixed start date
        issues_in_future (Union[Unset, int]): amount of issues that the user can select in the future - cannot be
            selected with fixed start date
        archived (Union[Unset, bool]): flag indicating if offer is archived
        allowed_payment_methods (Union[Unset, List[CrossOfferAllowedPaymentMethodsItem]]): additional constraints to the
            payment methods if some of the selected payment methods cannot be used for this offer - there can be no more
            payment methods than selected in the global payment settings section
        connected_company_settings (Union[Unset, OfferConnectedCompanySettings]):
        external_billing (Union[Unset, bool]): indicates if payments are handled by plenigo or an external system
        customer_cancellation_blocked (Union[Unset, bool]): indicates if a subscription cannot be cancelled by a
            customer
        corporate_account_users (Union[Unset, int]): count of allowed corporate account users
        corporate_account_invitation_url (Union[Unset, str]): corporate account invitation url
        self_service_hint_tm_id (Union[Unset, int]): id of the text module used as self service hint
        managed_external (Union[Unset, bool]): flag indicating if offer is managed externally
        managed_by (Union[Unset, CrossOfferManagedBy]): managed by of the given offer.
        pdf_template_usage (Union[Unset, CrossOfferPdfTemplateUsage]): contains the pdf template to use with this offer
        partner_settings (Union[Unset, OfferPartnerSettings]):
        products (Union[Unset, List['CrossOfferProduct']]): products associated with this offer
        product_groups (Union[Unset, List['CrossOfferProductGroup']]): product groups associated with this offer
        product_tags (Union[Unset, List['ProductTag']]): tags associated with this product
    """

    internal_title: str
    translations: List["OfferTranslation"]
    plenigo_offer_id: str
    created_date: Union[None, Unset, datetime.datetime] = UNSET
    changed_date: Union[None, Unset, datetime.datetime] = UNSET
    created_by: Union[Unset, str] = UNSET
    created_by_type: Union[Unset, ApiBaseCreatedByType] = UNSET
    changed_by: Union[Unset, str] = UNSET
    changed_by_type: Union[Unset, ApiBaseChangedByType] = UNSET
    pause_able: Union[Unset, bool] = UNSET
    invoice_address_mandatory: Union[Unset, bool] = UNSET
    delivery_address_mandatory: Union[Unset, bool] = UNSET
    multiple_purchases: Union[Unset, bool] = UNSET
    fixed_start_date: Union[None, Unset, datetime.date] = UNSET
    issues_in_past: Union[Unset, int] = UNSET
    issues_in_future: Union[Unset, int] = UNSET
    archived: Union[Unset, bool] = UNSET
    allowed_payment_methods: Union[Unset, List[CrossOfferAllowedPaymentMethodsItem]] = UNSET
    connected_company_settings: Union[Unset, "OfferConnectedCompanySettings"] = UNSET
    external_billing: Union[Unset, bool] = UNSET
    customer_cancellation_blocked: Union[Unset, bool] = UNSET
    corporate_account_users: Union[Unset, int] = UNSET
    corporate_account_invitation_url: Union[Unset, str] = UNSET
    self_service_hint_tm_id: Union[Unset, int] = UNSET
    managed_external: Union[Unset, bool] = UNSET
    managed_by: Union[Unset, CrossOfferManagedBy] = UNSET
    pdf_template_usage: Union[Unset, CrossOfferPdfTemplateUsage] = UNSET
    partner_settings: Union[Unset, "OfferPartnerSettings"] = UNSET
    products: Union[Unset, List["CrossOfferProduct"]] = UNSET
    product_groups: Union[Unset, List["CrossOfferProductGroup"]] = UNSET
    product_tags: Union[Unset, List["ProductTag"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        internal_title = self.internal_title

        translations = []
        for translations_item_data in self.translations:
            translations_item = translations_item_data.to_dict()
            translations.append(translations_item)

        plenigo_offer_id = self.plenigo_offer_id

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

        created_by = self.created_by

        created_by_type: Union[Unset, str] = UNSET
        if not isinstance(self.created_by_type, Unset):
            created_by_type = self.created_by_type.value

        changed_by = self.changed_by

        changed_by_type: Union[Unset, str] = UNSET
        if not isinstance(self.changed_by_type, Unset):
            changed_by_type = self.changed_by_type.value

        pause_able = self.pause_able

        invoice_address_mandatory = self.invoice_address_mandatory

        delivery_address_mandatory = self.delivery_address_mandatory

        multiple_purchases = self.multiple_purchases

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

        external_billing = self.external_billing

        customer_cancellation_blocked = self.customer_cancellation_blocked

        corporate_account_users = self.corporate_account_users

        corporate_account_invitation_url = self.corporate_account_invitation_url

        self_service_hint_tm_id = self.self_service_hint_tm_id

        managed_external = self.managed_external

        managed_by: Union[Unset, str] = UNSET
        if not isinstance(self.managed_by, Unset):
            managed_by = self.managed_by.value

        pdf_template_usage: Union[Unset, str] = UNSET
        if not isinstance(self.pdf_template_usage, Unset):
            pdf_template_usage = self.pdf_template_usage.value

        partner_settings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.partner_settings, Unset):
            partner_settings = self.partner_settings.to_dict()

        products: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.products, Unset):
            products = []
            for products_item_data in self.products:
                products_item = products_item_data.to_dict()
                products.append(products_item)

        product_groups: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.product_groups, Unset):
            product_groups = []
            for product_groups_item_data in self.product_groups:
                product_groups_item = product_groups_item_data.to_dict()
                product_groups.append(product_groups_item)

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
                "internalTitle": internal_title,
                "translations": translations,
                "plenigoOfferId": plenigo_offer_id,
            }
        )
        if created_date is not UNSET:
            field_dict["createdDate"] = created_date
        if changed_date is not UNSET:
            field_dict["changedDate"] = changed_date
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if created_by_type is not UNSET:
            field_dict["createdByType"] = created_by_type
        if changed_by is not UNSET:
            field_dict["changedBy"] = changed_by
        if changed_by_type is not UNSET:
            field_dict["changedByType"] = changed_by_type
        if pause_able is not UNSET:
            field_dict["pauseAble"] = pause_able
        if invoice_address_mandatory is not UNSET:
            field_dict["invoiceAddressMandatory"] = invoice_address_mandatory
        if delivery_address_mandatory is not UNSET:
            field_dict["deliveryAddressMandatory"] = delivery_address_mandatory
        if multiple_purchases is not UNSET:
            field_dict["multiplePurchases"] = multiple_purchases
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
        if external_billing is not UNSET:
            field_dict["externalBilling"] = external_billing
        if customer_cancellation_blocked is not UNSET:
            field_dict["customerCancellationBlocked"] = customer_cancellation_blocked
        if corporate_account_users is not UNSET:
            field_dict["corporateAccountUsers"] = corporate_account_users
        if corporate_account_invitation_url is not UNSET:
            field_dict["corporateAccountInvitationUrl"] = corporate_account_invitation_url
        if self_service_hint_tm_id is not UNSET:
            field_dict["selfServiceHintTmId"] = self_service_hint_tm_id
        if managed_external is not UNSET:
            field_dict["managedExternal"] = managed_external
        if managed_by is not UNSET:
            field_dict["managedBy"] = managed_by
        if pdf_template_usage is not UNSET:
            field_dict["pdfTemplateUsage"] = pdf_template_usage
        if partner_settings is not UNSET:
            field_dict["partnerSettings"] = partner_settings
        if products is not UNSET:
            field_dict["products"] = products
        if product_groups is not UNSET:
            field_dict["productGroups"] = product_groups
        if product_tags is not UNSET:
            field_dict["productTags"] = product_tags

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.cross_offer_product import CrossOfferProduct
        from ..models.cross_offer_product_group import CrossOfferProductGroup
        from ..models.offer_connected_company_settings import OfferConnectedCompanySettings
        from ..models.offer_partner_settings import OfferPartnerSettings
        from ..models.offer_translation import OfferTranslation
        from ..models.product_tag import ProductTag

        d = src_dict.copy()
        internal_title = d.pop("internalTitle")

        translations = []
        _translations = d.pop("translations")
        for translations_item_data in _translations:
            translations_item = OfferTranslation.from_dict(translations_item_data)

            translations.append(translations_item)

        plenigo_offer_id = d.pop("plenigoOfferId")

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

        created_by = d.pop("createdBy", UNSET)

        _created_by_type = d.pop("createdByType", UNSET)
        created_by_type: Union[Unset, ApiBaseCreatedByType]
        if isinstance(_created_by_type, Unset):
            created_by_type = UNSET
        else:
            created_by_type = ApiBaseCreatedByType(_created_by_type)

        changed_by = d.pop("changedBy", UNSET)

        _changed_by_type = d.pop("changedByType", UNSET)
        changed_by_type: Union[Unset, ApiBaseChangedByType]
        if isinstance(_changed_by_type, Unset):
            changed_by_type = UNSET
        else:
            changed_by_type = ApiBaseChangedByType(_changed_by_type)

        pause_able = d.pop("pauseAble", UNSET)

        invoice_address_mandatory = d.pop("invoiceAddressMandatory", UNSET)

        delivery_address_mandatory = d.pop("deliveryAddressMandatory", UNSET)

        multiple_purchases = d.pop("multiplePurchases", UNSET)

        def _parse_fixed_start_date(data: object) -> Union[None, Unset, datetime.date]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                fixed_start_date_type_0 = isoparse(data).date()

                return fixed_start_date_type_0
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
            allowed_payment_methods_item = CrossOfferAllowedPaymentMethodsItem(allowed_payment_methods_item_data)

            allowed_payment_methods.append(allowed_payment_methods_item)

        _connected_company_settings = d.pop("connectedCompanySettings", UNSET)
        connected_company_settings: Union[Unset, OfferConnectedCompanySettings]
        if isinstance(_connected_company_settings, Unset):
            connected_company_settings = UNSET
        else:
            connected_company_settings = OfferConnectedCompanySettings.from_dict(_connected_company_settings)

        external_billing = d.pop("externalBilling", UNSET)

        customer_cancellation_blocked = d.pop("customerCancellationBlocked", UNSET)

        corporate_account_users = d.pop("corporateAccountUsers", UNSET)

        corporate_account_invitation_url = d.pop("corporateAccountInvitationUrl", UNSET)

        self_service_hint_tm_id = d.pop("selfServiceHintTmId", UNSET)

        managed_external = d.pop("managedExternal", UNSET)

        _managed_by = d.pop("managedBy", UNSET)
        managed_by: Union[Unset, CrossOfferManagedBy]
        if isinstance(_managed_by, Unset):
            managed_by = UNSET
        else:
            managed_by = CrossOfferManagedBy(_managed_by)

        _pdf_template_usage = d.pop("pdfTemplateUsage", UNSET)
        pdf_template_usage: Union[Unset, CrossOfferPdfTemplateUsage]
        if isinstance(_pdf_template_usage, Unset):
            pdf_template_usage = UNSET
        else:
            pdf_template_usage = CrossOfferPdfTemplateUsage(_pdf_template_usage)

        _partner_settings = d.pop("partnerSettings", UNSET)
        partner_settings: Union[Unset, OfferPartnerSettings]
        if isinstance(_partner_settings, Unset):
            partner_settings = UNSET
        else:
            partner_settings = OfferPartnerSettings.from_dict(_partner_settings)

        products = []
        _products = d.pop("products", UNSET)
        for products_item_data in _products or []:
            products_item = CrossOfferProduct.from_dict(products_item_data)

            products.append(products_item)

        product_groups = []
        _product_groups = d.pop("productGroups", UNSET)
        for product_groups_item_data in _product_groups or []:
            product_groups_item = CrossOfferProductGroup.from_dict(product_groups_item_data)

            product_groups.append(product_groups_item)

        product_tags = []
        _product_tags = d.pop("productTags", UNSET)
        for product_tags_item_data in _product_tags or []:
            product_tags_item = ProductTag.from_dict(product_tags_item_data)

            product_tags.append(product_tags_item)

        cross_offer = cls(
            internal_title=internal_title,
            translations=translations,
            plenigo_offer_id=plenigo_offer_id,
            created_date=created_date,
            changed_date=changed_date,
            created_by=created_by,
            created_by_type=created_by_type,
            changed_by=changed_by,
            changed_by_type=changed_by_type,
            pause_able=pause_able,
            invoice_address_mandatory=invoice_address_mandatory,
            delivery_address_mandatory=delivery_address_mandatory,
            multiple_purchases=multiple_purchases,
            fixed_start_date=fixed_start_date,
            issues_in_past=issues_in_past,
            issues_in_future=issues_in_future,
            archived=archived,
            allowed_payment_methods=allowed_payment_methods,
            connected_company_settings=connected_company_settings,
            external_billing=external_billing,
            customer_cancellation_blocked=customer_cancellation_blocked,
            corporate_account_users=corporate_account_users,
            corporate_account_invitation_url=corporate_account_invitation_url,
            self_service_hint_tm_id=self_service_hint_tm_id,
            managed_external=managed_external,
            managed_by=managed_by,
            pdf_template_usage=pdf_template_usage,
            partner_settings=partner_settings,
            products=products,
            product_groups=product_groups,
            product_tags=product_tags,
        )

        cross_offer.additional_properties = d
        return cross_offer

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
