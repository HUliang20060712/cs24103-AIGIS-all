package cn.edu.chzu.aigis.reco.controller;

import cn.edu.chzu.aigis.reco.model.UserPreference;
import cn.edu.chzu.aigis.reco.service.PreferenceService;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@RequestMapping("/api/reco/preference")
public class PreferenceController {

    private final PreferenceService service;

    public PreferenceController(PreferenceService service) {
        this.service = service;
    }

    @GetMapping("/{userId}")
    public ResponseEntity<UserPreference> get(@PathVariable long userId) {
        return service.find(userId)
                .map(ResponseEntity::ok)
                .orElseGet(() -> ResponseEntity.notFound().build());
    }

    @PutMapping("/{userId}")
    public ResponseEntity<Void> put(@PathVariable long userId, @RequestBody PreferenceBody body) {
        service.save(userId, body.categories(), body.weight());
        return ResponseEntity.ok().build();
    }

    @DeleteMapping("/{userId}")
    public ResponseEntity<Void> delete(@PathVariable long userId) {
        service.clear(userId);
        return ResponseEntity.noContent().build();
    }

    public record PreferenceBody(List<String> categories, double weight) {
    }
}
