import logging
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx
from tenacity import RetryError, retry, retry_if_exception_type, stop_after_attempt, wait_exponential

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_result_base import ErrorResultBase
from ...models.product_access_right import ProductAccessRight
from ...types import Response, Unset

log = logging.getLogger(__name__)


def _get_kwargs(
    access_right_id: int,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/products/accessRights/{access_right_id}",
    }

    log.debug(_kwargs)

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResultBase, ProductAccessRight]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ProductAccessRight.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ErrorResultBase.from_dict(response.json())

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
) -> Response[Union[ErrorResultBase, ProductAccessRight]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_all(
    access_right_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[ErrorResultBase, ProductAccessRight]]:
    all_results = ProductAccessRight(items=[])
    # type: ignore

    while True:
        try:
            results = sync_detailed(
                access_right_id=access_right_id,
                client=client,
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
    access_right_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[ErrorResultBase, ProductAccessRight]]:
    """Get

     Get access right that is identified by the passed access right id.

    Args:
        access_right_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResultBase, ProductAccessRight]]
    """

    kwargs = _get_kwargs(
        access_right_id=access_right_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    access_right_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[ErrorResultBase, ProductAccessRight]]:
    """Get

     Get access right that is identified by the passed access right id.

    Args:
        access_right_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResultBase, ProductAccessRight]
    """

    return sync_detailed(
        access_right_id=access_right_id,
        client=client,
    ).parsed


@retry(
    retry=retry_if_exception_type(errors.RetryableError),
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=30),
)
async def asyncio_detailed(
    access_right_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[ErrorResultBase, ProductAccessRight]]:
    """Get

     Get access right that is identified by the passed access right id.

    Args:
        access_right_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResultBase, ProductAccessRight]]
    """

    kwargs = _get_kwargs(
        access_right_id=access_right_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio_all(
    access_right_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[ErrorResultBase, ProductAccessRight]]:
    all_results = ProductAccessRight(items=[])
    # type: ignore

    while True:
        try:
            results = (
                await asyncio_detailed(
                    access_right_id=access_right_id,
                    client=client,
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
    access_right_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[ErrorResultBase, ProductAccessRight]]:
    """Get

     Get access right that is identified by the passed access right id.

    Args:
        access_right_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResultBase, ProductAccessRight]
    """

    return (
        await asyncio_detailed(
            access_right_id=access_right_id,
            client=client,
        )
    ).parsed
