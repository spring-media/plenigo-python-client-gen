import logging
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx
from tenacity import retry, retry_if_exception_type, stop_after_attempt, wait_exponential

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response

logger = logging.getLogger(__name__)

from ...models.error_result import ErrorResult
from ...models.error_result_base import ErrorResultBase
from ...models.success_status import SuccessStatus


def _get_kwargs(
    customer_id: str,
    corporate_account_id: int,
    corporate_account_user_id: int,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": f"/corporateAccounts/{customer_id}/{corporate_account_id}/users/{corporate_account_user_id}/resend",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResult, ErrorResultBase, SuccessStatus]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SuccessStatus.from_dict(response.json())

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
) -> Response[Union[ErrorResult, ErrorResultBase, SuccessStatus]]:
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
    corporate_account_id: int,
    corporate_account_user_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[ErrorResult, ErrorResultBase, SuccessStatus]]:
    """Resend invitation email

     Resend a corporate account user invitation email for the given corporate account.

    Args:
        customer_id (str):
        corporate_account_id (int):
        corporate_account_user_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResult, ErrorResultBase, SuccessStatus]]
    """

    kwargs = _get_kwargs(
        customer_id=customer_id,
        corporate_account_id=corporate_account_id,
        corporate_account_user_id=corporate_account_user_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    customer_id: str,
    corporate_account_id: int,
    corporate_account_user_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[ErrorResult, ErrorResultBase, SuccessStatus]]:
    """Resend invitation email

     Resend a corporate account user invitation email for the given corporate account.

    Args:
        customer_id (str):
        corporate_account_id (int):
        corporate_account_user_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResult, ErrorResultBase, SuccessStatus]
    """

    return sync_detailed(
        customer_id=customer_id,
        corporate_account_id=corporate_account_id,
        corporate_account_user_id=corporate_account_user_id,
        client=client,
    ).parsed


@retry(
    retry=retry_if_exception_type(errors.RetryableError),
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=30),
)
async def asyncio_detailed(
    customer_id: str,
    corporate_account_id: int,
    corporate_account_user_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[ErrorResult, ErrorResultBase, SuccessStatus]]:
    """Resend invitation email

     Resend a corporate account user invitation email for the given corporate account.

    Args:
        customer_id (str):
        corporate_account_id (int):
        corporate_account_user_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResult, ErrorResultBase, SuccessStatus]]
    """

    kwargs = _get_kwargs(
        customer_id=customer_id,
        corporate_account_id=corporate_account_id,
        corporate_account_user_id=corporate_account_user_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    customer_id: str,
    corporate_account_id: int,
    corporate_account_user_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[ErrorResult, ErrorResultBase, SuccessStatus]]:
    """Resend invitation email

     Resend a corporate account user invitation email for the given corporate account.

    Args:
        customer_id (str):
        corporate_account_id (int):
        corporate_account_user_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResult, ErrorResultBase, SuccessStatus]
    """

    return (
        await asyncio_detailed(
            customer_id=customer_id,
            corporate_account_id=corporate_account_id,
            corporate_account_user_id=corporate_account_user_id,
            client=client,
        )
    ).parsed
