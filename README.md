# DVD-Store-Automation
Problem2: DVD Store Automation
In this experiment you are expected to develop a simple console based DVD Store Automation.
Your application should support the following features:
Load: When your program starts, it should look for a le of which name was taken as a
command line argument. If it is found, all records should be read in according to the format
explained below. If it cannot be found, your program should initialize an empty inventory.
In either case, you will fall into a loop waiting for console commands.
Save data: This operation should be carried out automatically just before your program
terminates. All data in your inventory should be saved to the sample (If you run your
program several times, each run should input the previous output, without an error.)

User commands:
A - Adding a new entry (Add a new dvd to your inventory)
First get the serial number from the user. If this number is already in use, give a warning
and repeat this process. Then get the rest of the data from the user. The state of a new dvd
is Inv (in inventory)
Input Definition: A,{serial},{price},{Name},{Genre},{Director},{State}
input: A,123,25,"Terminator","Action","James Cameron","Inv"
R - Removing an entry
To remove an item, first carry out the searching by serial in order to see the details of searched
dvd. First, user will enter the serial of the dvd and then attributes of the entry will be printed.
After that, program asks user to confirm the deletion. If the items state is hired, you cannot
remove the item and you must display a warning message.
Input Definition: R,{serial}
input: R,123
S - Searching for an entry by name
A search can be conducted either by the name data (multiple items may be listed). If an
entry is found, you have to output all the details (name, director, serial etc) . Your code
must get the entries in partial search(min. 3 character). (For Ex: If the entry is Ter , your
program will get Terminator)
Input Definition: S,{Name}
input: S,"Ter"
input: S,"Terminator"
L List
List all the items in the inventory. List each item on one line (print a header row at the top).
Print items in groups of 4. If there are more items, wait until the space key is hit before
proceeding to the next batch of items. List will be ordered by name.
Input Definition: L
input: L
E - Edit entry
Change the values of a record. You have to write on a single line. It is enough to write which
attribute you want to edit.
Input Definition: E,{Serial},Attribute1=NewValue1,Attribute2=NewValue2,...
input: E,123,{Name="IronMan"},{Price=50}
2
Fall 2017
BBM 103: Introduction to Programming Laboratory I
R- Hire DVD
Change the state of the dvd. First ask user for the serial of the dvd and print its attributes
then change its state as Hired. A hired dvd cannot be removed.
Input Definition: H,{Serial}
input: H,123
Q- Quit
Save all data into le and end program.
Input Definition: Q
input: Q
User will choose an operation from a menu.
A sample menu shown below:
Note: User can enter A, R, S, L, E, H or Q. If user enters any other character,
your application must display an error message.
Some details:
The inventory will be lled using data in the le of which format is given below.
Note that text elds in the le may include whitespace (space or tab) characters. It may
be wise to scan all lines for consecutive whitespace characters before loading data into your
inventory. Just remove extra whitespaces, leaving only one space character. There can be
empty lines in the input le.
Input le format (each input line consists of the following elds):
Serial (This is a unique integer. An item can have just one serial and a serial can be used
for only one item.).
Price (Price of the dvd, may have leading blanks)
Name (Name can include whitespace and punctuation characters)
Genre (Type can include whitespace characters) Genre of a movie can be "Action", "Fan-
tastic", "Love", "History" and "Horror".
Director (Director eld can include whitespace character)
3
Fall 2017
BBM 103: Introduction to Programming Laboratory I
State: It can be "Hired" or "Inv".
You must check and give appropriate warning messages (item couldnt be found, serial
number already exists, etc.) whenever necessary.

Sample Dvd information
serial: 123
price: 25
director: Terminator
genre: Action
name: James Cameron
state: Hired
