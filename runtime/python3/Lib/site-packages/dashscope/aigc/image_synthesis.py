from typing import Any, List, Union

from dashscope.api_entities.dashscope_response import (DashScopeAPIResponse,
                                                       ImageSynthesisResponse)
from dashscope.client.base_api import BaseAsyncApi
from dashscope.common.constants import IMAGES, NEGATIVE_PROMPT, PROMPT
from dashscope.common.error import InputRequired
from dashscope.common.utils import _get_task_group_and_task


class ImageSynthesis(BaseAsyncApi):
    task = 'text2image'
    """API for image synthesis.
    """
    class Models:
        wanx_v1 = 'wanx-v1'

    @classmethod
    def call(cls,
             model: str,
             prompt: Any,
             negative_prompt: Any = None,
             images: List[str] = None,
             api_key: str = None,
             **kwargs) -> ImageSynthesisResponse:
        """Call image(s) synthesis service and get result.

        Args:
            model (str): The model, reference ``Models``.
            prompt (Any): The prompt for image(s) synthesis.
            negative_prompt (Any): The negative_prompt. Defaults to None.
            images (List[str]): The input list of images url.
            api_key (str, optional): The api api_key. Defaults to None.
            **kwargs:
                n(int, `optional`): Number of images to synthesis,
                    Currently fixed at 4.
                size(str, `optional`): The output image(s) size(width*height),
                    Currently fixed at 1024*1024. Default 1024*1024
                similarity(float, `optional`): The similarity between the
                    output image and the input image


        Raises:
            InputRequired: The prompt cannot be empty.

        Returns:
            ImageSynthesisResponse: The image(s) synthesis result.
        """
        return super().call(model,
                            prompt,
                            negative_prompt,
                            images,
                            api_key=api_key,
                            **kwargs)

    @classmethod
    def async_call(cls,
                   model: str,
                   prompt: Any,
                   negative_prompt: Any = None,
                   images: List[str] = None,
                   api_key: str = None,
                   **kwargs) -> ImageSynthesisResponse:
        """Create a image(s) synthesis task, and return task information.

        Args:
            model (str): The model, reference ``Models``.
            prompt (Any): The prompt for image(s) synthesis.
            negative_prompt (Any): The negative_prompt. Defaults to None.
            images (List[str]): The input list of images url.
            api_key (str, optional): The api api_key. Defaults to None.
            **kwargs(wanx-v1):
                n(int, `optional`): Number of images to synthesis.
                size: The output image(s) size, Default 1024*1024
                similarity(float, `optional`): The similarity between the
                    output image and the input image

        Raises:
            InputRequired: The prompt cannot be empty.

        Returns:
            DashScopeAPIResponse: The image synthesis
                task id in the response.
        """
        if prompt is None or not prompt:
            raise InputRequired('prompt is required!')
        task_group, function = _get_task_group_and_task(__name__)
        input = {PROMPT: prompt}
        if negative_prompt is not None:
            input[NEGATIVE_PROMPT] = negative_prompt
        if images is not None:
            input[IMAGES] = images
        response = super().async_call(model=model,
                                      task_group=task_group,
                                      task=ImageSynthesis.task,
                                      function=function,
                                      api_key=api_key,
                                      input=input,
                                      **kwargs)
        return ImageSynthesisResponse.from_api_response(response)

    @classmethod
    def fetch(cls,
              task: Union[str, ImageSynthesisResponse],
              api_key: str = None) -> ImageSynthesisResponse:
        """Fetch image(s) synthesis task status or result.

        Args:
            task (Union[str, ImageSynthesisResponse]): The task_id or
                ImageSynthesisResponse return by async_call().
            api_key (str, optional): The api api_key. Defaults to None.

        Returns:
            ImageSynthesisResponse: The task status or result.
        """
        response = super().fetch(task, api_key)
        return ImageSynthesisResponse.from_api_response(response)

    @classmethod
    def wait(cls,
             task: Union[str, ImageSynthesisResponse],
             api_key: str = None) -> ImageSynthesisResponse:
        """Wait for image(s) synthesis task to complete, and return the result.

        Args:
            task (Union[str, ImageSynthesisResponse]): The task_id or
                ImageSynthesisResponse return by async_call().
            api_key (str, optional): The api api_key. Defaults to None.

        Returns:
            ImageSynthesisResponse: The task result.
        """
        response = super().wait(task, api_key)
        return ImageSynthesisResponse.from_api_response(response)

    @classmethod
    def cancel(cls,
               task: Union[str, ImageSynthesisResponse],
               api_key: str = None) -> DashScopeAPIResponse:
        """Cancel image synthesis task.
        Only tasks whose status is PENDING can be canceled.

        Args:
            task (Union[str, ImageSynthesisResponse]): The task_id or
                ImageSynthesisResponse return by async_call().
            api_key (str, optional): The api api_key. Defaults to None.

        Returns:
            DashScopeAPIResponse: The response data.
        """
        return super().cancel(task, api_key)

    @classmethod
    def list(cls,
             start_time: str = None,
             end_time: str = None,
             model_name: str = None,
             api_key_id: str = None,
             region: str = None,
             status: str = None,
             page_no: int = 1,
             page_size: int = 10,
             api_key: str = None,
             **kwargs) -> DashScopeAPIResponse:
        """List async tasks.

        Args:
            start_time (str, optional): The tasks start time,
                for example: 20230420000000. Defaults to None.
            end_time (str, optional): The tasks end time,
                for example: 20230420000000. Defaults to None.
            model_name (str, optional): The tasks model name. Defaults to None.
            api_key_id (str, optional): The tasks api-key-id. Defaults to None.
            region (str, optional): The service region,
                for example: cn-beijing. Defaults to None.
            status (str, optional): The status of tasks[PENDING,
                RUNNING, SUCCEEDED, FAILED, CANCELED]. Defaults to None.
            page_no (int, optional): The page number. Defaults to 1.
            page_size (int, optional): The page size. Defaults to 10.
            api_key (str, optional): The user api-key. Defaults to None.

        Returns:
            DashScopeAPIResponse: The response data.
        """
        return super().list(start_time=start_time,
                            end_time=end_time,
                            model_name=model_name,
                            api_key_id=api_key_id,
                            region=region,
                            status=status,
                            page_no=page_no,
                            page_size=page_size,
                            api_key=api_key,
                            **kwargs)
