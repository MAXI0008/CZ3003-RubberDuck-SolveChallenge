package com.rubberduck.RubberDuckWebService.repo;

import com.rubberduck.RubberDuckWebService.model.Question;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface QuestionRepo extends JpaRepository<Question, Integer> {

    Question findById(Long id);

    List<Question> findByLevel(String level);

    List<Question> findByWorld(String world);

    List<Question> findBySectionAndWorld(String section, String world);

    List<Question> findByLevelAndSectionAndWorld(String level, String section, String world);

    Question save(Question question);

    void delete(Question question);
}
