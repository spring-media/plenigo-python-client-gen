import logging
from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx
from tenacity import retry, retry_if_exception_type, stop_after_attempt, wait_exponential

from ... import errors
from ...client import Client
from ...types import UNSET, Response

log = logging.getLogger(__name__)

from typing import Dict, Optional, Union, cast

from ...models.analytics_count_result import AnalyticsCountResult
from ...models.error_result_base import ErrorResultBase
from ...models.get_new_subscriptions_statistics_interval import GetNewSubscriptionsStatisticsInterval
from ...models.get_new_subscriptions_statistics_sort import GetNewSubscriptionsStatisticsSort
from ...types import UNSET, Unset


def _get_kwargs(
    *,
    client: Client,
    calculation_date: Union[Unset, None, str] = UNSET,
    interval: GetNewSubscriptionsStatisticsInterval,
    size: int,
    sort: Union[Unset, None, GetNewSubscriptionsStatisticsSort] = UNSET,
) -> Dict[str, Any]:
    url = "{}/analytics/subscriptions/new".format(client.api.value)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["calculationDate"] = calculation_date

    json_interval = interval.value

    params["interval"] = json_interval

    params["size"] = size

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


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[AnalyticsCountResult, Any, ErrorResultBase]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = AnalyticsCountResult.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ErrorResultBase.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
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
    *, client: Client, response: httpx.Response
) -> Response[Union[AnalyticsCountResult, Any, ErrorResultBase]]:
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
    *,
    client: Client,
    calculation_date: Union[Unset, None, str] = UNSET,
    interval: GetNewSubscriptionsStatisticsInterval,
    size: int,
    sort: Union[Unset, None, GetNewSubscriptionsStatisticsSort] = UNSET,
) -> Response[Union[AnalyticsCountResult, Any, ErrorResultBase]]:
    """Get new subscriptions

     Get statistical information about new subscriptions within the defined time range.

    Args:
        calculation_date (Union[Unset, None, str]):
        interval (GetNewSubscriptionsStatisticsInterval):
        size (int):
        sort (Union[Unset, None, GetNewSubscriptionsStatisticsSort]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AnalyticsCountResult, Any, ErrorResultBase]]
    """

    kwargs = _get_kwargs(
        client=client,
        calculation_date=calculation_date,
        interval=interval,
        size=size,
        sort=sort,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    calculation_date: Union[Unset, None, str] = UNSET,
    interval: GetNewSubscriptionsStatisticsInterval,
    size: int,
    sort: Union[Unset, None, GetNewSubscriptionsStatisticsSort] = UNSET,
) -> Optional[Union[AnalyticsCountResult, Any, ErrorResultBase]]:
    """Get new subscriptions

     Get statistical information about new subscriptions within the defined time range.

    Args:
        calculation_date (Union[Unset, None, str]):
        interval (GetNewSubscriptionsStatisticsInterval):
        size (int):
        sort (Union[Unset, None, GetNewSubscriptionsStatisticsSort]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AnalyticsCountResult, Any, ErrorResultBase]
    """

    return sync_detailed(
        client=client,
        calculation_date=calculation_date,
        interval=interval,
        size=size,
        sort=sort,
    ).parsed


@retry(
    retry=retry_if_exception_type(errors.RetryableError),
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=30),
)
async def asyncio_detailed(
    *,
    client: Client,
    calculation_date: Union[Unset, None, str] = UNSET,
    interval: GetNewSubscriptionsStatisticsInterval,
    size: int,
    sort: Union[Unset, None, GetNewSubscriptionsStatisticsSort] = UNSET,
) -> Response[Union[AnalyticsCountResult, Any, ErrorResultBase]]:
    """Get new subscriptions

     Get statistical information about new subscriptions within the defined time range.

    Args:
        calculation_date (Union[Unset, None, str]):
        interval (GetNewSubscriptionsStatisticsInterval):
        size (int):
        sort (Union[Unset, None, GetNewSubscriptionsStatisticsSort]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AnalyticsCountResult, Any, ErrorResultBase]]
    """

    kwargs = _get_kwargs(
        client=client,
        calculation_date=calculation_date,
        interval=interval,
        size=size,
        sort=sort,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    calculation_date: Union[Unset, None, str] = UNSET,
    interval: GetNewSubscriptionsStatisticsInterval,
    size: int,
    sort: Union[Unset, None, GetNewSubscriptionsStatisticsSort] = UNSET,
) -> Optional[Union[AnalyticsCountResult, Any, ErrorResultBase]]:
    """Get new subscriptions

     Get statistical information about new subscriptions within the defined time range.

    Args:
        calculation_date (Union[Unset, None, str]):
        interval (GetNewSubscriptionsStatisticsInterval):
        size (int):
        sort (Union[Unset, None, GetNewSubscriptionsStatisticsSort]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AnalyticsCountResult, Any, ErrorResultBase]
    """

    return (
        await asyncio_detailed(
            client=client,
            calculation_date=calculation_date,
            interval=interval,
            size=size,
            sort=sort,
        )
    ).parsed
