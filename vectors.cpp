/*  Nick Sweeting 2013/10/08
    Student List (OOP)
    MIT Lisence
    g++ Vectors.cpp -o main && ./main
    Example of using vectors to store a list of students and their GPAs.
    It is referred from: https://github.com/pirate/Cpp-Data-Structures/
    
    Abhishek Sharma 2022/09/22
*/

#include <stdlib.h>
#include <iostream>
#include <vector>
#include <cmath>
#include <iomanip>
using namespace std;

struct Student {
    string firstName;
    string lastName;
    int studentID;
    double GPA;
};

// function to convert float to string with defined precision
string fltostr(double num){
    ostringstream strobj;
    strobj << fixed;
    strobj << setprecision(2);
    strobj << num ;
    string s = strobj.str();
    return s;

};


void printStudents(vector<Student> students) {

    int width = 14;
    string head_fn = "First Name";
    string head_ln = "Last Name";
    string head_id = "Student ID";
    string head_gpa = "Student GPA";
    int h_w1 = width - head_fn.length();
    int h_w2 = width - head_ln.length();
    int h_w3 = width - head_id.length(); 
    int h_w4 = width - head_gpa.length();

    cout << endl; 
    cout << " | " << head_fn <<setw(h_w1)<< " | " << head_ln <<setw(h_w2)<< " | " << head_id <<setw(h_w3)<< " | " << head_gpa <<setw(h_w4)<<" | " << endl; 

    for (int i=0; i<students.size(); i++)
    {
        string fnstr = students[i].firstName;
        string lnstr = students[i].lastName;
        string idstr =  to_string(students[i].studentID);
        string gpastr = fltostr(students[i].GPA);
        int w1 = width - fnstr.length();
        int w2 = width - lnstr.length();
        int w3 = width - idstr.length();
        int w4 = width - gpastr.length();

        cout << " | " << fnstr << setw(w1)<< " | " << lnstr << setw(w2)<< " | " << idstr << setw(w3) <<" | " << gpastr <<setw(w4) << " | " << endl;
    }
};

vector<Student> addStudent(vector<Student> students) {

    Student newStudent;

    cout << "First Name: ";
    cin >> newStudent.firstName;
    cout << "Last Name: ";
    cin >> newStudent.lastName;
    cout << "ID: ";
    cin >> newStudent.studentID;
    cout << "GPA: ";
    cin >> newStudent.GPA;

    students.push_back({newStudent.firstName, newStudent.lastName, newStudent.studentID, newStudent.GPA});

    return students;
}

vector<Student> delStudent(vector<Student> students) {
    int studentIDtoDel;
    cout << "ID of student to delete: ";
    cin >> studentIDtoDel;

    cout << "ID to delete: " << studentIDtoDel << endl;


    for(int i = 0; i<students.size(); i++){
        if(students[i].studentID == studentIDtoDel){
            students.erase(students.begin()+i);
        }
    }

    return students;
}

int main() {
    vector<Student> students;
    string input;

    while (true) {
        cout<<"Input operation: ";
        cin >> input;

        if (input == "ADD" || input == "a" || input == "add") {
            students = addStudent(students);
        }
        else if (input == "PRINT" || input == "p" || input == "print") {
            printStudents(students);
        }
        else if (input == "DELETE" || input == "d" || input == "delete") {
            students = delStudent(students);
        }
        else if (input == "QUIT" || input == "q" || input == "quit") {
            return 0;
        }
    }
}

