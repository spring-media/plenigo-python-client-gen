import logging
from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx
from tenacity import retry, retry_if_exception_type, stop_after_attempt, wait_exponential

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.customer_login_identifier_registration import CustomerLoginIdentifierRegistration
from ...models.error_result_base import ErrorResultBase
from ...models.step_token import StepToken
from ...types import Response

log = logging.getLogger(__name__)


def _get_kwargs(
    *,
    body: CustomerLoginIdentifierRegistration,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/processes/registration/loginIdentifier/start",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers

    log.debug(_kwargs)

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ErrorResultBase, StepToken]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = StepToken.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.ALREADY_REPORTED:
        response_208 = cast(Any, None)
        return response_208
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ErrorResultBase.from_dict(response.json())

        return response_400
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
) -> Response[Union[Any, ErrorResultBase, StepToken]]:
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
    body: CustomerLoginIdentifierRegistration,
) -> Response[Union[Any, ErrorResultBase, StepToken]]:
    """Start registration identifier

     This functionality starts the registration process for an existing customer with registration
    identifier.

    Args:
        body (CustomerLoginIdentifierRegistration):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResultBase, StepToken]]
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
    body: CustomerLoginIdentifierRegistration,
) -> Optional[Union[Any, ErrorResultBase, StepToken]]:
    """Start registration identifier

     This functionality starts the registration process for an existing customer with registration
    identifier.

    Args:
        body (CustomerLoginIdentifierRegistration):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResultBase, StepToken]
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
    body: CustomerLoginIdentifierRegistration,
) -> Response[Union[Any, ErrorResultBase, StepToken]]:
    """Start registration identifier

     This functionality starts the registration process for an existing customer with registration
    identifier.

    Args:
        body (CustomerLoginIdentifierRegistration):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResultBase, StepToken]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CustomerLoginIdentifierRegistration,
) -> Optional[Union[Any, ErrorResultBase, StepToken]]:
    """Start registration identifier

     This functionality starts the registration process for an existing customer with registration
    identifier.

    Args:
        body (CustomerLoginIdentifierRegistration):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResultBase, StepToken]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
