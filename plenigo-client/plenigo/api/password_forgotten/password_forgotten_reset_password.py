import logging
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx
from tenacity import retry, retry_if_exception_type, stop_after_attempt, wait_exponential

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response

logger = logging.getLogger(__name__)

from ...models.customer_password_forgotten_reset import CustomerPasswordForgottenReset
from ...models.customer_session_token import CustomerSessionToken
from ...models.error_result import ErrorResult
from ...models.error_result_base import ErrorResultBase
from ...models.next_step import NextStep
from ...models.session_limit_reached import SessionLimitReached


def _get_kwargs(
    *,
    body: CustomerPasswordForgottenReset,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/processes/passwordForgotten/resetPassword",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[CustomerSessionToken, ErrorResult, ErrorResultBase, NextStep, SessionLimitReached]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = NextStep.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.ACCEPTED:
        response_202 = CustomerSessionToken.from_dict(response.json())

        return response_202
    if response.status_code == HTTPStatus.MULTI_STATUS:
        response_207 = SessionLimitReached.from_dict(response.json())

        return response_207
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ErrorResult.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = ErrorResult.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = ErrorResult.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ErrorResultBase.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.REQUEST_TIMEOUT:
        response_408 = ErrorResult.from_dict(response.json())

        return response_408
    if response.status_code == HTTPStatus.PRECONDITION_FAILED:
        response_412 = ErrorResult.from_dict(response.json())

        return response_412
    if response.status_code == HTTPStatus.PRECONDITION_REQUIRED:
        response_428 = ErrorResult.from_dict(response.json())

        return response_428
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
) -> Response[Union[CustomerSessionToken, ErrorResult, ErrorResultBase, NextStep, SessionLimitReached]]:
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
    body: CustomerPasswordForgottenReset,
) -> Response[Union[CustomerSessionToken, ErrorResult, ErrorResultBase, NextStep, SessionLimitReached]]:
    """Reset password

     This functionality resets the password of the customer.

    Args:
        body (CustomerPasswordForgottenReset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CustomerSessionToken, ErrorResult, ErrorResultBase, NextStep, SessionLimitReached]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CustomerPasswordForgottenReset,
) -> Optional[Union[CustomerSessionToken, ErrorResult, ErrorResultBase, NextStep, SessionLimitReached]]:
    """Reset password

     This functionality resets the password of the customer.

    Args:
        body (CustomerPasswordForgottenReset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CustomerSessionToken, ErrorResult, ErrorResultBase, NextStep, SessionLimitReached]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


@retry(
    retry=retry_if_exception_type(errors.RetryableError),
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=30),
)
async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CustomerPasswordForgottenReset,
) -> Response[Union[CustomerSessionToken, ErrorResult, ErrorResultBase, NextStep, SessionLimitReached]]:
    """Reset password

     This functionality resets the password of the customer.

    Args:
        body (CustomerPasswordForgottenReset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CustomerSessionToken, ErrorResult, ErrorResultBase, NextStep, SessionLimitReached]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CustomerPasswordForgottenReset,
) -> Optional[Union[CustomerSessionToken, ErrorResult, ErrorResultBase, NextStep, SessionLimitReached]]:
    """Reset password

     This functionality resets the password of the customer.

    Args:
        body (CustomerPasswordForgottenReset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CustomerSessionToken, ErrorResult, ErrorResultBase, NextStep, SessionLimitReached]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
