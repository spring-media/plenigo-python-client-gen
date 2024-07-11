import logging
from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx
from tenacity import retry, retry_if_exception_type, stop_after_attempt, wait_exponential

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response

logger = logging.getLogger(__name__)

from ...models.error_result_base import ErrorResultBase
from ...models.tax_code import TaxCode


def _get_kwargs(
    tax_code_id: int,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/accounting/taxCodes/{tax_code_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ErrorResultBase, TaxCode]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = TaxCode.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = ErrorResultBase.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ErrorResultBase.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = cast(Any, None)
        return response_500
    if (response.status_code == HTTPStatus.BAD_GATEWAY) or (response.status_code == HTTPStatus.GATEWAY_TIMEOUT):
        raise errors.RetryableError
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, ErrorResultBase, TaxCode]]:
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
    tax_code_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, ErrorResultBase, TaxCode]]:
    """Get the tax code

     Get tax code that is identified by the passed tax code id.

    Args:
        tax_code_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResultBase, TaxCode]]
    """

    kwargs = _get_kwargs(
        tax_code_id=tax_code_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tax_code_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, ErrorResultBase, TaxCode]]:
    """Get the tax code

     Get tax code that is identified by the passed tax code id.

    Args:
        tax_code_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResultBase, TaxCode]
    """

    return sync_detailed(
        tax_code_id=tax_code_id,
        client=client,
    ).parsed


@retry(
    retry=retry_if_exception_type(errors.RetryableError),
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=30),
)
async def asyncio_detailed(
    tax_code_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, ErrorResultBase, TaxCode]]:
    """Get the tax code

     Get tax code that is identified by the passed tax code id.

    Args:
        tax_code_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResultBase, TaxCode]]
    """

    kwargs = _get_kwargs(
        tax_code_id=tax_code_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tax_code_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, ErrorResultBase, TaxCode]]:
    """Get the tax code

     Get tax code that is identified by the passed tax code id.

    Args:
        tax_code_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResultBase, TaxCode]
    """

    return (
        await asyncio_detailed(
            tax_code_id=tax_code_id,
            client=client,
        )
    ).parsed
