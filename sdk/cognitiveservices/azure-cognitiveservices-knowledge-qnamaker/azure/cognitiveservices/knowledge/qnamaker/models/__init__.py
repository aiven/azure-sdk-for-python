# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

try:
    from .update_kb_operation_dto_add_py3 import UpdateKbOperationDTOAdd
    from .update_kb_operation_dto_delete_py3 import UpdateKbOperationDTODelete
    from .update_kb_operation_dto_update_py3 import UpdateKbOperationDTOUpdate
    from .update_kb_operation_dto_py3 import UpdateKbOperationDTO
    from .update_qna_dto_questions_py3 import UpdateQnaDTOQuestions
    from .update_qna_dto_metadata_py3 import UpdateQnaDTOMetadata
    from .update_qna_dto_context_py3 import UpdateQnaDTOContext
    from .update_qna_dto_py3 import UpdateQnaDTO
    from .update_kb_contents_dto_py3 import UpdateKbContentsDTO
    from .update_questions_dto_py3 import UpdateQuestionsDTO
    from .metadata_dto_py3 import MetadataDTO
    from .update_metadata_dto_py3 import UpdateMetadataDTO
    from .prompt_dto_qna_py3 import PromptDTOQna
    from .prompt_dto_py3 import PromptDTO
    from .update_context_dto_py3 import UpdateContextDTO
    from .delete_kb_contents_dto_py3 import DeleteKbContentsDTO
    from .qn_adto_context_py3 import QnADTOContext
    from .qn_adto_py3 import QnADTO
    from .file_dto_py3 import FileDTO
    from .create_kb_input_dto_py3 import CreateKbInputDTO
    from .qn_adocuments_dto_py3 import QnADocumentsDTO
    from .create_kb_dto_py3 import CreateKbDTO
    from .replace_kb_dto_py3 import ReplaceKbDTO
    from .context_dto_py3 import ContextDTO
    from .error_response_error_py3 import ErrorResponseError
    from .error_response_py3 import ErrorResponse, ErrorResponseException
    from .inner_error_model_py3 import InnerErrorModel
    from .error_py3 import Error
    from .operation_py3 import Operation
    from .knowledgebase_dto_py3 import KnowledgebaseDTO
    from .knowledgebases_dto_py3 import KnowledgebasesDTO
    from .endpoint_settings_dto_active_learning_py3 import EndpointSettingsDTOActiveLearning
    from .endpoint_settings_dto_py3 import EndpointSettingsDTO
    from .active_learning_settings_dto_py3 import ActiveLearningSettingsDTO
    from .alterations_dto_py3 import AlterationsDTO
    from .word_alterations_dto_py3 import WordAlterationsDTO
    from .endpoint_keys_dto_py3 import EndpointKeysDTO
    from .query_dto_context_py3 import QueryDTOContext
    from .query_dto_answer_span_request_py3 import QueryDTOAnswerSpanRequest
    from .query_dto_py3 import QueryDTO
    from .query_context_dto_py3 import QueryContextDTO
    from .qn_asearch_result_context_py3 import QnASearchResultContext
    from .qn_asearch_result_answer_span_py3 import QnASearchResultAnswerSpan
    from .qn_asearch_result_py3 import QnASearchResult
    from .qn_asearch_result_list_py3 import QnASearchResultList
    from .feedback_record_dto_py3 import FeedbackRecordDTO
    from .feedback_records_dto_py3 import FeedbackRecordsDTO
    from .answer_span_request_dto_py3 import AnswerSpanRequestDTO
    from .answer_span_response_dto_py3 import AnswerSpanResponseDTO
except (SyntaxError, ImportError):
    from .update_kb_operation_dto_add import UpdateKbOperationDTOAdd
    from .update_kb_operation_dto_delete import UpdateKbOperationDTODelete
    from .update_kb_operation_dto_update import UpdateKbOperationDTOUpdate
    from .update_kb_operation_dto import UpdateKbOperationDTO
    from .update_qna_dto_questions import UpdateQnaDTOQuestions
    from .update_qna_dto_metadata import UpdateQnaDTOMetadata
    from .update_qna_dto_context import UpdateQnaDTOContext
    from .update_qna_dto import UpdateQnaDTO
    from .update_kb_contents_dto import UpdateKbContentsDTO
    from .update_questions_dto import UpdateQuestionsDTO
    from .metadata_dto import MetadataDTO
    from .update_metadata_dto import UpdateMetadataDTO
    from .prompt_dto_qna import PromptDTOQna
    from .prompt_dto import PromptDTO
    from .update_context_dto import UpdateContextDTO
    from .delete_kb_contents_dto import DeleteKbContentsDTO
    from .qn_adto_context import QnADTOContext
    from .qn_adto import QnADTO
    from .file_dto import FileDTO
    from .create_kb_input_dto import CreateKbInputDTO
    from .qn_adocuments_dto import QnADocumentsDTO
    from .create_kb_dto import CreateKbDTO
    from .replace_kb_dto import ReplaceKbDTO
    from .context_dto import ContextDTO
    from .error_response_error import ErrorResponseError
    from .error_response import ErrorResponse, ErrorResponseException
    from .inner_error_model import InnerErrorModel
    from .error import Error
    from .operation import Operation
    from .knowledgebase_dto import KnowledgebaseDTO
    from .knowledgebases_dto import KnowledgebasesDTO
    from .endpoint_settings_dto_active_learning import EndpointSettingsDTOActiveLearning
    from .endpoint_settings_dto import EndpointSettingsDTO
    from .active_learning_settings_dto import ActiveLearningSettingsDTO
    from .alterations_dto import AlterationsDTO
    from .word_alterations_dto import WordAlterationsDTO
    from .endpoint_keys_dto import EndpointKeysDTO
    from .query_dto_context import QueryDTOContext
    from .query_dto_answer_span_request import QueryDTOAnswerSpanRequest
    from .query_dto import QueryDTO
    from .query_context_dto import QueryContextDTO
    from .qn_asearch_result_context import QnASearchResultContext
    from .qn_asearch_result_answer_span import QnASearchResultAnswerSpan
    from .qn_asearch_result import QnASearchResult
    from .qn_asearch_result_list import QnASearchResultList
    from .feedback_record_dto import FeedbackRecordDTO
    from .feedback_records_dto import FeedbackRecordsDTO
    from .answer_span_request_dto import AnswerSpanRequestDTO
    from .answer_span_response_dto import AnswerSpanResponseDTO
from .qn_amaker_client_enums import (
    ErrorCodeType,
    OperationStateType,
    StrictFiltersCompoundOperationType,
    EnvironmentType,
)

__all__ = [
    'UpdateKbOperationDTOAdd',
    'UpdateKbOperationDTODelete',
    'UpdateKbOperationDTOUpdate',
    'UpdateKbOperationDTO',
    'UpdateQnaDTOQuestions',
    'UpdateQnaDTOMetadata',
    'UpdateQnaDTOContext',
    'UpdateQnaDTO',
    'UpdateKbContentsDTO',
    'UpdateQuestionsDTO',
    'MetadataDTO',
    'UpdateMetadataDTO',
    'PromptDTOQna',
    'PromptDTO',
    'UpdateContextDTO',
    'DeleteKbContentsDTO',
    'QnADTOContext',
    'QnADTO',
    'FileDTO',
    'CreateKbInputDTO',
    'QnADocumentsDTO',
    'CreateKbDTO',
    'ReplaceKbDTO',
    'ContextDTO',
    'ErrorResponseError',
    'ErrorResponse', 'ErrorResponseException',
    'InnerErrorModel',
    'Error',
    'Operation',
    'KnowledgebaseDTO',
    'KnowledgebasesDTO',
    'EndpointSettingsDTOActiveLearning',
    'EndpointSettingsDTO',
    'ActiveLearningSettingsDTO',
    'AlterationsDTO',
    'WordAlterationsDTO',
    'EndpointKeysDTO',
    'QueryDTOContext',
    'QueryDTOAnswerSpanRequest',
    'QueryDTO',
    'QueryContextDTO',
    'QnASearchResultContext',
    'QnASearchResultAnswerSpan',
    'QnASearchResult',
    'QnASearchResultList',
    'FeedbackRecordDTO',
    'FeedbackRecordsDTO',
    'AnswerSpanRequestDTO',
    'AnswerSpanResponseDTO',
    'ErrorCodeType',
    'OperationStateType',
    'StrictFiltersCompoundOperationType',
    'EnvironmentType',
]
