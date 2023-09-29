import logging
from logging import NullHandler

from dashscope.aigc.conversation import Conversation, History, HistoryItem
from dashscope.aigc.generation import Generation
from dashscope.aigc.image_synthesis import ImageSynthesis
from dashscope.aigc.multimodal_conversation import MultiModalConversation
from dashscope.aigc.code_generation import CodeGeneration
from dashscope.audio.asr.transcription import Transcription
from dashscope.audio.tts.speech_synthesizer import SpeechSynthesizer
from dashscope.common.api_key import save_api_key
from dashscope.common.env import (api_key, api_key_file_path,
                                  base_http_api_url, base_websocket_api_url)
from dashscope.deployment import Deployment
from dashscope.embeddings.batch_text_embedding import BatchTextEmbedding
from dashscope.embeddings.batch_text_embedding_response import \
    BatchTextEmbeddingResponse
from dashscope.embeddings.text_embedding import TextEmbedding
from dashscope.embeddings.multimodal_embedding import (MultiModalEmbedding,
                                                       MultiModalEmbeddingItemAudio,
                                                       MultiModalEmbeddingItemImage,
                                                       MultiModalEmbeddingItemText)
from dashscope.file import File
from dashscope.finetune import FineTune
from dashscope.model import Model
from dashscope.nlp.understanding import Understanding

__all__ = [
    base_http_api_url,
    base_websocket_api_url,
    api_key,
    api_key_file_path,
    save_api_key,
    Conversation,
    Generation,
    History,
    HistoryItem,
    ImageSynthesis,
    Transcription,
    File,
    Deployment,
    FineTune,
    Model,
    TextEmbedding,
    MultiModalEmbedding,
    MultiModalEmbeddingItemAudio,
    MultiModalEmbeddingItemImage,
    MultiModalEmbeddingItemText,
    SpeechSynthesizer,
    MultiModalConversation,
    BatchTextEmbedding,
    BatchTextEmbeddingResponse,
    Understanding,
    CodeGeneration
]

logging.getLogger(__name__).addHandler(NullHandler())
