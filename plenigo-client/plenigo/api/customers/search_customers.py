import datetime
import logging
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx
from tenacity import RetryError, retry, retry_if_exception_type, stop_after_attempt, wait_exponential

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.customers import Customers
from ...models.error_result import ErrorResult
from ...models.error_result_base import ErrorResultBase
from ...models.search_customers_sort import SearchCustomersSort
from ...types import UNSET, Response, Unset

log = logging.getLogger(__name__)


def _get_kwargs(
    *,
    size: Union[Unset, int] = UNSET,
    start_time: Union[Unset, datetime.datetime] = UNSET,
    end_time: Union[Unset, datetime.datetime] = UNSET,
    starting_after: Union[Unset, str] = UNSET,
    ending_before: Union[Unset, str] = UNSET,
    sort: Union[Unset, SearchCustomersSort] = UNSET,
    external_system_id: Union[Unset, str] = UNSET,
    email: Union[Unset, str] = UNSET,
    username: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: dict[str, Any] = {}

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

    params["externalSystemId"] = external_system_id

    params["email"] = email

    params["username"] = username

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/customers",
        "params": params,
    }

    log.debug(_kwargs)

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Customers, ErrorResult, ErrorResultBase]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Customers.from_dict(response.json())

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
    if response.status_code == HTTPStatus.BAD_GATEWAY:
        response_502 = ErrorResultBase.from_dict(response.json())

        return response_502
    if response.status_code == HTTPStatus.GATEWAY_TIMEOUT:
        response_504 = ErrorResultBase.from_dict(response.json())

        return response_504

    if (response.status_code == HTTPStatus.BAD_GATEWAY) or (response.status_code == HTTPStatus.GATEWAY_TIMEOUT):
        raise errors.RetryableError

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Customers, ErrorResult, ErrorResultBase]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_all(
    *,
    client: AuthenticatedClient,
    size: Union[Unset, int] = UNSET,
    start_time: Union[Unset, datetime.datetime] = UNSET,
    end_time: Union[Unset, datetime.datetime] = UNSET,
    starting_after: Union[Unset, str] = UNSET,
    ending_before: Union[Unset, str] = UNSET,
    sort: Union[Unset, SearchCustomersSort] = UNSET,
    external_system_id: Union[Unset, str] = UNSET,
    email: Union[Unset, str] = UNSET,
    username: Union[Unset, str] = UNSET,
) -> Optional[Union[Customers, ErrorResult, ErrorResultBase]]:
    all_results = Customers(items=[])
    # type: ignore

    while True:
        try:
            results = sync_detailed(
                client=client,
                size=size,
                start_time=start_time,
                end_time=end_time,
                starting_after=starting_after,
                ending_before=ending_before,
                sort=sort,
                external_system_id=external_system_id,
                email=email,
                username=username,
            ).parsed

            if results and not isinstance(results, ErrorResultBase) and not isinstance(results.items, Unset):
                all_results.items.extend(results.items)  # type: ignore

                cursor = results.additional_properties.get("startingAfterId")

                if not cursor:
                    break

                starting_after = cursor  # noqa
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
    *,
    client: AuthenticatedClient,
    size: Union[Unset, int] = UNSET,
    start_time: Union[Unset, datetime.datetime] = UNSET,
    end_time: Union[Unset, datetime.datetime] = UNSET,
    starting_after: Union[Unset, str] = UNSET,
    ending_before: Union[Unset, str] = UNSET,
    sort: Union[Unset, SearchCustomersSort] = UNSET,
    external_system_id: Union[Unset, str] = UNSET,
    email: Union[Unset, str] = UNSET,
    username: Union[Unset, str] = UNSET,
) -> Response[Union[Customers, ErrorResult, ErrorResultBase]]:
    """Search customers

     Search all customers that correspond to the given search conditions. It is important to note that
    email, username, and
    externalSystemid exclude each other so only one query parameter is used. The defined priority is
    email, username, externalSystemId.

    Args:
        size (Union[Unset, int]):
        start_time (Union[Unset, datetime.datetime]):
        end_time (Union[Unset, datetime.datetime]):
        starting_after (Union[Unset, str]):
        ending_before (Union[Unset, str]):
        sort (Union[Unset, SearchCustomersSort]):
        external_system_id (Union[Unset, str]):
        email (Union[Unset, str]):
        username (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Customers, ErrorResult, ErrorResultBase]]
    """

    kwargs = _get_kwargs(
        size=size,
        start_time=start_time,
        end_time=end_time,
        starting_after=starting_after,
        ending_before=ending_before,
        sort=sort,
        external_system_id=external_system_id,
        email=email,
        username=username,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    size: Union[Unset, int] = UNSET,
    start_time: Union[Unset, datetime.datetime] = UNSET,
    end_time: Union[Unset, datetime.datetime] = UNSET,
    starting_after: Union[Unset, str] = UNSET,
    ending_before: Union[Unset, str] = UNSET,
    sort: Union[Unset, SearchCustomersSort] = UNSET,
    external_system_id: Union[Unset, str] = UNSET,
    email: Union[Unset, str] = UNSET,
    username: Union[Unset, str] = UNSET,
) -> Optional[Union[Customers, ErrorResult, ErrorResultBase]]:
    """Search customers

     Search all customers that correspond to the given search conditions. It is important to note that
    email, username, and
    externalSystemid exclude each other so only one query parameter is used. The defined priority is
    email, username, externalSystemId.

    Args:
        size (Union[Unset, int]):
        start_time (Union[Unset, datetime.datetime]):
        end_time (Union[Unset, datetime.datetime]):
        starting_after (Union[Unset, str]):
        ending_before (Union[Unset, str]):
        sort (Union[Unset, SearchCustomersSort]):
        external_system_id (Union[Unset, str]):
        email (Union[Unset, str]):
        username (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Customers, ErrorResult, ErrorResultBase]
    """

    return sync_detailed(
        client=client,
        size=size,
        start_time=start_time,
        end_time=end_time,
        starting_after=starting_after,
        ending_before=ending_before,
        sort=sort,
        external_system_id=external_system_id,
        email=email,
        username=username,
    ).parsed


@retry(
    retry=retry_if_exception_type(errors.RetryableError),
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=30),
)
async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    size: Union[Unset, int] = UNSET,
    start_time: Union[Unset, datetime.datetime] = UNSET,
    end_time: Union[Unset, datetime.datetime] = UNSET,
    starting_after: Union[Unset, str] = UNSET,
    ending_before: Union[Unset, str] = UNSET,
    sort: Union[Unset, SearchCustomersSort] = UNSET,
    external_system_id: Union[Unset, str] = UNSET,
    email: Union[Unset, str] = UNSET,
    username: Union[Unset, str] = UNSET,
) -> Response[Union[Customers, ErrorResult, ErrorResultBase]]:
    """Search customers

     Search all customers that correspond to the given search conditions. It is important to note that
    email, username, and
    externalSystemid exclude each other so only one query parameter is used. The defined priority is
    email, username, externalSystemId.

    Args:
        size (Union[Unset, int]):
        start_time (Union[Unset, datetime.datetime]):
        end_time (Union[Unset, datetime.datetime]):
        starting_after (Union[Unset, str]):
        ending_before (Union[Unset, str]):
        sort (Union[Unset, SearchCustomersSort]):
        external_system_id (Union[Unset, str]):
        email (Union[Unset, str]):
        username (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Customers, ErrorResult, ErrorResultBase]]
    """

    kwargs = _get_kwargs(
        size=size,
        start_time=start_time,
        end_time=end_time,
        starting_after=starting_after,
        ending_before=ending_before,
        sort=sort,
        external_system_id=external_system_id,
        email=email,
        username=username,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio_all(
    *,
    client: AuthenticatedClient,
    size: Union[Unset, int] = UNSET,
    start_time: Union[Unset, datetime.datetime] = UNSET,
    end_time: Union[Unset, datetime.datetime] = UNSET,
    starting_after: Union[Unset, str] = UNSET,
    ending_before: Union[Unset, str] = UNSET,
    sort: Union[Unset, SearchCustomersSort] = UNSET,
    external_system_id: Union[Unset, str] = UNSET,
    email: Union[Unset, str] = UNSET,
    username: Union[Unset, str] = UNSET,
) -> Response[Union[Customers, ErrorResult, ErrorResultBase]]:
    all_results = Customers(items=[])
    # type: ignore

    while True:
        try:
            results = (
                await asyncio_detailed(
                    client=client,
                    size=size,
                    start_time=start_time,
                    end_time=end_time,
                    starting_after=starting_after,
                    ending_before=ending_before,
                    sort=sort,
                    external_system_id=external_system_id,
                    email=email,
                    username=username,
                )
            ).parsed

            if results and not isinstance(results, ErrorResultBase) and not isinstance(results.items, Unset):
                all_results.items.extend(results.items)  # type: ignore

                cursor = results.additional_properties.get("startingAfterId")

                if not cursor:
                    break

                starting_after = cursor  # noqa
            else:
                break
        except RetryError:
            break

    return all_results


async def asyncio(
    *,
    client: AuthenticatedClient,
    size: Union[Unset, int] = UNSET,
    start_time: Union[Unset, datetime.datetime] = UNSET,
    end_time: Union[Unset, datetime.datetime] = UNSET,
    starting_after: Union[Unset, str] = UNSET,
    ending_before: Union[Unset, str] = UNSET,
    sort: Union[Unset, SearchCustomersSort] = UNSET,
    external_system_id: Union[Unset, str] = UNSET,
    email: Union[Unset, str] = UNSET,
    username: Union[Unset, str] = UNSET,
) -> Optional[Union[Customers, ErrorResult, ErrorResultBase]]:
    """Search customers

     Search all customers that correspond to the given search conditions. It is important to note that
    email, username, and
    externalSystemid exclude each other so only one query parameter is used. The defined priority is
    email, username, externalSystemId.

    Args:
        size (Union[Unset, int]):
        start_time (Union[Unset, datetime.datetime]):
        end_time (Union[Unset, datetime.datetime]):
        starting_after (Union[Unset, str]):
        ending_before (Union[Unset, str]):
        sort (Union[Unset, SearchCustomersSort]):
        external_system_id (Union[Unset, str]):
        email (Union[Unset, str]):
        username (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Customers, ErrorResult, ErrorResultBase]
    """

    return (
        await asyncio_detailed(
            client=client,
            size=size,
            start_time=start_time,
            end_time=end_time,
            starting_after=starting_after,
            ending_before=ending_before,
            sort=sort,
            external_system_id=external_system_id,
            email=email,
            username=username,
        )
    ).parsed
