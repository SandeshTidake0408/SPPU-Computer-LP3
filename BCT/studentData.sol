// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract StudentDatabase {
    
    // Structure to store student data
    struct Student {
        uint256 id;
        string name;
        uint8 age;
    }

    // Array to store the list of students
    Student[] public students;
    
    // Mapping to check if a student ID is already used
    mapping(uint256 => bool) private studentExists;

    // Event to emit when a new student is added
    event StudentAdded(uint256 id, string name, uint8 age);

    // Function to add a new student
    function addStudent(uint256 _id, string memory _name, uint8 _age) public {
        require(!studentExists[_id], "Student ID already exists");
        require(_age > 0, "Age must be greater than zero");

        students.push(Student(_id, _name, _age));
        studentExists[_id] = true;

        emit StudentAdded(_id, _name, _age);
    }

    // Function to get the list of all students
    function getStudents() public view returns (Student[] memory) {
        return students;
    }

    receive() external payable {
    }

    fallback() external payable {
    }

    function getContractBalance() public view returns (uint256) {
        return address(this).balance;
    }
}