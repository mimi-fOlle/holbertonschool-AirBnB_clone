# AirBnB clone - The console

![hbnb](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20221012%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20221012T060947Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=f8825506a93cce43be3af37b5c76aa4ff29b3ac60e7bd890bed378e62191643f)

## Description
The object of this project is to deploy on the server a simple copy of AirBnB website. The console, is the first step towards building a full web application: the AirBnB clone. Besides, we will use it for all other following projects, i.e. HTML/CSS templating, database storage, API, front-end integration, etc.
![flow](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20221012%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20221012T060947Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=988ce7a09af82af4855953876a5a97bc28b00454bcb876399db6be274a19ab02)

### Command interpreter 
The console is a command interpreter to manage the objects of  project AirBnB, such as:
-   Create a new object 
-   Retrieve an object from a file, a database etc.
-   Execute operations on objects (i.e. count, compute stats, etc.)
-   Update attributes of an object
-   Destroy an object

## Instruction
First clone the repository:
```
$ git clone https://github.com/MoustaphaElPsyCongroo/holbertonschool-AirBnB_clone.git
```
To launch the console application in interactive mode:
```
$ ./console.py
```
or to use the non-interactive mode:
```
$ echo "your commands here" | ./console.py
```

## Commands
| Commands |Description| Usage|
|--|--|--|
|**create** |Create a new instance of BaseModel, saves it (to the JSON file) and prints the id.| **create** <class_name>|
|**show**|Print the string representation of an instance based on the class name and id|**show** <class_name><class_id>|
|**destroy**|Delete an instance based on the class name and id (save the change into the JSON file)|**destroy** <class_name><class_id>|
|**all**|Print all string representation of all instances based or not on the class name|**all** or **all** <class_name>|
|**update**|Update an instance base on the class name and id by adding or updating attribute (save the change into the JSON file)|**update** <class_name>< class_id>< key>< value>|
|**help or ?**|Display the documented commands|**help**|
|**quit**|Exit the program|**quit**|
|**EOF**|Exit the program|**N/A**|

## Execution
**Interactive mode**
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
**non-interactive mode**
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```
## Examples
- `Create` a new object (`User`, `Place`, `State`, `City`, `Amenity`, `Review`), saves it (to the JSON file) and prints the id.
```
(hbnb) create User
98093c0f-b001-4087-abbd-91ffc3f90fb8
(hbnb)
```
- Retrieve an object from a file by using `show`
```
(hbnb) show User 98093c0f-b001-4087-abbd-91ffc3f90fb8
[BaseModel] (98093c0f-b001-4087-abbd-91ffc3f90fb8) {'id': '98093c0f-b001-4087-abbd-91ffc3f90fb8', 'created_at': datetime.datetime(2022, 10, 12, 17, 40, 58, 133561), 'updated_at': datetime.datetime(2022, 10, 12, 17, 40, 58, 133604)}
(hbnb)
```
- `Update` attributes of an object
```
(hbnb) update User 98093c0f-b001-4087-abbd-91ffc3f90fb8 first_name "Holbie"
(hbnb) show User 98093c0f-b001-4087-abbd-91ffc3f90fb8
[BaseModel] (98093c0f-b001-4087-abbd-91ffc3f90fb8) {'id': '98093c0f-b001-4087-abbd-91ffc3f90fb8', 'created_at': datetime.datetime(2022, 10, 12, 17, 40, 58, 133561), 'updated_at': datetime.datetime(2022, 10, 12, 17, 40, 58, 133604), 'first_name': 'Holbie'}
(hbnb)
```
- `Destroy` an object
```
(hbnb) destroy User 98093c0f-b001-4087-abbd-91ffc3f90fb8
(hbnb) show User 98093c0f-b001-4087-abbd-91ffc3f90fb8
** no instance found **
(hbnb)
```
-  `quit` and `EOF` to  exit the program
```
$./console.py
(hbnb)
(hbnb) quit
$
```

## Tests
All tests are located in folder **tests/**  and can execute all by running this command:
 `$ python3 -m unittest discover tests`

## Authors
**Moustapha Tall** - [Moustapha's github](https://github.com/MoustaphaElPsyCongroo)
**Yeh-Hsin Lee** - [Yeh-Hsin's github](https://github.com/mimi-fOlle)
