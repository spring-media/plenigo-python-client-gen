import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.activity_activity_type import ActivityActivityType
from ..models.activity_changed_by_type import ActivityChangedByType
from ..models.activity_json_object_type import ActivityJsonObjectType
from ..models.activity_reason import ActivityReason
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_new_object import ActivityNewObject
    from ..models.activity_old_object import ActivityOldObject


T = TypeVar("T", bound="Activity")


@attr.s(auto_attribs=True)
class Activity:
    """
    Attributes:
        activity_id (Union[Unset, int]): unique id of the activity
        changed_date (Union[Unset, datetime.datetime]): date the activity entity was changed with date-time notation as
            defined by RFC 3339, section 5.6, for example, 2017-07-21T17:32:28Z
        changed_by (Union[Unset, str]): id who changed the activity
        changed_by_type (Union[Unset, ActivityChangedByType]): type of changed by
        customer_id (Union[Unset, str]): unique id of the customer the activity is related to
        activity_type (Union[Unset, ActivityActivityType]): type of the activity. When activity type is COMMENTS, EMAIL,
            LETTER or PHONE then newObject will contain a activity message.
        json_object_type (Union[Unset, ActivityJsonObjectType]): type of the json object
        json_object_identifier (Union[Unset, str]): unique id of the owner object of this activity
        old_object (Union[Unset, ActivityOldObject]): json object with the old data
        new_object (Union[Unset, ActivityNewObject]): json object with the new data
        reason (Union[Unset, ActivityReason]): reason of the activity
    """

    activity_id: Union[Unset, int] = UNSET
    changed_date: Union[Unset, datetime.datetime] = UNSET
    changed_by: Union[Unset, str] = UNSET
    changed_by_type: Union[Unset, ActivityChangedByType] = UNSET
    customer_id: Union[Unset, str] = UNSET
    activity_type: Union[Unset, ActivityActivityType] = UNSET
    json_object_type: Union[Unset, ActivityJsonObjectType] = UNSET
    json_object_identifier: Union[Unset, str] = UNSET
    old_object: Union[Unset, "ActivityOldObject"] = UNSET
    new_object: Union[Unset, "ActivityNewObject"] = UNSET
    reason: Union[Unset, ActivityReason] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        activity_id = self.activity_id
        changed_date: Union[Unset, str] = UNSET
        if not isinstance(self.changed_date, Unset):
            changed_date = self.changed_date.isoformat()

        changed_by = self.changed_by
        changed_by_type: Union[Unset, str] = UNSET
        if not isinstance(self.changed_by_type, Unset):
            changed_by_type = self.changed_by_type.value

        customer_id = self.customer_id
        activity_type: Union[Unset, str] = UNSET
        if not isinstance(self.activity_type, Unset):
            activity_type = self.activity_type.value

        json_object_type: Union[Unset, str] = UNSET
        if not isinstance(self.json_object_type, Unset):
            json_object_type = self.json_object_type.value

        json_object_identifier = self.json_object_identifier
        old_object: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.old_object, Unset):
            old_object = self.old_object.to_dict()

        new_object: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.new_object, Unset):
            new_object = self.new_object.to_dict()

        reason: Union[Unset, str] = UNSET
        if not isinstance(self.reason, Unset):
            reason = self.reason.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if activity_id is not UNSET:
            field_dict["activityId"] = activity_id
        if changed_date is not UNSET:
            field_dict["changedDate"] = changed_date
        if changed_by is not UNSET:
            field_dict["changedBy"] = changed_by
        if changed_by_type is not UNSET:
            field_dict["changedByType"] = changed_by_type
        if customer_id is not UNSET:
            field_dict["customerId"] = customer_id
        if activity_type is not UNSET:
            field_dict["activityType"] = activity_type
        if json_object_type is not UNSET:
            field_dict["jsonObjectType"] = json_object_type
        if json_object_identifier is not UNSET:
            field_dict["jsonObjectIdentifier"] = json_object_identifier
        if old_object is not UNSET:
            field_dict["oldObject"] = old_object
        if new_object is not UNSET:
            field_dict["newObject"] = new_object
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.activity_new_object import ActivityNewObject
        from ..models.activity_old_object import ActivityOldObject

        d = src_dict.copy()
        activity_id = d.pop("activityId", UNSET)

        _changed_date = d.pop("changedDate", UNSET)
        changed_date: Union[Unset, datetime.datetime]
        if isinstance(_changed_date, Unset):
            changed_date = UNSET
        else:
            changed_date = isoparse(_changed_date)

        changed_by = d.pop("changedBy", UNSET)

        _changed_by_type = d.pop("changedByType", UNSET)
        changed_by_type: Union[Unset, ActivityChangedByType]
        if isinstance(_changed_by_type, Unset):
            changed_by_type = UNSET
        else:
            changed_by_type = ActivityChangedByType(_changed_by_type)

        customer_id = d.pop("customerId", UNSET)

        _activity_type = d.pop("activityType", UNSET)
        activity_type: Union[Unset, ActivityActivityType]
        if isinstance(_activity_type, Unset):
            activity_type = UNSET
        else:
            activity_type = ActivityActivityType(_activity_type)

        _json_object_type = d.pop("jsonObjectType", UNSET)
        json_object_type: Union[Unset, ActivityJsonObjectType]
        if isinstance(_json_object_type, Unset):
            json_object_type = UNSET
        else:
            json_object_type = ActivityJsonObjectType(_json_object_type)

        json_object_identifier = d.pop("jsonObjectIdentifier", UNSET)

        _old_object = d.pop("oldObject", UNSET)
        old_object: Union[Unset, ActivityOldObject]
        if isinstance(_old_object, Unset):
            old_object = UNSET
        else:
            old_object = ActivityOldObject.from_dict(_old_object)

        _new_object = d.pop("newObject", UNSET)
        new_object: Union[Unset, ActivityNewObject]
        if isinstance(_new_object, Unset):
            new_object = UNSET
        else:
            new_object = ActivityNewObject.from_dict(_new_object)

        _reason = d.pop("reason", UNSET)
        reason: Union[Unset, ActivityReason]
        if isinstance(_reason, Unset):
            reason = UNSET
        else:
            reason = ActivityReason(_reason)

        activity = cls(
            activity_id=activity_id,
            changed_date=changed_date,
            changed_by=changed_by,
            changed_by_type=changed_by_type,
            customer_id=customer_id,
            activity_type=activity_type,
            json_object_type=json_object_type,
            json_object_identifier=json_object_identifier,
            old_object=old_object,
            new_object=new_object,
            reason=reason,
        )

        activity.additional_properties = d
        return activity

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
