from os import path

import predict_actions_price

base_path = path.dirname(path.dirname(predict_actions_price.__file__))
workspace_path = path.join(base_path, 'workspace')
data_path = path.join(workspace_path, 'data')
models_path = path.join(workspace_path, 'models')
