import logging
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx
from tenacity import retry, retry_if_exception_type, stop_after_attempt, wait_exponential

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response

log = logging.getLogger(__name__)

import datetime
from typing import Dict, Optional, Union

from ...models.delivery_list_dates import DeliveryListDates
from ...models.error_result_base import ErrorResultBase
from ...models.get_delivery_list_dates_sort import GetDeliveryListDatesSort
from ...types import UNSET, Unset


def _get_kwargs(
    delivery_list_id: int,
    *,
    client: AuthenticatedClient,
    size: Union[Unset, None, int] = UNSET,
    start_time: Union[Unset, None, datetime.datetime] = UNSET,
    end_time: Union[Unset, None, datetime.datetime] = UNSET,
    starting_after: Union[Unset, None, str] = UNSET,
    ending_before: Union[Unset, None, str] = UNSET,
    sort: Union[Unset, None, GetDeliveryListDatesSort] = UNSET,
) -> Dict[str, Any]:
    url = "{}/products/deliveryLists/{deliveryListId}/dates".format(client.api.value, deliveryListId=delivery_list_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["size"] = size

    json_start_time: Union[Unset, None, str] = UNSET
    if not isinstance(start_time, Unset):
        json_start_time = start_time.isoformat() if start_time else None

    params["startTime"] = json_start_time

    json_end_time: Union[Unset, None, str] = UNSET
    if not isinstance(end_time, Unset):
        json_end_time = end_time.isoformat() if end_time else None

    params["endTime"] = json_end_time

    params["startingAfter"] = starting_after

    params["endingBefore"] = ending_before

    json_sort: Union[Unset, None, str] = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort.value if sort else None

    params["sort"] = json_sort

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    kwargs = {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "params": params,
    }

    log.debug(kwargs)

    return kwargs


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[DeliveryListDates, ErrorResultBase]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = DeliveryListDates.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ErrorResultBase.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = ErrorResultBase.from_dict(response.json())

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


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[DeliveryListDates, ErrorResultBase]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )  # type: ignore


@retry(
    retry=retry_if_exception_type(errors.RetryableError),
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=30),
)
def sync_detailed(
    delivery_list_id: int,
    *,
    client: AuthenticatedClient,
    size: Union[Unset, None, int] = UNSET,
    start_time: Union[Unset, None, datetime.datetime] = UNSET,
    end_time: Union[Unset, None, datetime.datetime] = UNSET,
    starting_after: Union[Unset, None, str] = UNSET,
    ending_before: Union[Unset, None, str] = UNSET,
    sort: Union[Unset, None, GetDeliveryListDatesSort] = UNSET,
) -> Response[Union[DeliveryListDates, ErrorResultBase]]:
    """Get delivery list dates

     Get delivery list dates that belong to the delivery list identified by the passed delivery list id.

    Args:
        delivery_list_id (int):
        size (Union[Unset, None, int]):
        start_time (Union[Unset, None, datetime.datetime]):
        end_time (Union[Unset, None, datetime.datetime]):
        starting_after (Union[Unset, None, str]):
        ending_before (Union[Unset, None, str]):
        sort (Union[Unset, None, GetDeliveryListDatesSort]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DeliveryListDates, ErrorResultBase]]
    """

    kwargs = _get_kwargs(
        delivery_list_id=delivery_list_id,
        client=client,
        size=size,
        start_time=start_time,
        end_time=end_time,
        starting_after=starting_after,
        ending_before=ending_before,
        sort=sort,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    delivery_list_id: int,
    *,
    client: AuthenticatedClient,
    size: Union[Unset, None, int] = UNSET,
    start_time: Union[Unset, None, datetime.datetime] = UNSET,
    end_time: Union[Unset, None, datetime.datetime] = UNSET,
    starting_after: Union[Unset, None, str] = UNSET,
    ending_before: Union[Unset, None, str] = UNSET,
    sort: Union[Unset, None, GetDeliveryListDatesSort] = UNSET,
) -> Optional[Union[DeliveryListDates, ErrorResultBase]]:
    """Get delivery list dates

     Get delivery list dates that belong to the delivery list identified by the passed delivery list id.

    Args:
        delivery_list_id (int):
        size (Union[Unset, None, int]):
        start_time (Union[Unset, None, datetime.datetime]):
        end_time (Union[Unset, None, datetime.datetime]):
        starting_after (Union[Unset, None, str]):
        ending_before (Union[Unset, None, str]):
        sort (Union[Unset, None, GetDeliveryListDatesSort]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DeliveryListDates, ErrorResultBase]
    """

    return sync_detailed(
        delivery_list_id=delivery_list_id,
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
    *,
    client: AuthenticatedClient,
    size: Union[Unset, None, int] = UNSET,
    start_time: Union[Unset, None, datetime.datetime] = UNSET,
    end_time: Union[Unset, None, datetime.datetime] = UNSET,
    starting_after: Union[Unset, None, str] = UNSET,
    ending_before: Union[Unset, None, str] = UNSET,
    sort: Union[Unset, None, GetDeliveryListDatesSort] = UNSET,
) -> Response[Union[DeliveryListDates, ErrorResultBase]]:
    """Get delivery list dates

     Get delivery list dates that belong to the delivery list identified by the passed delivery list id.

    Args:
        delivery_list_id (int):
        size (Union[Unset, None, int]):
        start_time (Union[Unset, None, datetime.datetime]):
        end_time (Union[Unset, None, datetime.datetime]):
        starting_after (Union[Unset, None, str]):
        ending_before (Union[Unset, None, str]):
        sort (Union[Unset, None, GetDeliveryListDatesSort]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DeliveryListDates, ErrorResultBase]]
    """

    kwargs = _get_kwargs(
        delivery_list_id=delivery_list_id,
        client=client,
        size=size,
        start_time=start_time,
        end_time=end_time,
        starting_after=starting_after,
        ending_before=ending_before,
        sort=sort,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    delivery_list_id: int,
    *,
    client: AuthenticatedClient,
    size: Union[Unset, None, int] = UNSET,
    start_time: Union[Unset, None, datetime.datetime] = UNSET,
    end_time: Union[Unset, None, datetime.datetime] = UNSET,
    starting_after: Union[Unset, None, str] = UNSET,
    ending_before: Union[Unset, None, str] = UNSET,
    sort: Union[Unset, None, GetDeliveryListDatesSort] = UNSET,
) -> Optional[Union[DeliveryListDates, ErrorResultBase]]:
    """Get delivery list dates

     Get delivery list dates that belong to the delivery list identified by the passed delivery list id.

    Args:
        delivery_list_id (int):
        size (Union[Unset, None, int]):
        start_time (Union[Unset, None, datetime.datetime]):
        end_time (Union[Unset, None, datetime.datetime]):
        starting_after (Union[Unset, None, str]):
        ending_before (Union[Unset, None, str]):
        sort (Union[Unset, None, GetDeliveryListDatesSort]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DeliveryListDates, ErrorResultBase]
    """

    return (
        await asyncio_detailed(
            delivery_list_id=delivery_list_id,
            client=client,
            size=size,
            start_time=start_time,
            end_time=end_time,
            starting_after=starting_after,
            ending_before=ending_before,
            sort=sort,
        )
    ).parsed
