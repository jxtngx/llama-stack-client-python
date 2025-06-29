# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, overload

import httpx

from ...types import response_list_params, response_create_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import required_args, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .input_items import (
    InputItemsResource,
    AsyncInputItemsResource,
    InputItemsResourceWithRawResponse,
    AsyncInputItemsResourceWithRawResponse,
    InputItemsResourceWithStreamingResponse,
    AsyncInputItemsResourceWithStreamingResponse,
)
from ..._streaming import Stream, AsyncStream
from ..._base_client import make_request_options
from ...types.response_object import ResponseObject
from ...types.response_list_response import ResponseListResponse
from ...types.response_object_stream import ResponseObjectStream

__all__ = ["ResponsesResource", "AsyncResponsesResource"]


class ResponsesResource(SyncAPIResource):
    @cached_property
    def input_items(self) -> InputItemsResource:
        return InputItemsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ResponsesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#accessing-raw-response-data-eg-headers
        """
        return ResponsesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ResponsesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#with_streaming_response
        """
        return ResponsesResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        *,
        input: Union[str, Iterable[response_create_params.InputUnionMember1]],
        model: str,
        instructions: str | NotGiven = NOT_GIVEN,
        max_infer_iters: int | NotGiven = NOT_GIVEN,
        previous_response_id: str | NotGiven = NOT_GIVEN,
        store: bool | NotGiven = NOT_GIVEN,
        stream: Literal[False] | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        text: response_create_params.Text | NotGiven = NOT_GIVEN,
        tools: Iterable[response_create_params.Tool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResponseObject:
        """
        Create a new OpenAI response.

        Args:
          input: Input message(s) to create the response.

          model: The underlying LLM used for completions.

          previous_response_id: (Optional) if specified, the new response will be a continuation of the previous
              response. This can be used to easily fork-off new responses from existing
              responses.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        input: Union[str, Iterable[response_create_params.InputUnionMember1]],
        model: str,
        stream: Literal[True],
        instructions: str | NotGiven = NOT_GIVEN,
        max_infer_iters: int | NotGiven = NOT_GIVEN,
        previous_response_id: str | NotGiven = NOT_GIVEN,
        store: bool | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        text: response_create_params.Text | NotGiven = NOT_GIVEN,
        tools: Iterable[response_create_params.Tool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Stream[ResponseObjectStream]:
        """
        Create a new OpenAI response.

        Args:
          input: Input message(s) to create the response.

          model: The underlying LLM used for completions.

          previous_response_id: (Optional) if specified, the new response will be a continuation of the previous
              response. This can be used to easily fork-off new responses from existing
              responses.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        input: Union[str, Iterable[response_create_params.InputUnionMember1]],
        model: str,
        stream: bool,
        instructions: str | NotGiven = NOT_GIVEN,
        max_infer_iters: int | NotGiven = NOT_GIVEN,
        previous_response_id: str | NotGiven = NOT_GIVEN,
        store: bool | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        text: response_create_params.Text | NotGiven = NOT_GIVEN,
        tools: Iterable[response_create_params.Tool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResponseObject | Stream[ResponseObjectStream]:
        """
        Create a new OpenAI response.

        Args:
          input: Input message(s) to create the response.

          model: The underlying LLM used for completions.

          previous_response_id: (Optional) if specified, the new response will be a continuation of the previous
              response. This can be used to easily fork-off new responses from existing
              responses.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["input", "model"], ["input", "model", "stream"])
    def create(
        self,
        *,
        input: Union[str, Iterable[response_create_params.InputUnionMember1]],
        model: str,
        instructions: str | NotGiven = NOT_GIVEN,
        max_infer_iters: int | NotGiven = NOT_GIVEN,
        previous_response_id: str | NotGiven = NOT_GIVEN,
        store: bool | NotGiven = NOT_GIVEN,
        stream: Literal[False] | Literal[True] | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        text: response_create_params.Text | NotGiven = NOT_GIVEN,
        tools: Iterable[response_create_params.Tool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResponseObject | Stream[ResponseObjectStream]:
        return self._post(
            "/v1/openai/v1/responses",
            body=maybe_transform(
                {
                    "input": input,
                    "model": model,
                    "instructions": instructions,
                    "max_infer_iters": max_infer_iters,
                    "previous_response_id": previous_response_id,
                    "store": store,
                    "stream": stream,
                    "temperature": temperature,
                    "text": text,
                    "tools": tools,
                },
                response_create_params.ResponseCreateParamsStreaming
                if stream
                else response_create_params.ResponseCreateParamsNonStreaming,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResponseObject,
            stream=stream or False,
            stream_cls=Stream[ResponseObjectStream],
        )

    def retrieve(
        self,
        response_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResponseObject:
        """
        Retrieve an OpenAI response by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not response_id:
            raise ValueError(f"Expected a non-empty value for `response_id` but received {response_id!r}")
        return self._get(
            f"/v1/openai/v1/responses/{response_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResponseObject,
        )

    def list(
        self,
        *,
        after: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        model: str | NotGiven = NOT_GIVEN,
        order: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResponseListResponse:
        """
        List all OpenAI responses.

        Args:
          after: The ID of the last response to return.

          limit: The number of responses to return.

          model: The model to filter responses by.

          order: The order to sort responses by when sorted by created_at ('asc' or 'desc').

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/openai/v1/responses",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "limit": limit,
                        "model": model,
                        "order": order,
                    },
                    response_list_params.ResponseListParams,
                ),
            ),
            cast_to=ResponseListResponse,
        )


class AsyncResponsesResource(AsyncAPIResource):
    @cached_property
    def input_items(self) -> AsyncInputItemsResource:
        return AsyncInputItemsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncResponsesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncResponsesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncResponsesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#with_streaming_response
        """
        return AsyncResponsesResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        *,
        input: Union[str, Iterable[response_create_params.InputUnionMember1]],
        model: str,
        instructions: str | NotGiven = NOT_GIVEN,
        max_infer_iters: int | NotGiven = NOT_GIVEN,
        previous_response_id: str | NotGiven = NOT_GIVEN,
        store: bool | NotGiven = NOT_GIVEN,
        stream: Literal[False] | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        text: response_create_params.Text | NotGiven = NOT_GIVEN,
        tools: Iterable[response_create_params.Tool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResponseObject:
        """
        Create a new OpenAI response.

        Args:
          input: Input message(s) to create the response.

          model: The underlying LLM used for completions.

          previous_response_id: (Optional) if specified, the new response will be a continuation of the previous
              response. This can be used to easily fork-off new responses from existing
              responses.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        input: Union[str, Iterable[response_create_params.InputUnionMember1]],
        model: str,
        stream: Literal[True],
        instructions: str | NotGiven = NOT_GIVEN,
        max_infer_iters: int | NotGiven = NOT_GIVEN,
        previous_response_id: str | NotGiven = NOT_GIVEN,
        store: bool | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        text: response_create_params.Text | NotGiven = NOT_GIVEN,
        tools: Iterable[response_create_params.Tool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncStream[ResponseObjectStream]:
        """
        Create a new OpenAI response.

        Args:
          input: Input message(s) to create the response.

          model: The underlying LLM used for completions.

          previous_response_id: (Optional) if specified, the new response will be a continuation of the previous
              response. This can be used to easily fork-off new responses from existing
              responses.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        input: Union[str, Iterable[response_create_params.InputUnionMember1]],
        model: str,
        stream: bool,
        instructions: str | NotGiven = NOT_GIVEN,
        max_infer_iters: int | NotGiven = NOT_GIVEN,
        previous_response_id: str | NotGiven = NOT_GIVEN,
        store: bool | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        text: response_create_params.Text | NotGiven = NOT_GIVEN,
        tools: Iterable[response_create_params.Tool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResponseObject | AsyncStream[ResponseObjectStream]:
        """
        Create a new OpenAI response.

        Args:
          input: Input message(s) to create the response.

          model: The underlying LLM used for completions.

          previous_response_id: (Optional) if specified, the new response will be a continuation of the previous
              response. This can be used to easily fork-off new responses from existing
              responses.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["input", "model"], ["input", "model", "stream"])
    async def create(
        self,
        *,
        input: Union[str, Iterable[response_create_params.InputUnionMember1]],
        model: str,
        instructions: str | NotGiven = NOT_GIVEN,
        max_infer_iters: int | NotGiven = NOT_GIVEN,
        previous_response_id: str | NotGiven = NOT_GIVEN,
        store: bool | NotGiven = NOT_GIVEN,
        stream: Literal[False] | Literal[True] | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        text: response_create_params.Text | NotGiven = NOT_GIVEN,
        tools: Iterable[response_create_params.Tool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResponseObject | AsyncStream[ResponseObjectStream]:
        return await self._post(
            "/v1/openai/v1/responses",
            body=await async_maybe_transform(
                {
                    "input": input,
                    "model": model,
                    "instructions": instructions,
                    "max_infer_iters": max_infer_iters,
                    "previous_response_id": previous_response_id,
                    "store": store,
                    "stream": stream,
                    "temperature": temperature,
                    "text": text,
                    "tools": tools,
                },
                response_create_params.ResponseCreateParamsStreaming
                if stream
                else response_create_params.ResponseCreateParamsNonStreaming,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResponseObject,
            stream=stream or False,
            stream_cls=AsyncStream[ResponseObjectStream],
        )

    async def retrieve(
        self,
        response_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResponseObject:
        """
        Retrieve an OpenAI response by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not response_id:
            raise ValueError(f"Expected a non-empty value for `response_id` but received {response_id!r}")
        return await self._get(
            f"/v1/openai/v1/responses/{response_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResponseObject,
        )

    async def list(
        self,
        *,
        after: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        model: str | NotGiven = NOT_GIVEN,
        order: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResponseListResponse:
        """
        List all OpenAI responses.

        Args:
          after: The ID of the last response to return.

          limit: The number of responses to return.

          model: The model to filter responses by.

          order: The order to sort responses by when sorted by created_at ('asc' or 'desc').

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/openai/v1/responses",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "limit": limit,
                        "model": model,
                        "order": order,
                    },
                    response_list_params.ResponseListParams,
                ),
            ),
            cast_to=ResponseListResponse,
        )


class ResponsesResourceWithRawResponse:
    def __init__(self, responses: ResponsesResource) -> None:
        self._responses = responses

        self.create = to_raw_response_wrapper(
            responses.create,
        )
        self.retrieve = to_raw_response_wrapper(
            responses.retrieve,
        )
        self.list = to_raw_response_wrapper(
            responses.list,
        )

    @cached_property
    def input_items(self) -> InputItemsResourceWithRawResponse:
        return InputItemsResourceWithRawResponse(self._responses.input_items)


class AsyncResponsesResourceWithRawResponse:
    def __init__(self, responses: AsyncResponsesResource) -> None:
        self._responses = responses

        self.create = async_to_raw_response_wrapper(
            responses.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            responses.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            responses.list,
        )

    @cached_property
    def input_items(self) -> AsyncInputItemsResourceWithRawResponse:
        return AsyncInputItemsResourceWithRawResponse(self._responses.input_items)


class ResponsesResourceWithStreamingResponse:
    def __init__(self, responses: ResponsesResource) -> None:
        self._responses = responses

        self.create = to_streamed_response_wrapper(
            responses.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            responses.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            responses.list,
        )

    @cached_property
    def input_items(self) -> InputItemsResourceWithStreamingResponse:
        return InputItemsResourceWithStreamingResponse(self._responses.input_items)


class AsyncResponsesResourceWithStreamingResponse:
    def __init__(self, responses: AsyncResponsesResource) -> None:
        self._responses = responses

        self.create = async_to_streamed_response_wrapper(
            responses.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            responses.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            responses.list,
        )

    @cached_property
    def input_items(self) -> AsyncInputItemsResourceWithStreamingResponse:
        return AsyncInputItemsResourceWithStreamingResponse(self._responses.input_items)
