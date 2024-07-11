import logging
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx
from tenacity import RetryError, retry, retry_if_exception_type, stop_after_attempt, wait_exponential

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response

logger = logging.getLogger(__name__)

import datetime

from ...models.error_result import ErrorResult
from ...models.error_result_base import ErrorResultBase
from ...models.search_cross_client_subscription_delivery_dates_sort import (
    SearchCrossClientSubscriptionDeliveryDatesSort,
)
from ...models.subscription_delivery_dates import SubscriptionDeliveryDates
from ...types import Unset


def _get_kwargs(
    delivery_list_id: int,
    delivery_list_date_id: int,
    *,
    size: Union[Unset, int] = UNSET,
    start_time: Union[Unset, datetime.datetime] = UNSET,
    end_time: Union[Unset, datetime.datetime] = UNSET,
    starting_after: Union[Unset, str] = UNSET,
    sort: Union[Unset, SearchCrossClientSubscriptionDeliveryDatesSort] = UNSET,
    delivery_customer_id: Union[Unset, str] = UNSET,
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

    json_sort: Union[Unset, str] = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort.value

    params["sort"] = json_sort

    params["deliveryCustomerId"] = delivery_customer_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/subscriptions/crossClient/deliveryLists/{delivery_list_id}/dates/{delivery_list_date_id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResult, ErrorResultBase, SubscriptionDeliveryDates]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SubscriptionDeliveryDates.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ErrorResult.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = ErrorResultBase.from_dict(response.json())

        return response_401
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
) -> Response[Union[ErrorResult, ErrorResultBase, SubscriptionDeliveryDates]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_all(
    delivery_list_id: int,
    delivery_list_date_id: int,
    *,
    client: AuthenticatedClient,
    size: Union[Unset, int] = UNSET,
    start_time: Union[Unset, datetime.datetime] = UNSET,
    end_time: Union[Unset, datetime.datetime] = UNSET,
    starting_after: Union[Unset, str] = UNSET,
    sort: Union[Unset, SearchCrossClientSubscriptionDeliveryDatesSort] = UNSET,
    delivery_customer_id: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResult, ErrorResultBase, SubscriptionDeliveryDates]]:
    all_results = SubscriptionDeliveryDates(items=[])  # type: ignore

    while True:
        try:
            results = sync_detailed(
                delivery_list_id=delivery_list_id,
                delivery_list_date_id=delivery_list_date_id,
                client=client,
                size=size,
                start_time=start_time,
                end_time=end_time,
                starting_after=starting_after,
                sort=sort,
                delivery_customer_id=delivery_customer_id,
            ).parsed

            if results and not isinstance(results, ErrorResultBase) and not isinstance(results.items, Unset):
                all_results.items.extend(results.items)  # type: ignore

                cursor = results.additional_properties.get("startingAfterId")

                if not cursor:
                    break

                starting_after = cursor
            else:
                break
        except RetryError:
            break

    return all_results


@retry(
    retry=retry_if_exception_type(errors.RetryableError),
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=30),
)
def sync_detailed(
    delivery_list_id: int,
    delivery_list_date_id: int,
    *,
    client: AuthenticatedClient,
    size: Union[Unset, int] = UNSET,
    start_time: Union[Unset, datetime.datetime] = UNSET,
    end_time: Union[Unset, datetime.datetime] = UNSET,
    starting_after: Union[Unset, str] = UNSET,
    sort: Union[Unset, SearchCrossClientSubscriptionDeliveryDatesSort] = UNSET,
    delivery_customer_id: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResult, ErrorResultBase, SubscriptionDeliveryDates]]:
    """Search cross client subscription delivery dates

     Search all cross client subscriptions delivery dates that correspond to the given search conditions.

    Args:
        delivery_list_id (int):
        delivery_list_date_id (int):
        size (Union[Unset, int]):
        start_time (Union[Unset, datetime.datetime]):
        end_time (Union[Unset, datetime.datetime]):
        starting_after (Union[Unset, str]):
        sort (Union[Unset, SearchCrossClientSubscriptionDeliveryDatesSort]):
        delivery_customer_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResult, ErrorResultBase, SubscriptionDeliveryDates]]
    """

    kwargs = _get_kwargs(
        delivery_list_id=delivery_list_id,
        delivery_list_date_id=delivery_list_date_id,
        size=size,
        start_time=start_time,
        end_time=end_time,
        starting_after=starting_after,
        sort=sort,
        delivery_customer_id=delivery_customer_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    delivery_list_id: int,
    delivery_list_date_id: int,
    *,
    client: AuthenticatedClient,
    size: Union[Unset, int] = UNSET,
    start_time: Union[Unset, datetime.datetime] = UNSET,
    end_time: Union[Unset, datetime.datetime] = UNSET,
    starting_after: Union[Unset, str] = UNSET,
    sort: Union[Unset, SearchCrossClientSubscriptionDeliveryDatesSort] = UNSET,
    delivery_customer_id: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResult, ErrorResultBase, SubscriptionDeliveryDates]]:
    """Search cross client subscription delivery dates

     Search all cross client subscriptions delivery dates that correspond to the given search conditions.

    Args:
        delivery_list_id (int):
        delivery_list_date_id (int):
        size (Union[Unset, int]):
        start_time (Union[Unset, datetime.datetime]):
        end_time (Union[Unset, datetime.datetime]):
        starting_after (Union[Unset, str]):
        sort (Union[Unset, SearchCrossClientSubscriptionDeliveryDatesSort]):
        delivery_customer_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResult, ErrorResultBase, SubscriptionDeliveryDates]
    """

    return sync_detailed(
        delivery_list_id=delivery_list_id,
        delivery_list_date_id=delivery_list_date_id,
        client=client,
        size=size,
        start_time=start_time,
        end_time=end_time,
        starting_after=starting_after,
        sort=sort,
        delivery_customer_id=delivery_customer_id,
    ).parsed


@retry(
    retry=retry_if_exception_type(errors.RetryableError),
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=30),
)
async def asyncio_detailed(
    delivery_list_id: int,
    delivery_list_date_id: int,
    *,
    client: AuthenticatedClient,
    size: Union[Unset, int] = UNSET,
    start_time: Union[Unset, datetime.datetime] = UNSET,
    end_time: Union[Unset, datetime.datetime] = UNSET,
    starting_after: Union[Unset, str] = UNSET,
    sort: Union[Unset, SearchCrossClientSubscriptionDeliveryDatesSort] = UNSET,
    delivery_customer_id: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResult, ErrorResultBase, SubscriptionDeliveryDates]]:
    """Search cross client subscription delivery dates

     Search all cross client subscriptions delivery dates that correspond to the given search conditions.

    Args:
        delivery_list_id (int):
        delivery_list_date_id (int):
        size (Union[Unset, int]):
        start_time (Union[Unset, datetime.datetime]):
        end_time (Union[Unset, datetime.datetime]):
        starting_after (Union[Unset, str]):
        sort (Union[Unset, SearchCrossClientSubscriptionDeliveryDatesSort]):
        delivery_customer_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResult, ErrorResultBase, SubscriptionDeliveryDates]]
    """

    kwargs = _get_kwargs(
        delivery_list_id=delivery_list_id,
        delivery_list_date_id=delivery_list_date_id,
        size=size,
        start_time=start_time,
        end_time=end_time,
        starting_after=starting_after,
        sort=sort,
        delivery_customer_id=delivery_customer_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio_all(
    delivery_list_id: int,
    delivery_list_date_id: int,
    *,
    client: AuthenticatedClient,
    size: Union[Unset, int] = UNSET,
    start_time: Union[Unset, datetime.datetime] = UNSET,
    end_time: Union[Unset, datetime.datetime] = UNSET,
    starting_after: Union[Unset, str] = UNSET,
    sort: Union[Unset, SearchCrossClientSubscriptionDeliveryDatesSort] = UNSET,
    delivery_customer_id: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResult, ErrorResultBase, SubscriptionDeliveryDates]]:
    all_results = []

    while True:
        try:
            results = (
                await asyncio_detailed(
                    delivery_list_id=delivery_list_id,
                    delivery_list_date_id=delivery_list_date_id,
                    client=client,
                    size=size,
                    start_time=start_time,
                    end_time=end_time,
                    starting_after=starting_after,
                    sort=sort,
                    delivery_customer_id=delivery_customer_id,
                )
            ).parsed

            if results and not isinstance(results, ErrorResultBase) and not isinstance(results.items, Unset):
                all_results.items.extend(results.items)  # type: ignore

                cursor = results.additional_properties.get("startingAfterId")

                if not cursor:
                    break

                starting_after = cursor
            else:
                break
        except RetryError:
            break

    return all_results


async def asyncio(
    delivery_list_id: int,
    delivery_list_date_id: int,
    *,
    client: AuthenticatedClient,
    size: Union[Unset, int] = UNSET,
    start_time: Union[Unset, datetime.datetime] = UNSET,
    end_time: Union[Unset, datetime.datetime] = UNSET,
    starting_after: Union[Unset, str] = UNSET,
    sort: Union[Unset, SearchCrossClientSubscriptionDeliveryDatesSort] = UNSET,
    delivery_customer_id: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResult, ErrorResultBase, SubscriptionDeliveryDates]]:
    """Search cross client subscription delivery dates

     Search all cross client subscriptions delivery dates that correspond to the given search conditions.

    Args:
        delivery_list_id (int):
        delivery_list_date_id (int):
        size (Union[Unset, int]):
        start_time (Union[Unset, datetime.datetime]):
        end_time (Union[Unset, datetime.datetime]):
        starting_after (Union[Unset, str]):
        sort (Union[Unset, SearchCrossClientSubscriptionDeliveryDatesSort]):
        delivery_customer_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResult, ErrorResultBase, SubscriptionDeliveryDates]
    """

    return (
        await asyncio_detailed(
            delivery_list_id=delivery_list_id,
            delivery_list_date_id=delivery_list_date_id,
            client=client,
            size=size,
            start_time=start_time,
            end_time=end_time,
            starting_after=starting_after,
            sort=sort,
            delivery_customer_id=delivery_customer_id,
        )
    ).parsed
