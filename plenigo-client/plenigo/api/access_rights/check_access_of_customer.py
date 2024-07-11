import logging
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx
from tenacity import retry, retry_if_exception_type, stop_after_attempt, wait_exponential

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response

logger = logging.getLogger(__name__)

from ...models.access_right_data_granted import AccessRightDataGranted
from ...models.error_result import ErrorResult
from ...models.error_result_base import ErrorResultBase


def _get_kwargs(
    customer_id: str,
    *,
    access_right_unique_ids: str,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["accessRightUniqueIds"] = access_right_unique_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/accessRights/{customer_id}/hasAccess",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[AccessRightDataGranted, ErrorResult, ErrorResultBase]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = AccessRightDataGranted.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ErrorResult.from_dict(response.json())

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


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[AccessRightDataGranted, ErrorResult, ErrorResultBase]]:
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
    customer_id: str,
    *,
    client: AuthenticatedClient,
    access_right_unique_ids: str,
) -> Response[Union[AccessRightDataGranted, ErrorResult, ErrorResultBase]]:
    """Check customer has access

     Check if customer has a valid access right for one or multiple access rights identified by the
    provided access right unique ids.

    Args:
        customer_id (str):
        access_right_unique_ids (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AccessRightDataGranted, ErrorResult, ErrorResultBase]]
    """

    kwargs = _get_kwargs(
        customer_id=customer_id,
        access_right_unique_ids=access_right_unique_ids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    customer_id: str,
    *,
    client: AuthenticatedClient,
    access_right_unique_ids: str,
) -> Optional[Union[AccessRightDataGranted, ErrorResult, ErrorResultBase]]:
    """Check customer has access

     Check if customer has a valid access right for one or multiple access rights identified by the
    provided access right unique ids.

    Args:
        customer_id (str):
        access_right_unique_ids (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AccessRightDataGranted, ErrorResult, ErrorResultBase]
    """

    return sync_detailed(
        customer_id=customer_id,
        client=client,
        access_right_unique_ids=access_right_unique_ids,
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
    access_right_unique_ids: str,
) -> Response[Union[AccessRightDataGranted, ErrorResult, ErrorResultBase]]:
    """Check customer has access

     Check if customer has a valid access right for one or multiple access rights identified by the
    provided access right unique ids.

    Args:
        customer_id (str):
        access_right_unique_ids (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AccessRightDataGranted, ErrorResult, ErrorResultBase]]
    """

    kwargs = _get_kwargs(
        customer_id=customer_id,
        access_right_unique_ids=access_right_unique_ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    customer_id: str,
    *,
    client: AuthenticatedClient,
    access_right_unique_ids: str,
) -> Optional[Union[AccessRightDataGranted, ErrorResult, ErrorResultBase]]:
    """Check customer has access

     Check if customer has a valid access right for one or multiple access rights identified by the
    provided access right unique ids.

    Args:
        customer_id (str):
        access_right_unique_ids (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AccessRightDataGranted, ErrorResult, ErrorResultBase]
    """

    return (
        await asyncio_detailed(
            customer_id=customer_id,
            client=client,
            access_right_unique_ids=access_right_unique_ids,
        )
    ).parsed
