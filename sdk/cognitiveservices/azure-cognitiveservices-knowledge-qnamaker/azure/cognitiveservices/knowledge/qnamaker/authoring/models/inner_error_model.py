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

from msrest.serialization import Model


class InnerErrorModel(Model):
    """An object containing more specific information about the error. As per
    Microsoft One API guidelines -
    https://github.com/Microsoft/api-guidelines/blob/vNext/Guidelines.md#7102-error-condition-responses.

    :param code: A more specific error code than was provided by the
     containing error.
    :type code: str
    :param inner_error: An object containing more specific information than
     the current object about the error.
    :type inner_error:
     ~azure.cognitiveservices.knowledge.qnamaker.authoring.models.InnerErrorModel
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'inner_error': {'key': 'innerError', 'type': 'InnerErrorModel'},
    }

    def __init__(self, **kwargs):
        super(InnerErrorModel, self).__init__(**kwargs)
        self.code = kwargs.get('code', None)
        self.inner_error = kwargs.get('inner_error', None)