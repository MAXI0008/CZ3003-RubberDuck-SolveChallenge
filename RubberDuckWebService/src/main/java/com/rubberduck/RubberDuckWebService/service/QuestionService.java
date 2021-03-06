package com.rubberduck.RubberDuckWebService.service;

import com.rubberduck.RubberDuckWebService.model.DifficultyEnum;
import com.rubberduck.RubberDuckWebService.model.Question;

import java.util.List;

public interface QuestionService {

    List<Question> findAll();

    Question findById(Long id);

    List<Question> findByLevel(String level);

    List<Question> findByWorld(String world);

    List<Question> findBySectionAndWorld(String section, String world);

    List<Question> findByLevelAndSectionAndWorld(String level, String section, String world);

    List<Question> findByCharacter(String character);

    List<Question> findByLevelAndSectionAndWorldAndCharacter(String level, String section, String world, String character);

    List<Question> findByCharacterAndWorldAndDifficulty(String character, String world, DifficultyEnum difficultyEnum);

    Question save(Question question);

    void delete(Question question);
}
