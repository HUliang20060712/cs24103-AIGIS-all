# 桌面端与推荐侧接口契约（D ↔ B）

- 类别枚举统一为 6 类：水体、植被、建筑、道路、农田、裸地。
- 桌面端输出 GeoJSON，`properties.category` 使用上述中文枚举，`properties.confidence` 为 0–1 浮点。
- 推荐侧按 `itemId` 关联 `item_meta`，新增类别须同时改两侧枚举并走 CR。

示例：

```json
{"type":"Feature","geometry":{"type":"Polygon","coordinates":[[[118.1,32.2],[118.2,32.2],[118.2,32.3],[118.1,32.2]]]},
 "properties":{"itemId":2001,"category":"水体","confidence":0.87}}
```
