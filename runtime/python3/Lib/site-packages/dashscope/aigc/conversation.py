from copy import deepcopy
from http import HTTPStatus
from typing import Any, Generator, List, Union

from dashscope.api_entities.dashscope_response import (ConversationResponse,
                                                       Message, Role)
from dashscope.client.base_api import BaseApi
from dashscope.common.constants import (DEPRECATED_MESSAGE, HISTORY, MESSAGES,
                                        PROMPT)
from dashscope.common.error import InputRequired, InvalidInput, ModelRequired
from dashscope.common.logging import logger
from dashscope.common.utils import _get_task_group_and_task


class HistoryItem(dict):
    """A conversation history item.

    """
    def __init__(self, role: str, text: str = None, **kwargs):
        """Init a history item.

        Args:
            role (str): The role name.
            text (str): The text history. Default ot None.
            kwargs: The key/value pair of history content.

        Raises:
            InvalidInput: The key and value must pair.
        """
        logger.warning(DEPRECATED_MESSAGE)
        self.role = role
        dict.__init__(self, {role: []})
        if text is not None:
            self[self.role].append({'text': text})
        for k, v in kwargs.items():
            self[self.role].append({k: v})

    def add(self, key: str, content: Any):
        """Add a key/value to history.

        Args:
            key (str): The key of the content.
            value (Any): The history content.
        """
        self[self.role].append({key: content})


class History(list):
    """Manage the conversation history.

    """
    def __init__(self, items: List[HistoryItem] = None):
        """Init a history with list of HistoryItems.

        Args:
            items (List[HistoryItem], optional): The history items.
                Defaults to None.
        """
        if items is not None:
            logger.warning(DEPRECATED_MESSAGE)
            list.__init__(items)
        else:
            list.__init__([])


def _history_to_qwen_format(history: History, n_history: int):
    """Convert history to simple format.
       [{"user":"您好", "bot":"我是你的助手，很高兴为您服务"},
        {"user":"user input", "bot":"bot output"}]
    """
    simple_history = []
    user = None
    bot = None

    if n_history != -1 and len(history) >= 2 * n_history:
        history = history[len(history) - 2 * n_history:]

    for item in history:
        if 'user' in item:
            user = item['user'][0]['text']
        if 'bot' in item:
            bot = item['bot'][0]['text']
        if user is not None and bot is not None:
            simple_history.append({'user': user, 'bot': bot})
            user = None
            bot = None
    return simple_history


class Conversation(BaseApi):
    """Conversational robot interface.
    """
    task = 'generation'

    class Models:
        """@deprecated, use qwen_turbo instead"""
        qwen_v1 = 'qwen-v1'
        """@deprecated, use qwen_plus instead"""
        qwen_plus_v1 = 'qwen-plus-v1'

        qwen_turbo = 'qwen-turbo'
        qwen_plus = 'qwen-plus'

    def __init__(self,
                 history: History = None) -> None:
        """Init a chat.

        Args:
            history (dict): The conversation initialization settings.
               will be recorded in the system history list.
                Defaults to None.
        """
        super().__init__()
        if history is None:
            self.history = History()
        else:
            logger.warning(DEPRECATED_MESSAGE)
            self.history = history

    def call(
        self,
        model: str,
        prompt: Any = None,
        history: History = None,
        auto_history: bool = False,
        n_history: int = -1,
        api_key: str = None,
        messages: List[Message] = None,
        **kwargs
    ) -> Union[ConversationResponse, Generator[ConversationResponse, None,
                                               None]]:
        """Call conversational robot generator a response.

        Args:
            model (str): The request model.
            prompt (Any): The input prompt.
            history(History): The user provided history.
                Only works for this call, will not be recorded in the
                system history list. The ``history`` and ``auto_history``
                are mutually exclusive. Default to None.
            auto_history (bool): Call with the automatically maintenance
                conversation history list. The ``history`` and ``auto_history``
                are mutually exclusive.
            n_history (int): Number of latest history in conversation,
                -1 all history. Default to -1
            api_key (str, optional): The api api_key, if not present,
                will get by default rule(TODO: api key doc). Defaults to None.
            messages (list): The generation messages.
                examples:
                    [{'role': 'user',
                      'content': 'The weather is fine today.'},
                      {'role': 'assistant', 'content': 'Suitable for outings'}]
            **kwargs(qwen-turbo, qwen-plus):
                stream(bool, `optional`): Enable server-sent events
                    (ref: https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events)  # noqa E501
                    the result will back partially.
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
                    deterministic,range(0, 2) .[qwen-turbo,qwen-plus].
                top_p(float, `optional`): A sampling strategy, called nucleus
                    sampling, where the model considers the results of the
                    tokens with top_p probability mass. So 0.1 means only
                    the tokens comprising the top 10% probability mass are
                    considered.
                enable_search(bool, `optional`): Whether to enable web search(quark).  # noqa E501
                    Currently works best only on the first round of conversation.
                    Default to False.
                result_format(str, `optional`): [message|text] Set result result format. # noqa E501
                    Default result is text

        Raises:
            InputRequired: The prompt cannot be empty.
            InvalidInput: The history and auto_history are mutually exclusive.

        Returns:
            Union[ConversationResponse,
                  Generator[ConversationResponse, None, None]]: If
            stream is True, return Generator, otherwise ConversationResponse.

        """
        if ((prompt is None or not prompt)
                and ((messages is None or not messages))):
            raise InputRequired('prompt or messages is required!')
        if model is None or not model:
            raise ModelRequired('Model is required!')
        task_group, _ = _get_task_group_and_task(__name__)
        input, parameters = self._build_input_parameters(
            model, prompt, history, auto_history, n_history, messages,
            **kwargs)
        response = super().call(model=model,
                                task_group=task_group,
                                task='text-generation',
                                function='generation',
                                api_key=api_key,
                                input=input,
                                **parameters)
        is_stream = kwargs.get('stream', False)
        return self._handle_response(prompt, response, is_stream)

    def _handle_stream_response(self, prompt, responses):
        for rsp in responses:
            rsp = ConversationResponse.from_api_response(rsp)
            yield rsp
        if rsp.status_code == HTTPStatus.OK and rsp.output.choices is None:
            user_item = HistoryItem('user', text=prompt)
            bot_history_item = HistoryItem('bot', text=rsp.output.text)
            self.history.append(user_item)
            self.history.append(bot_history_item)

    def _handle_response(self, prompt, response, is_stream):
        if is_stream:
            return (rsp
                    for rsp in self._handle_stream_response(prompt, response))
        else:
            response = ConversationResponse.from_api_response(response)
            if (response.status_code == HTTPStatus.OK
                    and response.output.choices is None):
                user_item = HistoryItem('user', text=prompt)
                bot_history_item = HistoryItem('bot',
                                               text=response.output['text'])
                self.history.append(user_item)
                self.history.append(bot_history_item)
            return response

    def _build_input_parameters(self, model, prompt, history, auto_history,
                                n_history, messages, **kwargs):
        if model == Conversation.Models.qwen_v1:
            logger.warning("Model %s is deprecated, use %s instead!" % (
                Conversation.Models.qwen_v1,
                Conversation.Models.qwen_turbo
            ))
        if model == Conversation.Models.qwen_plus_v1:
            logger.warning("Model %s is deprecated, use %s instead!" % (
                Conversation.Models.qwen_plus_v1,
                Conversation.Models.qwen_plus
            ))            
        parameters = {}
        if history is not None and auto_history:
            raise InvalidInput('auto_history is True, history must None')
        if history is not None:  # use user provided history or system.
            logger.warning(DEPRECATED_MESSAGE)
            input = {
                PROMPT:
                prompt,
                HISTORY:
                _history_to_qwen_format(history, n_history) if history else [],
            }
        elif auto_history:
            logger.warning(DEPRECATED_MESSAGE)
            input = {
                PROMPT: prompt,
                HISTORY: _history_to_qwen_format(self.history, n_history)
            }
        elif messages:
            msgs = deepcopy(messages)
            if prompt is not None and prompt:
                msgs.append({'role': Role.USER, 'content': prompt})
            input = {'messages': msgs}
        else:
            input = {
                PROMPT: prompt,
            }
        # parameters
        if model.startswith('qwen'):
            enable_search = kwargs.pop('enable_search', False)
            if enable_search:
                parameters['enable_search'] = enable_search

        return input, {**parameters, **kwargs}
