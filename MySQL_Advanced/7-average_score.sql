-- Write a SQL script that creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student

DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser
(
  IN user_id INT
)
BEGIN
  -- Declare a variable to store the average score
  DECLARE avg_score FLOAT;

  -- Compute the average score
  SELECT AVG(score) INTO avg_score
  FROM corrections
  WHERE corrections.user_id = user_id;

  -- Insert or update the average score in the users table
  UPDATE users
  SET average_score = avg_score
  WHERE id = user_id;

END;

//

DELIMITER ;
