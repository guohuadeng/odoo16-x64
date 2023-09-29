import asyncio
import time
from typing import List, Union

import aiohttp

from dashscope.api_entities.dashscope_response import (DashScopeAPIResponse,
                                                       TranscriptionResponse)
from dashscope.client.base_api import BaseAsyncApi
from dashscope.common.constants import ApiProtocol, HTTPMethod
from dashscope.common.logging import logger
from dashscope.common.utils import _get_task_group_and_task


class Transcription(BaseAsyncApi):
    """API for File Transcription models.
    """

    MAX_QUERY_TRY_COUNT = 3

    class Models:
        paraformer_v1 = 'paraformer-v1'
        paraformer_8k_v1 = 'paraformer-8k-v1'
        paraformer_mtl_v1 = 'paraformer-mtl-v1'

    @classmethod
    def call(cls,
             model: str,
             file_urls: List[str],
             api_key: str = None,
             **kwargs) -> TranscriptionResponse:
        """Transcribe the given files synchronously.

        Args:
            model (str): The requested model_id.
            file_urls (List[str]): List of stored URLs.
            channel_id (List[int], optional): The selected channel_id of audio file. # noqa: E501

        Returns:
            TranscriptionResponse: The result of batch transcription.
        """
        response = super().call(model, file_urls, api_key=api_key, **kwargs)
        return TranscriptionResponse.from_api_response(response)

    @classmethod
    def async_call(cls,
                   model: str,
                   file_urls: List[str],
                   api_key: str = None,
                   **kwargs) -> TranscriptionResponse:
        """Transcribe the given files asynchronously,
        return the status of task submission for querying results subsequently.

        Args:
            model (str): The requested model, such as paraformer-16k-1
            file_urls (List[str]): List of stored URLs.
            channel_id (List[int], optional): The selected channel_id of audio file. # noqa: E501

        Returns:
            TranscriptionResponse: The response including task_id.
        """
        response = cls._launch_request(model,
                                       file_urls,
                                       api_key=api_key,
                                       **kwargs)
        return TranscriptionResponse.from_api_response(response)

    @classmethod
    def fetch(
        cls,
        task: Union[str, TranscriptionResponse],
        api_key: str = None,
    ) -> TranscriptionResponse:
        """Fetch the status of task, including results of batch transcription when task_status is SUCCEEDED.  # noqa: E501

        Args:
            task (Union[str, TranscriptionResponse]): The task_id or
                response including task_id returned from async_call().

        Returns:
            TranscriptionResponse: The status of task_id,
        including results of batch transcription when task_status is SUCCEEDED.
        """
        try_count: int = 0
        while True:
            try:
                response = super().fetch(task, api_key=api_key)
            except (asyncio.TimeoutError, aiohttp.ClientConnectorError) as e:
                logger.error(e)
                try_count += 1
                if try_count <= Transcription.MAX_QUERY_TRY_COUNT:
                    time.sleep(2)
                    continue

            try_count = 0
            break

        return TranscriptionResponse.from_api_response(response)

    @classmethod
    def wait(
        cls,
        task: Union[str, TranscriptionResponse],
        api_key: str = None,
    ) -> TranscriptionResponse:
        """Poll task until the final results of transcription is obtained.

        Args:
            task (Union[str, TranscriptionResponse]): The task_id or
                response including task_id returned from async_call().

        Returns:
            TranscriptionResponse: The result of batch transcription.
        """
        response = super().wait(task, api_key=api_key)
        return TranscriptionResponse.from_api_response(response)

    @classmethod
    def _launch_request(cls,
                        model: str,
                        files: List[str],
                        api_key: str = None,
                        **kwargs) -> DashScopeAPIResponse:
        """Submit transcribe request.

        Args:
            model (str): The requested model, such as paraformer-16k-1
            files (List[str]): List of stored URLs.

        Returns:
            DashScopeAPIResponse: The result of task submission.
        """
        task_name, function = _get_task_group_and_task(__name__)

        try_count: int = 0
        while True:
            try:
                response = super().async_call(model=model,
                                              task_group='audio',
                                              task=task_name,
                                              function=function,
                                              input={'file_urls': files},
                                              api_protocol=ApiProtocol.HTTP,
                                              http_method=HTTPMethod.POST,
                                              api_key=api_key,
                                              **kwargs)
            except (asyncio.TimeoutError, aiohttp.ClientConnectorError) as e:
                logger.error(e)
                try_count += 1
                if try_count <= Transcription.MAX_QUERY_TRY_COUNT:
                    time.sleep(2)
                    continue

            break

        return response
