import datetime
import logging
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx
from tenacity import RetryError, retry, retry_if_exception_type, stop_after_attempt, wait_exponential

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.activities import Activities
from ...models.error_result_base import ErrorResultBase
from ...models.search_activities_json_object_type import SearchActivitiesJsonObjectType
from ...models.search_activities_sort import SearchActivitiesSort
from ...types import UNSET, Response, Unset

log = logging.getLogger(__name__)


def _get_kwargs(
    customer_id: str,
    *,
    size: Union[Unset, int] = UNSET,
    start_time: Union[Unset, datetime.datetime] = UNSET,
    end_time: Union[Unset, datetime.datetime] = UNSET,
    starting_after: Union[Unset, str] = UNSET,
    ending_before: Union[Unset, str] = UNSET,
    sort: Union[Unset, SearchActivitiesSort] = UNSET,
    json_object_type: Union[Unset, SearchActivitiesJsonObjectType] = UNSET,
    json_object_identifier: Union[Unset, str] = UNSET,
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

    json_json_object_type: Union[Unset, str] = UNSET
    if not isinstance(json_object_type, Unset):
        json_json_object_type = json_object_type.value

    params["jsonObjectType"] = json_json_object_type

    params["jsonObjectIdentifier"] = json_object_identifier

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/activities/{customer_id}",
        "params": params,
    }

    log.debug(_kwargs)

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Activities, ErrorResultBase]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Activities.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ErrorResultBase.from_dict(response.json())

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
) -> Response[Union[Activities, ErrorResultBase]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_all(
    customer_id: str,
    *,
    client: AuthenticatedClient,
    size: Union[Unset, int] = UNSET,
    start_time: Union[Unset, datetime.datetime] = UNSET,
    end_time: Union[Unset, datetime.datetime] = UNSET,
    starting_after: Union[Unset, str] = UNSET,
    ending_before: Union[Unset, str] = UNSET,
    sort: Union[Unset, SearchActivitiesSort] = UNSET,
    json_object_type: Union[Unset, SearchActivitiesJsonObjectType] = UNSET,
    json_object_identifier: Union[Unset, str] = UNSET,
) -> Optional[Union[Activities, ErrorResultBase]]:
    all_results = Activities(items=[])
    # type: ignore

    while True:
        try:
            results = sync_detailed(
                customer_id=customer_id,
                client=client,
                size=size,
                start_time=start_time,
                end_time=end_time,
                starting_after=starting_after,
                ending_before=ending_before,
                sort=sort,
                json_object_type=json_object_type,
                json_object_identifier=json_object_identifier,
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
    customer_id: str,
    *,
    client: AuthenticatedClient,
    size: Union[Unset, int] = UNSET,
    start_time: Union[Unset, datetime.datetime] = UNSET,
    end_time: Union[Unset, datetime.datetime] = UNSET,
    starting_after: Union[Unset, str] = UNSET,
    ending_before: Union[Unset, str] = UNSET,
    sort: Union[Unset, SearchActivitiesSort] = UNSET,
    json_object_type: Union[Unset, SearchActivitiesJsonObjectType] = UNSET,
    json_object_identifier: Union[Unset, str] = UNSET,
) -> Response[Union[Activities, ErrorResultBase]]:
    """Search

     Search all accounting forms that correspond to the given search conditions.

    Args:
        customer_id (str):
        size (Union[Unset, int]):
        start_time (Union[Unset, datetime.datetime]):
        end_time (Union[Unset, datetime.datetime]):
        starting_after (Union[Unset, str]):
        ending_before (Union[Unset, str]):
        sort (Union[Unset, SearchActivitiesSort]):
        json_object_type (Union[Unset, SearchActivitiesJsonObjectType]):
        json_object_identifier (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Activities, ErrorResultBase]]
    """

    kwargs = _get_kwargs(
        customer_id=customer_id,
        size=size,
        start_time=start_time,
        end_time=end_time,
        starting_after=starting_after,
        ending_before=ending_before,
        sort=sort,
        json_object_type=json_object_type,
        json_object_identifier=json_object_identifier,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    customer_id: str,
    *,
    client: AuthenticatedClient,
    size: Union[Unset, int] = UNSET,
    start_time: Union[Unset, datetime.datetime] = UNSET,
    end_time: Union[Unset, datetime.datetime] = UNSET,
    starting_after: Union[Unset, str] = UNSET,
    ending_before: Union[Unset, str] = UNSET,
    sort: Union[Unset, SearchActivitiesSort] = UNSET,
    json_object_type: Union[Unset, SearchActivitiesJsonObjectType] = UNSET,
    json_object_identifier: Union[Unset, str] = UNSET,
) -> Optional[Union[Activities, ErrorResultBase]]:
    """Search

     Search all accounting forms that correspond to the given search conditions.

    Args:
        customer_id (str):
        size (Union[Unset, int]):
        start_time (Union[Unset, datetime.datetime]):
        end_time (Union[Unset, datetime.datetime]):
        starting_after (Union[Unset, str]):
        ending_before (Union[Unset, str]):
        sort (Union[Unset, SearchActivitiesSort]):
        json_object_type (Union[Unset, SearchActivitiesJsonObjectType]):
        json_object_identifier (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Activities, ErrorResultBase]
    """

    return sync_detailed(
        customer_id=customer_id,
        client=client,
        size=size,
        start_time=start_time,
        end_time=end_time,
        starting_after=starting_after,
        ending_before=ending_before,
        sort=sort,
        json_object_type=json_object_type,
        json_object_identifier=json_object_identifier,
    ).parsed


@retry(
    retry=retry_if_exception_type(errors.RetryableError),
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=30),
)
async def asyncio_detailed(
    customer_id: str,
    *,
    client: AuthenticatedClient,
    size: Union[Unset, int] = UNSET,
    start_time: Union[Unset, datetime.datetime] = UNSET,
    end_time: Union[Unset, datetime.datetime] = UNSET,
    starting_after: Union[Unset, str] = UNSET,
    ending_before: Union[Unset, str] = UNSET,
    sort: Union[Unset, SearchActivitiesSort] = UNSET,
    json_object_type: Union[Unset, SearchActivitiesJsonObjectType] = UNSET,
    json_object_identifier: Union[Unset, str] = UNSET,
) -> Response[Union[Activities, ErrorResultBase]]:
    """Search

     Search all accounting forms that correspond to the given search conditions.

    Args:
        customer_id (str):
        size (Union[Unset, int]):
        start_time (Union[Unset, datetime.datetime]):
        end_time (Union[Unset, datetime.datetime]):
        starting_after (Union[Unset, str]):
        ending_before (Union[Unset, str]):
        sort (Union[Unset, SearchActivitiesSort]):
        json_object_type (Union[Unset, SearchActivitiesJsonObjectType]):
        json_object_identifier (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Activities, ErrorResultBase]]
    """

    kwargs = _get_kwargs(
        customer_id=customer_id,
        size=size,
        start_time=start_time,
        end_time=end_time,
        starting_after=starting_after,
        ending_before=ending_before,
        sort=sort,
        json_object_type=json_object_type,
        json_object_identifier=json_object_identifier,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio_all(
    customer_id: str,
    *,
    client: AuthenticatedClient,
    size: Union[Unset, int] = UNSET,
    start_time: Union[Unset, datetime.datetime] = UNSET,
    end_time: Union[Unset, datetime.datetime] = UNSET,
    starting_after: Union[Unset, str] = UNSET,
    ending_before: Union[Unset, str] = UNSET,
    sort: Union[Unset, SearchActivitiesSort] = UNSET,
    json_object_type: Union[Unset, SearchActivitiesJsonObjectType] = UNSET,
    json_object_identifier: Union[Unset, str] = UNSET,
) -> Response[Union[Activities, ErrorResultBase]]:
    all_results = Activities(items=[])
    # type: ignore

    while True:
        try:
            results = (
                await asyncio_detailed(
                    customer_id=customer_id,
                    client=client,
                    size=size,
                    start_time=start_time,
                    end_time=end_time,
                    starting_after=starting_after,
                    ending_before=ending_before,
                    sort=sort,
                    json_object_type=json_object_type,
                    json_object_identifier=json_object_identifier,
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
    customer_id: str,
    *,
    client: AuthenticatedClient,
    size: Union[Unset, int] = UNSET,
    start_time: Union[Unset, datetime.datetime] = UNSET,
    end_time: Union[Unset, datetime.datetime] = UNSET,
    starting_after: Union[Unset, str] = UNSET,
    ending_before: Union[Unset, str] = UNSET,
    sort: Union[Unset, SearchActivitiesSort] = UNSET,
    json_object_type: Union[Unset, SearchActivitiesJsonObjectType] = UNSET,
    json_object_identifier: Union[Unset, str] = UNSET,
) -> Optional[Union[Activities, ErrorResultBase]]:
    """Search

     Search all accounting forms that correspond to the given search conditions.

    Args:
        customer_id (str):
        size (Union[Unset, int]):
        start_time (Union[Unset, datetime.datetime]):
        end_time (Union[Unset, datetime.datetime]):
        starting_after (Union[Unset, str]):
        ending_before (Union[Unset, str]):
        sort (Union[Unset, SearchActivitiesSort]):
        json_object_type (Union[Unset, SearchActivitiesJsonObjectType]):
        json_object_identifier (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Activities, ErrorResultBase]
    """

    return (
        await asyncio_detailed(
            customer_id=customer_id,
            client=client,
            size=size,
            start_time=start_time,
            end_time=end_time,
            starting_after=starting_after,
            ending_before=ending_before,
            sort=sort,
            json_object_type=json_object_type,
            json_object_identifier=json_object_identifier,
        )
    ).parsed
