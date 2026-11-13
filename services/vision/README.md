# C-图像识别（vision-service）

负责人：黄德淳 2024210549　状态：骨架

- `POST /api/vision/recognize`：上传图片，返回 `taskId`，状态 `QUEUED`。
- `GET /api/vision/tasks/{taskId}`：查询任务状态。
- 待补：异步队列消费、6 类地物分类模型、批量任务、结果落库。
