"""
 Copyright (C) 2018-2021 Intel Corporation

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
"""

from mo.front.extractor import FrontExtractorOp
from mo.front.tf.extractors.utils import tf_dtype_extractor, tf_tensor_shape, tf_tensor_content
from mo.ops.const import Const


class ConstExtractor(FrontExtractorOp):
    op = 'Const'
    enabled = True

    @classmethod
    def extract(cls, node):
        pb_tensor = node.pb.attr["value"].tensor
        shape = tf_tensor_shape(pb_tensor.tensor_shape)
        attrs = {
            'shape': shape,
            'value': tf_tensor_content(pb_tensor.dtype, shape, pb_tensor),
            'data_type': tf_dtype_extractor(pb_tensor.dtype),
        }
        Const.update_node_stat(node, attrs)
        return cls.enabled
