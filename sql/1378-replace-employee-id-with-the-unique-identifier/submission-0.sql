-- LeetCode 1378: Replace Employee ID With The Unique Identifier
-- https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/

SELECT d.unique_id, e.name
FROM Employees e
LEFT JOIN EmployeeUNI d
    ON e.id = d.id;
