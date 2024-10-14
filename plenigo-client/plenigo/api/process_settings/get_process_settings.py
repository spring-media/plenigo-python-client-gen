import logging
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx
from tenacity import retry, retry_if_exception_type, stop_after_attempt, wait_exponential

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_result_base import ErrorResultBase
from ...models.process_data import ProcessData
from ...types import UNSET, Response, Unset

log = logging.getLogger(__name__)


def _get_kwargs(
    *,
    language: Union[Unset, str] = UNSET,
    plenigo_checkout_design_id: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["language"] = language

    params["plenigoCheckoutDesignId"] = plenigo_checkout_design_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/processes/settings",
        "params": params,
    }

    log.debug(_kwargs)

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResultBase, ProcessData]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ProcessData.from_dict(response.json())

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
) -> Response[Union[ErrorResultBase, ProcessData]]:
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
    client: AuthenticatedClient,
    language: Union[Unset, str] = UNSET,
    plenigo_checkout_design_id: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResultBase, ProcessData]]:
    """Get process settings

     Get settings for configuring the SSO and checkout part.

    Args:
        language (Union[Unset, str]):
        plenigo_checkout_design_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResultBase, ProcessData]]
    """

    kwargs = _get_kwargs(
        language=language,
        plenigo_checkout_design_id=plenigo_checkout_design_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    language: Union[Unset, str] = UNSET,
    plenigo_checkout_design_id: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResultBase, ProcessData]]:
    """Get process settings

     Get settings for configuring the SSO and checkout part.

    Args:
        language (Union[Unset, str]):
        plenigo_checkout_design_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResultBase, ProcessData]
    """

    return sync_detailed(
        client=client,
        language=language,
        plenigo_checkout_design_id=plenigo_checkout_design_id,
    ).parsed


@retry(
    retry=retry_if_exception_type(errors.RetryableError),
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=30),
)
async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    language: Union[Unset, str] = UNSET,
    plenigo_checkout_design_id: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResultBase, ProcessData]]:
    """Get process settings

     Get settings for configuring the SSO and checkout part.

    Args:
        language (Union[Unset, str]):
        plenigo_checkout_design_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResultBase, ProcessData]]
    """

    kwargs = _get_kwargs(
        language=language,
        plenigo_checkout_design_id=plenigo_checkout_design_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    language: Union[Unset, str] = UNSET,
    plenigo_checkout_design_id: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResultBase, ProcessData]]:
    """Get process settings

     Get settings for configuring the SSO and checkout part.

    Args:
        language (Union[Unset, str]):
        plenigo_checkout_design_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResultBase, ProcessData]
    """

    return (
        await asyncio_detailed(
            client=client,
            language=language,
            plenigo_checkout_design_id=plenigo_checkout_design_id,
        )
    ).parsed
