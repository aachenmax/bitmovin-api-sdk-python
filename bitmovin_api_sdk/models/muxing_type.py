# coding: utf-8

from enum import Enum
from six import string_types
from bitmovin_api_sdk.common.poscheck import poscheck_model


class MuxingType(Enum):
    FMP4 = "FMP4"
    CMAF = "CMAF"
    MP4 = "MP4"
    TS = "TS"
    WEBM = "WEBM"
    MP3 = "MP3"
    PROGRESSIVE_WEBM = "PROGRESSIVE_WEBM"
    PROGRESSIVE_MOV = "PROGRESSIVE_MOV"
    PROGRESSIVE_TS = "PROGRESSIVE_TS"
    BROADCAST_TS = "BROADCAST_TS"
    CHUNKED_TEXT = "CHUNKED_TEXT"
    TEXT = "TEXT"