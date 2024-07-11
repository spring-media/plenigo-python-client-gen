import logging
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx
from tenacity import retry, retry_if_exception_type, stop_after_attempt, wait_exponential

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response

logger = logging.getLogger(__name__)

from ...models.analytics_transactions_result import AnalyticsTransactionsResult
from ...models.error_result import ErrorResult
from ...models.error_result_base import ErrorResultBase
from ...models.get_customer_return_transactions_statistics_interval import (
    GetCustomerReturnTransactionsStatisticsInterval,
)
from ...models.get_customer_return_transactions_statistics_sort import GetCustomerReturnTransactionsStatisticsSort
from ...types import Unset


def _get_kwargs(
    *,
    calculation_date: Union[Unset, str] = UNSET,
    interval: GetCustomerReturnTransactionsStatisticsInterval,
    size: int,
    sort: Union[Unset, GetCustomerReturnTransactionsStatisticsSort] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["calculationDate"] = calculation_date

    json_interval = interval.value
    params["interval"] = json_interval

    params["size"] = size

    json_sort: Union[Unset, str] = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort.value

    params["sort"] = json_sort

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/analytics/transactions/customerReturns",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[AnalyticsTransactionsResult, ErrorResult, ErrorResultBase]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = AnalyticsTransactionsResult.from_dict(response.json())

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
) -> Response[Union[AnalyticsTransactionsResult, ErrorResult, ErrorResultBase]]:
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
    *,
    client: Union[AuthenticatedClient, Client],
    calculation_date: Union[Unset, str] = UNSET,
    interval: GetCustomerReturnTransactionsStatisticsInterval,
    size: int,
    sort: Union[Unset, GetCustomerReturnTransactionsStatisticsSort] = UNSET,
) -> Response[Union[AnalyticsTransactionsResult, ErrorResult, ErrorResultBase]]:
    """Get customer return transactions

     Get statistical information about customer return transactions within the defined time range.

    Args:
        calculation_date (Union[Unset, str]):
        interval (GetCustomerReturnTransactionsStatisticsInterval):
        size (int):
        sort (Union[Unset, GetCustomerReturnTransactionsStatisticsSort]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AnalyticsTransactionsResult, ErrorResult, ErrorResultBase]]
    """

    kwargs = _get_kwargs(
        calculation_date=calculation_date,
        interval=interval,
        size=size,
        sort=sort,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    calculation_date: Union[Unset, str] = UNSET,
    interval: GetCustomerReturnTransactionsStatisticsInterval,
    size: int,
    sort: Union[Unset, GetCustomerReturnTransactionsStatisticsSort] = UNSET,
) -> Optional[Union[AnalyticsTransactionsResult, ErrorResult, ErrorResultBase]]:
    """Get customer return transactions

     Get statistical information about customer return transactions within the defined time range.

    Args:
        calculation_date (Union[Unset, str]):
        interval (GetCustomerReturnTransactionsStatisticsInterval):
        size (int):
        sort (Union[Unset, GetCustomerReturnTransactionsStatisticsSort]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AnalyticsTransactionsResult, ErrorResult, ErrorResultBase]
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
    client: Union[AuthenticatedClient, Client],
    calculation_date: Union[Unset, str] = UNSET,
    interval: GetCustomerReturnTransactionsStatisticsInterval,
    size: int,
    sort: Union[Unset, GetCustomerReturnTransactionsStatisticsSort] = UNSET,
) -> Response[Union[AnalyticsTransactionsResult, ErrorResult, ErrorResultBase]]:
    """Get customer return transactions

     Get statistical information about customer return transactions within the defined time range.

    Args:
        calculation_date (Union[Unset, str]):
        interval (GetCustomerReturnTransactionsStatisticsInterval):
        size (int):
        sort (Union[Unset, GetCustomerReturnTransactionsStatisticsSort]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AnalyticsTransactionsResult, ErrorResult, ErrorResultBase]]
    """

    kwargs = _get_kwargs(
        calculation_date=calculation_date,
        interval=interval,
        size=size,
        sort=sort,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    calculation_date: Union[Unset, str] = UNSET,
    interval: GetCustomerReturnTransactionsStatisticsInterval,
    size: int,
    sort: Union[Unset, GetCustomerReturnTransactionsStatisticsSort] = UNSET,
) -> Optional[Union[AnalyticsTransactionsResult, ErrorResult, ErrorResultBase]]:
    """Get customer return transactions

     Get statistical information about customer return transactions within the defined time range.

    Args:
        calculation_date (Union[Unset, str]):
        interval (GetCustomerReturnTransactionsStatisticsInterval):
        size (int):
        sort (Union[Unset, GetCustomerReturnTransactionsStatisticsSort]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AnalyticsTransactionsResult, ErrorResult, ErrorResultBase]
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
