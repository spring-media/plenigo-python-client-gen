import logging
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx
from tenacity import retry, retry_if_exception_type, stop_after_attempt, wait_exponential

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_result_base import ErrorResultBase
from ...models.success_status import SuccessStatus
from ...types import Response

log = logging.getLogger(__name__)


def _get_kwargs(
    customer_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/customers/{customer_id}/gdprExport",
    }

    log.debug(_kwargs)

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResultBase, SuccessStatus]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SuccessStatus.from_dict(response.json())

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
) -> Response[Union[ErrorResultBase, SuccessStatus]]:
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
) -> Response[Union[ErrorResultBase, SuccessStatus]]:
    """Create GDPR data

     *ASYNC* Every call to this endpoint will return a promise ID and create a GDPR request callback that
    contains the customer data requested. The callback also returns the promise ID returned by this call
    to be identified.
    This endpoint is highly limited because of its expensive nature. You can only call it three times
    every five seconds. Unlimited requests can be done by an agent via the plenigo merchant backend.

    Args:
        customer_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResultBase, SuccessStatus]]
    """

    kwargs = _get_kwargs(
        customer_id=customer_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    customer_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[ErrorResultBase, SuccessStatus]]:
    """Create GDPR data

     *ASYNC* Every call to this endpoint will return a promise ID and create a GDPR request callback that
    contains the customer data requested. The callback also returns the promise ID returned by this call
    to be identified.
    This endpoint is highly limited because of its expensive nature. You can only call it three times
    every five seconds. Unlimited requests can be done by an agent via the plenigo merchant backend.

    Args:
        customer_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResultBase, SuccessStatus]
    """

    return sync_detailed(
        customer_id=customer_id,
        client=client,
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
) -> Response[Union[ErrorResultBase, SuccessStatus]]:
    """Create GDPR data

     *ASYNC* Every call to this endpoint will return a promise ID and create a GDPR request callback that
    contains the customer data requested. The callback also returns the promise ID returned by this call
    to be identified.
    This endpoint is highly limited because of its expensive nature. You can only call it three times
    every five seconds. Unlimited requests can be done by an agent via the plenigo merchant backend.

    Args:
        customer_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResultBase, SuccessStatus]]
    """

    kwargs = _get_kwargs(
        customer_id=customer_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    customer_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[ErrorResultBase, SuccessStatus]]:
    """Create GDPR data

     *ASYNC* Every call to this endpoint will return a promise ID and create a GDPR request callback that
    contains the customer data requested. The callback also returns the promise ID returned by this call
    to be identified.
    This endpoint is highly limited because of its expensive nature. You can only call it three times
    every five seconds. Unlimited requests can be done by an agent via the plenigo merchant backend.

    Args:
        customer_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResultBase, SuccessStatus]
    """

    return (
        await asyncio_detailed(
            customer_id=customer_id,
            client=client,
        )
    ).parsed