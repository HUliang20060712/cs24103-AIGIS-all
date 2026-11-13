package cn.edu.chzu.aigis.vision.service;

import org.springframework.stereotype.Service;

import java.util.Map;
import java.util.UUID;
import java.util.concurrent.ConcurrentHashMap;

/** 识别任务登记（队列与推理待接，实验四补）。 */
@Service
public class TaskService {

    private final Map<String, String> tasks = new ConcurrentHashMap<>();

    public String submit(String filename) {
        String taskId = UUID.randomUUID().toString().substring(0, 8);
        tasks.put(taskId, "QUEUED:" + filename);
        return taskId;
    }

    public String status(String taskId) {
        return tasks.getOrDefault(taskId, "NOT_FOUND");
    }
}
