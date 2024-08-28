import datetime
import logging
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx
from tenacity import retry, retry_if_exception_type, stop_after_attempt, wait_exponential

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delivery_list_dates import DeliveryListDates
from ...models.error_result import ErrorResult
from ...models.error_result_base import ErrorResultBase
from ...models.get_delivery_list_dates_for_shared_offer_sort import GetDeliveryListDatesForSharedOfferSort
from ...types import UNSET, Response, Unset

log = logging.getLogger(__name__)


def _get_kwargs(
    delivery_list_id: int,
    source_company_id: str,
    shared_offer_id: int,
    *,
    size: Union[Unset, int] = UNSET,
    start_time: Union[Unset, datetime.datetime] = UNSET,
    end_time: Union[Unset, datetime.datetime] = UNSET,
    starting_after: Union[Unset, str] = UNSET,
    ending_before: Union[Unset, str] = UNSET,
    sort: Union[Unset, GetDeliveryListDatesForSharedOfferSort] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["size"] = size

    json_start_time: Union[Unset, str] = UNSET
    if not isinstance(start_time, Unset):
        json_start_time = start_time.isoformat()
    params["startTime"] = json_start_time

    json_end_time: Union[Unset, str] = UNSET
    if not isinstance(end_time, Unset):
        json_end_time = end_time.isoformat()
    params["endTime"] = json_end_time

    params["startingAfter"] = starting_after

    params["endingBefore"] = ending_before

    json_sort: Union[Unset, str] = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort.value

    params["sort"] = json_sort

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/products/deliveryLists/{delivery_list_id}/dates/shared/{source_company_id}/{shared_offer_id}",
        "params": params,
    }

    log.debug(_kwargs)

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[DeliveryListDates, ErrorResult, ErrorResultBase]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = DeliveryListDates.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ErrorResult.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = ErrorResult.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ErrorResultBase.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.TOO_MANY_REQUESTS:
        response_429 = ErrorResultBase.from_dict(response.json())

        return response_429
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = ErrorResultBase.from_dict(response.json())

        return response_500

    if (response.status_code == HTTPStatus.BAD_GATEWAY) or (response.status_code == HTTPStatus.GATEWAY_TIMEOUT):
        raise errors.RetryableError

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[DeliveryListDates, ErrorResult, ErrorResultBase]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


@retry(
    retry=retry_if_exception_type(errors.RetryableError),
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=30),
)
def sync_detailed(
    delivery_list_id: int,
    source_company_id: str,
    shared_offer_id: int,
    *,
    client: AuthenticatedClient,
    size: Union[Unset, int] = UNSET,
    start_time: Union[Unset, datetime.datetime] = UNSET,
    end_time: Union[Unset, datetime.datetime] = UNSET,
    starting_after: Union[Unset, str] = UNSET,
    ending_before: Union[Unset, str] = UNSET,
    sort: Union[Unset, GetDeliveryListDatesForSharedOfferSort] = UNSET,
) -> Response[Union[DeliveryListDates, ErrorResult, ErrorResultBase]]:
    """Get delivery list dates

     Get delivery list dates that belong to the delivery list identified by the passed delivery list id.

    Args:
        delivery_list_id (int):
        source_company_id (str):
        shared_offer_id (int):
        size (Union[Unset, int]):
        start_time (Union[Unset, datetime.datetime]):
        end_time (Union[Unset, datetime.datetime]):
        starting_after (Union[Unset, str]):
        ending_before (Union[Unset, str]):
        sort (Union[Unset, GetDeliveryListDatesForSharedOfferSort]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DeliveryListDates, ErrorResult, ErrorResultBase]]
    """

    kwargs = _get_kwargs(
        delivery_list_id=delivery_list_id,
        source_company_id=source_company_id,
        shared_offer_id=shared_offer_id,
        size=size,
        start_time=start_time,
        end_time=end_time,
        starting_after=starting_after,
        ending_before=ending_before,
        sort=sort,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    delivery_list_id: int,
    source_company_id: str,
    shared_offer_id: int,
    *,
    client: AuthenticatedClient,
    size: Union[Unset, int] = UNSET,
    start_time: Union[Unset, datetime.datetime] = UNSET,
    end_time: Union[Unset, datetime.datetime] = UNSET,
    starting_after: Union[Unset, str] = UNSET,
    ending_before: Union[Unset, str] = UNSET,
    sort: Union[Unset, GetDeliveryListDatesForSharedOfferSort] = UNSET,
) -> Optional[Union[DeliveryListDates, ErrorResult, ErrorResultBase]]:
    """Get delivery list dates

     Get delivery list dates that belong to the delivery list identified by the passed delivery list id.

    Args:
        delivery_list_id (int):
        source_company_id (str):
        shared_offer_id (int):
        size (Union[Unset, int]):
        start_time (Union[Unset, datetime.datetime]):
        end_time (Union[Unset, datetime.datetime]):
        starting_after (Union[Unset, str]):
        ending_before (Union[Unset, str]):
        sort (Union[Unset, GetDeliveryListDatesForSharedOfferSort]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DeliveryListDates, ErrorResult, ErrorResultBase]
    """

    return sync_detailed(
        delivery_list_id=delivery_list_id,
        source_company_id=source_company_id,
        shared_offer_id=shared_offer_id,
        client=client,
        size=size,
        start_time=start_time,
        end_time=end_time,
        starting_after=starting_after,
        ending_before=ending_before,
        sort=sort,
    ).parsed


@retry(
    retry=retry_if_exception_type(errors.RetryableError),
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=30),
)
async def asyncio_detailed(
    delivery_list_id: int,
    source_company_id: str,
    shared_offer_id: int,
    *,
    client: AuthenticatedClient,
    size: Union[Unset, int] = UNSET,
    start_time: Union[Unset, datetime.datetime] = UNSET,
    end_time: Union[Unset, datetime.datetime] = UNSET,
    starting_after: Union[Unset, str] = UNSET,
    ending_before: Union[Unset, str] = UNSET,
    sort: Union[Unset, GetDeliveryListDatesForSharedOfferSort] = UNSET,
) -> Response[Union[DeliveryListDates, ErrorResult, ErrorResultBase]]:
    """Get delivery list dates

     Get delivery list dates that belong to the delivery list identified by the passed delivery list id.

    Args:
        delivery_list_id (int):
        source_company_id (str):
        shared_offer_id (int):
        size (Union[Unset, int]):
        start_time (Union[Unset, datetime.datetime]):
        end_time (Union[Unset, datetime.datetime]):
        starting_after (Union[Unset, str]):
        ending_before (Union[Unset, str]):
        sort (Union[Unset, GetDeliveryListDatesForSharedOfferSort]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DeliveryListDates, ErrorResult, ErrorResultBase]]
    """

    kwargs = _get_kwargs(
        delivery_list_id=delivery_list_id,
        source_company_id=source_company_id,
        shared_offer_id=shared_offer_id,
        size=size,
        start_time=start_time,
        end_time=end_time,
        starting_after=starting_after,
        ending_before=ending_before,
        sort=sort,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    delivery_list_id: int,
    source_company_id: str,
    shared_offer_id: int,
    *,
    client: AuthenticatedClient,
    size: Union[Unset, int] = UNSET,
    start_time: Union[Unset, datetime.datetime] = UNSET,
    end_time: Union[Unset, datetime.datetime] = UNSET,
    starting_after: Union[Unset, str] = UNSET,
    ending_before: Union[Unset, str] = UNSET,
    sort: Union[Unset, GetDeliveryListDatesForSharedOfferSort] = UNSET,
) -> Optional[Union[DeliveryListDates, ErrorResult, ErrorResultBase]]:
    """Get delivery list dates

     Get delivery list dates that belong to the delivery list identified by the passed delivery list id.

    Args:
        delivery_list_id (int):
        source_company_id (str):
        shared_offer_id (int):
        size (Union[Unset, int]):
        start_time (Union[Unset, datetime.datetime]):
        end_time (Union[Unset, datetime.datetime]):
        starting_after (Union[Unset, str]):
        ending_before (Union[Unset, str]):
        sort (Union[Unset, GetDeliveryListDatesForSharedOfferSort]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DeliveryListDates, ErrorResult, ErrorResultBase]
    """

    return (
        await asyncio_detailed(
            delivery_list_id=delivery_list_id,
            source_company_id=source_company_id,
            shared_offer_id=shared_offer_id,
            client=client,
            size=size,
            start_time=start_time,
            end_time=end_time,
            starting_after=starting_after,
            ending_before=ending_before,
            sort=sort,
        )
    ).parsed
