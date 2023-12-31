import logging
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx
from tenacity import retry, retry_if_exception_type, stop_after_attempt, wait_exponential

from ... import errors
from ...client import Client
from ...types import UNSET, Response

log = logging.getLogger(__name__)

from typing import Dict, Optional, Union

from ...models.customer_session_token import CustomerSessionToken
from ...models.error_result_base import ErrorResultBase
from ...types import UNSET, Unset


def _get_kwargs(
    removal_token: str,
    *,
    client: Client,
    session_id: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/processes/login/changeSessions/{removalToken}".format(client.api.value, removalToken=removal_token)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["sessionId"] = session_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    kwargs = {
        "method": "put",
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
) -> Optional[Union[CustomerSessionToken, ErrorResultBase]]:
    if response.status_code == HTTPStatus.ACCEPTED:
        response_202 = CustomerSessionToken.from_dict(response.json())

        return response_202
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
    *, client: Client, response: httpx.Response
) -> Response[Union[CustomerSessionToken, ErrorResultBase]]:
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
    removal_token: str,
    *,
    client: Client,
    session_id: Union[Unset, None, str] = UNSET,
) -> Response[Union[CustomerSessionToken, ErrorResultBase]]:
    """Remove active sessions

     Removes one or all active sessions of a customer. If a session id is provided the specific session
    will be removed otherwise all active sessions
    will be removed.

    Args:
        removal_token (str):
        session_id (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CustomerSessionToken, ErrorResultBase]]
    """

    kwargs = _get_kwargs(
        removal_token=removal_token,
        client=client,
        session_id=session_id,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    removal_token: str,
    *,
    client: Client,
    session_id: Union[Unset, None, str] = UNSET,
) -> Optional[Union[CustomerSessionToken, ErrorResultBase]]:
    """Remove active sessions

     Removes one or all active sessions of a customer. If a session id is provided the specific session
    will be removed otherwise all active sessions
    will be removed.

    Args:
        removal_token (str):
        session_id (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CustomerSessionToken, ErrorResultBase]
    """

    return sync_detailed(
        removal_token=removal_token,
        client=client,
        session_id=session_id,
    ).parsed


@retry(
    retry=retry_if_exception_type(errors.RetryableError),
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=30),
)
async def asyncio_detailed(
    removal_token: str,
    *,
    client: Client,
    session_id: Union[Unset, None, str] = UNSET,
) -> Response[Union[CustomerSessionToken, ErrorResultBase]]:
    """Remove active sessions

     Removes one or all active sessions of a customer. If a session id is provided the specific session
    will be removed otherwise all active sessions
    will be removed.

    Args:
        removal_token (str):
        session_id (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CustomerSessionToken, ErrorResultBase]]
    """

    kwargs = _get_kwargs(
        removal_token=removal_token,
        client=client,
        session_id=session_id,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    removal_token: str,
    *,
    client: Client,
    session_id: Union[Unset, None, str] = UNSET,
) -> Optional[Union[CustomerSessionToken, ErrorResultBase]]:
    """Remove active sessions

     Removes one or all active sessions of a customer. If a session id is provided the specific session
    will be removed otherwise all active sessions
    will be removed.

    Args:
        removal_token (str):
        session_id (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CustomerSessionToken, ErrorResultBase]
    """

    return (
        await asyncio_detailed(
            removal_token=removal_token,
            client=client,
            session_id=session_id,
        )
    ).parsed
