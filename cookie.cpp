#include<iostream>
#include<math.h>
using namespace std;

class students
{
    public:
    int rollno;
    string name;
    float marks;
    
    void getdata()
    {
        cout<<"Enter roll number: ";
        cin>>rollno;
        cout<<"Enter name: ";
        cin>>name;
        cout<<"Enter marks: ";
        cin>>marks;
    }
    
    void displaydata()
    {
        cout<<"Roll number: "<<rollno<<endl;
        cout<<"Name: "<<name<<endl;
        cout<<"Marks: "<<marks<<endl;
    }
};

void main(){
    students s;
    s.getdata();
    s.displaydata();
}