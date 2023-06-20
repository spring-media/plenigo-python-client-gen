import logging
from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx
from tenacity import retry, retry_if_exception_type, stop_after_attempt, wait_exponential

from ... import errors
from ...client import Client
from ...types import Response

log = logging.getLogger(__name__)

from typing import Dict, cast

from ...models.customer_login_identifier_registration import CustomerLoginIdentifierRegistration
from ...models.error_result_base import ErrorResultBase
from ...models.step_token import StepToken


def _get_kwargs(
    *,
    client: Client,
    json_body: CustomerLoginIdentifierRegistration,
) -> Dict[str, Any]:
    url = "{}/processes/registration/loginIdentifier/start".format(client.api.value)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    kwargs = {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "json": json_json_body,
    }

    log.debug(kwargs)

    return kwargs


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Any, ErrorResultBase, StepToken]]:
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


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Any, ErrorResultBase, StepToken]]:
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
    json_body: CustomerLoginIdentifierRegistration,
) -> Response[Union[Any, ErrorResultBase, StepToken]]:
    """Start registration identifier

     This functionality starts the registration process for an exisiting customer with registration
    identifier.

    Args:
        json_body (CustomerLoginIdentifierRegistration):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResultBase, StepToken]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    json_body: CustomerLoginIdentifierRegistration,
) -> Optional[Union[Any, ErrorResultBase, StepToken]]:
    """Start registration identifier

     This functionality starts the registration process for an exisiting customer with registration
    identifier.

    Args:
        json_body (CustomerLoginIdentifierRegistration):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResultBase, StepToken]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


@retry(
    retry=retry_if_exception_type(errors.RetryableError),
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=30),
)
async def asyncio_detailed(
    *,
    client: Client,
    json_body: CustomerLoginIdentifierRegistration,
) -> Response[Union[Any, ErrorResultBase, StepToken]]:
    """Start registration identifier

     This functionality starts the registration process for an exisiting customer with registration
    identifier.

    Args:
        json_body (CustomerLoginIdentifierRegistration):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResultBase, StepToken]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    json_body: CustomerLoginIdentifierRegistration,
) -> Optional[Union[Any, ErrorResultBase, StepToken]]:
    """Start registration identifier

     This functionality starts the registration process for an exisiting customer with registration
    identifier.

    Args:
        json_body (CustomerLoginIdentifierRegistration):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResultBase, StepToken]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
