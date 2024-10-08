import logging
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx
from tenacity import retry, retry_if_exception_type, stop_after_attempt, wait_exponential

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_result import ErrorResult
from ...models.error_result_base import ErrorResultBase
from ...models.get_sort_tree_leaf_by_type_type import GetSortTreeLeafByTypeType
from ...models.sort_tree_leaf import SortTreeLeaf
from ...types import Response

log = logging.getLogger(__name__)


def _get_kwargs(
    sort_tree_leaf_id: int,
    type: GetSortTreeLeafByTypeType,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/settings/sortTreeLeafs/{sort_tree_leaf_id}/byType/{type}",
    }

    log.debug(_kwargs)

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResult, ErrorResultBase, SortTreeLeaf]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SortTreeLeaf.from_dict(response.json())

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
) -> Response[Union[ErrorResult, ErrorResultBase, SortTreeLeaf]]:
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
    sort_tree_leaf_id: int,
    type: GetSortTreeLeafByTypeType,
    *,
    client: AuthenticatedClient,
) -> Response[Union[ErrorResult, ErrorResultBase, SortTreeLeaf]]:
    """Get sort tree leaf by id and type

     Get sort tree leaf that is identified by the passed sort tree leaf id and type.

    Args:
        sort_tree_leaf_id (int):
        type (GetSortTreeLeafByTypeType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResult, ErrorResultBase, SortTreeLeaf]]
    """

    kwargs = _get_kwargs(
        sort_tree_leaf_id=sort_tree_leaf_id,
        type=type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    sort_tree_leaf_id: int,
    type: GetSortTreeLeafByTypeType,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[ErrorResult, ErrorResultBase, SortTreeLeaf]]:
    """Get sort tree leaf by id and type

     Get sort tree leaf that is identified by the passed sort tree leaf id and type.

    Args:
        sort_tree_leaf_id (int):
        type (GetSortTreeLeafByTypeType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResult, ErrorResultBase, SortTreeLeaf]
    """

    return sync_detailed(
        sort_tree_leaf_id=sort_tree_leaf_id,
        type=type,
        client=client,
    ).parsed


@retry(
    retry=retry_if_exception_type(errors.RetryableError),
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=30),
)
async def asyncio_detailed(
    sort_tree_leaf_id: int,
    type: GetSortTreeLeafByTypeType,
    *,
    client: AuthenticatedClient,
) -> Response[Union[ErrorResult, ErrorResultBase, SortTreeLeaf]]:
    """Get sort tree leaf by id and type

     Get sort tree leaf that is identified by the passed sort tree leaf id and type.

    Args:
        sort_tree_leaf_id (int):
        type (GetSortTreeLeafByTypeType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResult, ErrorResultBase, SortTreeLeaf]]
    """

    kwargs = _get_kwargs(
        sort_tree_leaf_id=sort_tree_leaf_id,
        type=type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    sort_tree_leaf_id: int,
    type: GetSortTreeLeafByTypeType,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[ErrorResult, ErrorResultBase, SortTreeLeaf]]:
    """Get sort tree leaf by id and type

     Get sort tree leaf that is identified by the passed sort tree leaf id and type.

    Args:
        sort_tree_leaf_id (int):
        type (GetSortTreeLeafByTypeType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResult, ErrorResultBase, SortTreeLeaf]
    """

    return (
        await asyncio_detailed(
            sort_tree_leaf_id=sort_tree_leaf_id,
            type=type,
            client=client,
        )
    ).parsed
