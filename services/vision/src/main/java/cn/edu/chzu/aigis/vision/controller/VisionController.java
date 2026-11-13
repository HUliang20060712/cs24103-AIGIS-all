package cn.edu.chzu.aigis.vision.controller;

import cn.edu.chzu.aigis.vision.service.TaskService;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.multipart.MultipartFile;

import java.util.Map;

@RestController
@RequestMapping("/api/vision")
public class VisionController {

    private final TaskService taskService;

    public VisionController(TaskService taskService) {
        this.taskService = taskService;
    }

    @PostMapping("/recognize")
    public Map<String, String> recognize(@RequestParam("file") MultipartFile file) {
        String taskId = taskService.submit(file.getOriginalFilename());
        return Map.of("taskId", taskId, "state", "QUEUED");
    }

    @GetMapping("/tasks/{taskId}")
    public Map<String, String> task(@PathVariable String taskId) {
        return Map.of("taskId", taskId, "state", taskService.status(taskId));
    }
}
