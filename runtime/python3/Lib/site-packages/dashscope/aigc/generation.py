import copy
from typing import Any, Generator, List, Union

from dashscope.api_entities.dashscope_response import (GenerationResponse,
                                                       Message, Role)
from dashscope.client.base_api import BaseApi
from dashscope.common.constants import (CUSTOMIZED_MODEL_ID,
                                        DEPRECATED_MESSAGE, HISTORY, MESSAGES,
                                        PROMPT)
from dashscope.common.error import InputRequired, ModelRequired
from dashscope.common.logging import logger
from dashscope.common.utils import _get_task_group_and_task


class Generation(BaseApi):
    task = 'text-generation'
    """API for AI-Generated Content(AIGC) models.

    """
    class Models:
        """@deprecated, use qwen_turbo instead"""
        qwen_v1 = 'qwen-v1'
        """@deprecated, use qwen_plus instead"""
        qwen_plus_v1 = 'qwen-plus-v1'

        bailian_v1 = 'bailian-v1'
        dolly_12b_v2 = 'dolly-12b-v2'
        qwen_turbo = 'qwen-turbo'
        qwen_plus = 'qwen-plus'

    @classmethod
    def call(
        cls,
        model: str,
        prompt: Any = None,
        history: list = None,
        api_key: str = None,
        messages: List[Message] = None,
        **kwargs
    ) -> Union[GenerationResponse, Generator[GenerationResponse, None, None]]:
        """Call generation model service.

        Args:
            model (str): The requested model, such as gpt3-v2
            prompt (Any): The input prompt.
            history (list):The user provided history, deprecated
                examples:
                    [{'user':'The weather is fine today.',
                    'bot': 'Suitable for outings'}].
                Defaults to None.
            api_key (str, optional): The api api_key, can be None,
                if None, will get by default rule(TODO: api key doc).
            messages (list): The generation messages.
                examples:
                    [{'role': 'user',
                      'content': 'The weather is fine today.'},
                      {'role': 'assistant', 'content': 'Suitable for outings'}]
            **kwargs:
                stream(bool, `optional`): Enable server-sent events
                    (ref: https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events)  # noqa E501
                    the result will back partially[qwen-turbo,bailian-v1].
                temperature(float, `optional`): Used to control the degree
                    of randomness and diversity. Specifically, the temperature
                    value controls the degree to which the probability distribution
                    of each candidate word is smoothed when generating text. 
                    A higher temperature value will reduce the peak value of 
                    the probability, allowing more low-probability words to be 
                    selected, and the generated results will be more diverse; 
                    while a lower temperature value will enhance the peak value 
                    of the probability, making it easier for high-probability 
                    words to be selected, the generated results are more 
                    deterministic, range(0, 2) .[qwen-turbo,qwen-plus].
                top_p(float, `optional`): A sampling strategy, called nucleus
                    sampling, where the model considers the results of the
                    tokens with top_p probability mass. So 0.1 means only
                    the tokens comprising the top 10% probability mass are
                    considered[qwen-turbo,bailian-v1].
                enable_search(bool, `optional`): Whether to enable web search(quark).  # noqa E501
                    Currently works best only on the first round of conversation.
                    Default to False, support model: [qwen-turbo].
                customized_model_id(str, required) The enterprise-specific
                    large model id, which needs to be generated from the
                    operation background of the enterprise-specific
                    large model product, support model: [bailian-v1].
                result_format(str, `optional`): [message|text] Set result result format. # noqa E501
                    Default result is text

        Raises:
            InvalidInput: The history and auto_history are mutually exclusive.

        Returns:
            Union[GenerationResponse,
                  Generator[GenerationResponse, None, None]]: If
            stream is True, return Generator, otherwise GenerationResponse.
        """
        if (prompt is None or not prompt) and (messages is None
                                               or not messages):
            raise InputRequired('prompt or messages is required!')
        if model is None or not model:
            raise ModelRequired('Model is required!')
        task_group, function = _get_task_group_and_task(__name__)
        input, parameters = cls._build_input_parameters(
            model, prompt, history, messages, **kwargs)
        response = super().call(model=model,
                                task_group=task_group,
                                task=Generation.task,
                                function=function,
                                api_key=api_key,
                                input=input,
                                **parameters)
        is_stream = kwargs.get('stream', False)
        if is_stream:
            return (GenerationResponse.from_api_response(rsp)
                    for rsp in response)
        else:
            return GenerationResponse.from_api_response(response)

    @classmethod
    def _build_input_parameters(cls, model, prompt, history, messages,
                                **kwargs):
        if model == Generation.Models.qwen_v1:
            logger.warning("Model %s is deprecated, use %s instead!" % (
                Generation.Models.qwen_v1,
                Generation.Models.qwen_turbo
            ))
        if model == Generation.Models.qwen_plus_v1:
            logger.warning("Model %s is deprecated, use %s instead!" % (
                Generation.Models.qwen_plus_v1,
                Generation.Models.qwen_plus
            ))   
        parameters = {}
        input = {}
        if history is not None:
            logger.warning(DEPRECATED_MESSAGE)
            input[HISTORY] = history
            if prompt is not None and prompt:
                input[PROMPT] = prompt            
        elif messages is not None:
            msgs = copy.deepcopy(messages)
            if prompt is not None and prompt:
                msgs.append({'role': Role.USER, 'content': prompt})
            input = {MESSAGES: msgs}
        else:
            input[PROMPT] = prompt
                
        if model.startswith('qwen'):
            enable_search = kwargs.pop('enable_search', False)
            if enable_search:
                parameters['enable_search'] = enable_search
        elif model.startswith('bailian'):
            customized_model_id = kwargs.pop('customized_model_id', None)
            if customized_model_id is None:
                raise InputRequired('customized_model_id is required for %s' %
                                    model)
            input[CUSTOMIZED_MODEL_ID] = customized_model_id

        return input, {**parameters, **kwargs}
