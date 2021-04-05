#include<iostream>
#include<string>

#define MAX 1000

using std::cin;
using std::cout;
using std::endl;
using std::string;

struct Person{
    string m_name;
    int m_sex;
    int m_age;
    string m_phone;
    string m_addr;
};

struct AddressBook{
    struct Person personArray[MAX];
    int m_size;
};

void showMenu(){
    cout<<"--------------------------"<<endl;
    cout<<"------1.Add Contacts------"<<endl;
    cout<<"------2.Show Contacts-----"<<endl;
    cout<<"------3.Delete Contacts---"<<endl;
    cout<<"------4.Find Contacts-----"<<endl;
    cout<<"------5.Modify Contacts---"<<endl;
    cout<<"------6.Clear Contacts----"<<endl;
    cout<<"------0.Exit Contacts-----"<<endl;
    cout<<"--------------------------"<<endl;
}

void AddContacts(AddressBook *abs){
    if(abs->m_size==MAX){
        cout<<"Max person"<<endl;
        return;
    }
    else{
        //name
        string name;
        cout<<"type name plz"<<endl;
        cin>>name;
        abs->personArray[abs->m_size].m_name = name;
        //sex
        int sex;
        cout<<"type sex plz"<<endl;
        cout<<"1.male || 2.female"<<endl;
        while(true){
            cin>>sex;
            if(sex == 1 || sex == 2){
                abs->personArray[abs->m_size].m_sex = sex;
                break;
            }   
            cout<<"type wrong, retype plz"<<endl;
        }
        //age
        int age;
        cout<<"type age plz"<<endl;
        cin>>age;
        abs->personArray[abs->m_size].m_age = age;
        //phone number
        string phone;
        cout<<"type phone number plz"<<endl;
        cin>>phone;
        abs->personArray[abs->m_size].m_phone = phone;
        //address
        string address;
        cout<<"type address plz"<<endl;
        cin>>address;
        abs->personArray[abs->m_size].m_addr = address;
        // ++
        abs->m_size++;
        //instruction
        cout<<"finished loading person"<<endl;
        system("pause");
        system("cls");
    }
}
void ShowContacts(AddressBook *abs){
    int nums = abs->m_size;
    if(nums==0){
        cout<<"No contacts"<<endl;
    }
    else{
        for(int i=0;i<nums;i++){
        //cout<<"--------------------------"<<endl;
        cout<<"name: "<<abs->personArray[i].m_name<<"\t";
        cout<<"sex: "<<(abs->personArray[i].m_sex==1?"male":"female")<<"\t";
        cout<<"age: "<<abs->personArray[i].m_age<<"\t";
        cout<<"phone num: "<<abs->personArray[i].m_phone<<"\t";
        cout<<"address: "<<abs->personArray[i].m_addr<<endl;
        //cout<<"--------------------------"<<endl;
        }
    }
    
    //instruction
    cout<<"finished showing person"<<endl;
    system("pause");
    system("cls");
}
void DeleteContacts(AddressBook *abs){
    string name;
    cout<<"person u wanna delete:"<<endl;
    cin>>name;

    bool exit_flg = 0;

    for(int i=0;i<abs->m_size;i++){
        if(abs->personArray[i].m_name==name){
            exit_flg = 1;
            for(int j = i;j<abs->m_size-1;j++){
                abs->personArray[j] = abs->personArray[j+1];
            }
            abs->m_size--;
        }
    }
    
    if(exit_flg==0){
        cout<<"not exit"<<endl;
    }
    //instruction
    cout<<"finished deleting person"<<endl;
    system("pause");
    system("cls");
}
void FindContacts(AddressBook *abs){
    cout<<"person u wanna find:"<<endl;
    string name;
    cin>>name;
    int exit_flg = 0;
    for(int i=0;i<abs->m_size;i++){
        exit_flg = 1;
        if(abs->personArray[i].m_name == name){
        cout<<"name: "<<abs->personArray[i].m_name<<"\t";
        cout<<"sex: "<<(abs->personArray[i].m_sex==1?"male":"female")<<"\t";
        cout<<"age: "<<abs->personArray[i].m_age<<"\t";
        cout<<"phone num: "<<abs->personArray[i].m_phone<<"\t";
        cout<<"address: "<<abs->personArray[i].m_addr<<endl;
        }
    }
    if(exit_flg==0){
        cout<<"not exit"<<endl;
    }
    //instruction
    cout<<"finished finding person"<<endl;
    system("pause");
    system("cls");
}
void ModifyContacts(AddressBook *abs){
    cout<<"person u wanna modify:"<<endl;
    string name;
    cin>>name;
    int exit_flg = 0;
    for(int i=0;i<abs->m_size;i++){
        exit_flg = 1;
        if(abs->personArray[i].m_name == name){
            string name;
            cout<<"type name plz"<<endl;
            cin>>name;
            abs->personArray[abs->m_size].m_name = name;
            //sex
            int sex;
            cout<<"type sex plz"<<endl;
            cout<<"1.male || 2.female"<<endl;
            while(true){
                cin>>sex;
                if(sex == 1 || sex == 2){
                    abs->personArray[abs->m_size].m_sex = sex;
                    break;
                }   
                cout<<"type wrong, retype plz"<<endl;
            }
            //age
            int age;
            cout<<"type age plz"<<endl;
            cin>>age;
            abs->personArray[abs->m_size].m_age = age;
            //phone number
            string phone;
            cout<<"type phone number plz"<<endl;
            cin>>phone;
            abs->personArray[abs->m_size].m_phone = phone;
            //address
            string address;
            cout<<"type address plz"<<endl;
            cin>>address;
            abs->personArray[abs->m_size].m_addr = address;
        }
    }
    if(exit_flg==0){
        cout<<"not exit"<<endl;
    }
    //instruction
    cout<<"finished modifying person"<<endl;
    system("pause");
    system("cls");
}
void ClearContacts(AddressBook *abs){
    abs->m_size = 0;
    //instruction
    cout<<"finished clearing person"<<endl;
    system("pause");
    system("cls");
}
int ExitContacts(){
    cout<<"see u"<<endl;
    system("pause");
    return 0;
}

int main(){
    AddressBook abs;
    abs.m_size = 0;

    int select = 0;

    while(true){
        showMenu();
        cout<<"Plz choose ur operation"<<endl;

        cin>>select;

        switch (select){
        case 1:
            AddContacts(&abs);
            break;
        case 2:
            ShowContacts(&abs);
            break;
        case 3:
            DeleteContacts(&abs);
            break;
        case 4:
            FindContacts(&abs);
            break;
        case 5:
            ModifyContacts(&abs);
            break;
        case 6:
            ClearContacts(&abs);
            break;
        case 0:
            cout<<"see u"<<endl;
            system("pause");
            return false;
            break;
        default:
            cout<<"retype operation"<<endl;
            break;
        }
    }  
}