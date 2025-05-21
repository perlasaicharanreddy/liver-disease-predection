# Liver Disease Prediction

![Project Banner](ReadmeImages/Aspose.Words.e4bfd82e-acc5-43da-8479-c6d62d68f870.002.jpg)

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)

## Introduction
Liver Disease Prediction is a machine learning project aimed at predicting the likelihood of liver disease in patients based on their medical data. The project uses various machine learning algorithms and is deployed as a web application using Streamlit and Heroku.

## Features
- Predicts liver disease likelihood using multiple machine learning models.
- User-friendly web interface for data input and prediction.
- Supports Logistic Regression, KNN, Decision Tree, Random Forest, SVM, and Neural Networks.
- Deployed on Heroku for easy access.

## Technologies Used
- **Programming Language**: Python
- **Libraries**: NumPy, Pandas, Scikit-learn, Streamlit
- **Deployment**: Heroku
- **Data Source**: UCI Machine Learning Repository (Indian Liver Patient Dataset)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/liver-disease-prediction.git
   ```
2. Navigate to the project directory:
   ```bash
   cd liver-disease-prediction
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   streamlit run src/webapp.py
   ```

## Usage
1. Open the web application in your browser.
2. Input patient data such as age, gender, and medical test results.
3. Select a machine learning model from the sidebar.
4. Click "Classify" to get the prediction.

## Screenshots
### Web Application Interface
![Web App](ReadmeImages/Aspose.Words.e4bfd82e-acc5-43da-8479-c6d62d68f870.042.png)

### Data Visualization
![Data Visualization](ReadmeImages/Aspose.Words.e4bfd82e-acc5-43da-8479-c6d62d68f870.033.png)

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature-name"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

# Liver Disease Prediction  

**1.INTRODUCTION** 

**OVERVIEW OF TECHNOLOGIES**  

1.Introduction for Python  

Python  is  a  very  powerful  programming  language  used  for  many  different applications. Over time, the huge community around this open source language has created quite a few tools to efficiently work with Python. In recent years, a number of tools have been built specifically for data science. As a result, analysing data with Python has never been easier. Python is a programming language that lets you work quickly and integrate systems more efficiently. There are two major Python versions- Python 2 and Python 3.  

Both  are  quite  different.  Python  is  a  multi-paradigm  programming  language. Object Oriented programming and structured programming are fully supported, and many  of  its  features  support  functional  programming  and  aspect-oriented programming. 

Many other paradigms are supported via extensions, including design by contract and logic programming. Python uses dynamic typing, and a combination of reference counting and a cycle-detecting garbage collector for memory management. It also features dynamic name resolution (late binding), which binds method and variable names during program execution.Python's design offers some support for functional programming  in  the  Lisp  tradition.  It  has  filter,  map,  and  reduce  functions;  list comprehensions, dictionaries, sets end generator expressions.  

The standard library has  two modules (itertools and functools) that  implement functional tools borrowed from Haskell and Standard ML. Python is meant to be an easily  readable  language.  Its  formatting  is  visually  uncluttered,  and  it  often  uses English  keywords  where  other  languages  use  punctuation.  Unlike  many  other languages,  it  does  not  use  curly  brackets  to  delimit  blocks,  and  semicolons  after statements are optional. It has fewer syntactic exceptions and special cases than C or Pascal 

 2.Introduction for Machine learning 

AI Machine learning  is the scientific study of algorithms and statistical models that computer systems use in order to perform a specific task effectively without using explicit instructions, relying on patterns and inference instead. It is seen as a subset of artificial intelligence. Machine learning algorithms build a mathematical model based on sample data, known as "training data", in order to make predictions or decisions without being explicitly programmed to perform the task. Machine learning algorithms are used in a wide variety of applications, such as email filtering, and computer vision, where it is infeasible to develop an algorithm of specific instructions for performing the task. Machine learning is closely related to computational statistics, which focuses on making predictions using computers. 

The study of mathematical optimization delivers methods, theory and application domains to the field of machine learning. Machine learning tasks are classified into several broad categories. In supervised learning, the algorithm builds a mathematical model from a set of data that contains both the inputs and the desired outputs. For example, if the task were determining whether an image contained a certain object, the training data for a supervised learning algorithm would include images with and without that object (the input), and each image would have a label (the output) designating whether it contained the object. In special cases, the input may be only partially available, or restricted to special feedback. Classification algorithms and regression algorithms are types of supervised learning. 

Classification algorithms are used when the outputs are restricted to a limited set of values. For a classification algorithm that filters emails, the input would be an incoming email, and the output would be the name of the folder in which to file the email.  Regression algorithms are named for their continuous outputs, meaning they may have any value within a range. Examples of a continuous value are the temperature, length, or price of an object. In unsupervised learning, the algorithm builds a mathematical model from a set of data which contains only inputs and no desired output labels. Unsupervised learning algorithms are used to find structure in the data, like grouping or clustering of data points. Unsupervised learning can discover patterns in the data, and can group the inputs into categories

Machine learning is an application of artificial intelligence (AI) that provides systems the ability to automatically learn and improve from experience without being explicitly programmed. Machine learning focuses on the development of computer programs that can access data and use it learn for themselves.

 **Machine Learning Types** 
 
 **Supervised Learning :** 

In supervised learning, we are given a data set and already know what our correct output should look like, having the idea that there is a relationship between the input and output. 

**Two types of Supervised Learning :** 

Regression — Estimate continuous values (Real valued output) Classification — Identify a unique class (Discrete values, Boolean or Categories) 

Regression :-

Regression models a target prediction value based on independent variables. It is mostly  used  for  finding  out  the relationship  between  variables and forecasting. Regression can be used to estimate/ predict continuous values (Real valued output). For example : Given a picture of a person, we have to predict the age on the basis of the given picture . 

Classification :-

Classification means  to group the  output  into  a  class.  If  the  data  set is discrete or categorical then it is a classification problem.For example : Given data about the sizes of houses in the real estate market, making our output about whether the house “sells for more or less than the asking price” i.e. Classifying houses into two discrete categories 

 **Unsupervised Learning :** 

It allows us to approach problems with little or no idea about what our results look like. We can derive structure from data where we don’t necessarily know the effect of the  variables.  We  can  derive  this  structure  by clustering the  data  based  on relationships among the variables in the data. 

Clustering :-

Clustering is the task of grouping a set of objects in such a way that objects in the same group (called a cluster) are more similar (in some sense) to each other than to those in other groups (clusters).For example : Take a collection of 1,000,000 different genes,  and  find  a  way  to  automatically  group  these  genes  into groups  that  are somehow similar or related by different variables, such as lifespan, location, roles, and so on. 

Reinforcement Learning :-

Reinforcement Learning is about taking suitable actions to maximize reward in a particular situation. It is employed by various software and machines to find the best possible behavior or path to take in a specific situation. 

Reinforcement  learning  differs  from  the  supervised  learning  in  a  way  that  in supervised learning  the training data has the answer key with it, so the model is trained with the correct answer itself whereas in reinforcement learning, there is no answer and the reinforcement agent decides what to do in order to perform the given task. In the absence of training data set, it is bound to learn from its experience. 

 **Applications of Machine Learning :-** 
- Virtual Personal Assistants. 
- Predictions while commuting.Videos Surveillance.Social Media Services. 
- Email Spam and Malware Filtering.Online Customer Support. 
- Search Engine Result Refining. 
- Product Recommendations. 
- Online Fraud Detection. 

 **NumPy**  
- NumPy is an open-source numerical Python library. 
- NumPy contains a multi-dimensional array and matrix data structures. 
- It can be utilised to perform a number of mathematical operations on arrays such as trigonometric, statistical, and algebraic routines. Therefore, the library contains a large number of mathematical, algebraic, and transformation functions. 
- NumPy is an extension of Numeric and Numarray. 
- Numpy also contains random number generators. 
- NumPy is a wrapper around a library implemented in C. 

**Pandas** 
In computer programming, pandas is a software library written for the Python programming language for data manipulation and analysis. In particular, it offers data structures and operations for manipulating numerical tables and time series. It is free software released under the three-clause BSD license.

**Scikit-learn** 

Scikit-learn (Sklearn) is the most useful and robust library for machine learning in Python. It provides a selection of efficient tools for machine learning and statistical modeling including classification, regression, clustering and dimensionality reduction via a consistence interface in Python. This library, which is largely written in Python, is built upon NumPy, SciPy and Matplotlib. 

**Streamlit** 

Streamlit is an open-source Python library that makes it easy to create and share beautiful, custom web  apps for  machine  learning  and data science. In just a few minutes you can build and deploy powerful data apps 

**Heroku**  

Heroku is a container-based cloud Platform as a Service (PaaS). Developers use Heroku to deploy, manage, and scale modern apps. Our platform is elegant, flexible, and easy to use, offering developers the simplest path to getting their apps to market.

Heroku is fully managed, giving developers the freedom to focus on their core product without the distraction of maintaining servers, hardware, or infrastructure. The Heroku experience provides services, tools, workflows, and polyglot support all designed to enhance developer productivity.

Heroku enables developers to build, run and operate application entirely on cloud rather than doing locally on your machine. In this project we will deploy using heroku git. There are other methods as well to deploy.

**EXISTINGSYSTEM** 

Existing methods using support vector machine and K-nearest neighbour. 

**1.2.1 Limitations of existing system** 

classification is slower and costlier with respect to time and memory  

**OBJECTIVES** 

In India, delayed diagnosis of diseases is a fundamental problem due to a shortage of medical professionals. A typical scenario, prevalent mostly in rural and somewhat in urban areas is:  

- A patient going to a doctor with certain symptoms.  
- The doctor recommending certain tests like blood test, urine test etc depending on the symptoms.  
- The patient taking the aforementioned tests in an analysis lab.  
- The patient taking the reports back to the reports back to the hospital, where they are examined and the disease is identified.  

The aim of this project is to somewhat reduce the time delay caused due to the unnecessary back and forth shuttling between the hospital and the pathology lab.A machine learning algorithm will be trained to predict a liver disease in patients.** 

**OUTCOMES** 

The Patients data is collected from UCI machine learning repository. With this data will be going to train the Machine  learning  Models and   evaluate accuracy. Then Deploy in the website. When the new patient data is entered in the website we can predict the likelihood weather the patient has liver disease or not    

**APPLICATIONS** 

This strategy used for liver disease prediction

**STRUCTURE OF PROJECT (SYSTEM ANALYSIS)** 

![]( ReadmeImages/Aspose.Words.e4bfd82e-acc5-43da-8479-c6d62d68f870.002.jpg)

Fig: 1.1 Project SDLC 

- Project Requisites Accumulating and Analysis 
- Application System Design 
- Practical Implementation 
- Manual Testing of My Application 
- Application Deployment of System 
- Maintenance of the Project 
1. **Requisites Accumulating And Analysis** 

It’s the first and foremost stage of the any project as our is a an academic leave for requisites  amassing  we  followed  of  IEEE  Journals  and  Amassed  so  many  IEEE Relegated papers and final culled a Paper designated “Individual web revisitation by setting and substance importance input and for analysis stage we took referees from the paper and did literature survey of some papers and amassed all the Requisites of the project in this stage 

2. **System Design** 

In  System  Design  has  divided  into  three  types  like  GUI  Designing,  UML Designing with avails in development of project in facile way with different actor and its utilizer case by utilizer case diagram, flow of the project utilizing sequence, Class diagram gives information about different class in the project with methods that have to be utilized in the project if comes to our project our UML Will utilizable in this way The third and post import for the project in system design is Data base design where we endeavor to design data base predicated on the number of modules in our project 

3. **Implementation** 

The Implementation is Phase where we endeavor to give the practical output of the work done in designing stage and most of Coding in Business logic lay coms into action in this stage its main and crucial part of the project

4. **TestingUnit Testing** 

It is done by the developer itself in every stage of the project and fine-tuning the bug and module predicated additionally done by the developer only here we are going to solve all the runtime errors 

5. **Manual Testing** 

As our Project is academic Leave, we can do any automatic testing so we follow manual testing by endeavor and error methods 

6. **Deployment Of System And Maintenance** 

Once the project is total yare, we will come to deployment of client system in genuinely world as its academic leave we did deployment i our college lab only with all need Software’s with having Windows OS . 

The Maintenance of our Project is one-time process only 

7. **FUNCTIONAL REQUIREMENTS** 

1\.Data Collection 2.Data Pre-processing 3.Training And Testing 4.Modeling  5.Predicting 

8. **NON FUNCTIONAL REQUIREMENTS** 

NON-FUNCTIONAL REQUIREMENT (NFR) specifies the quality attribute of a software system. They judge the software system based on Responsiveness, Usability, Security, Portability and other non-functional standards that are critical to the success of the software system. Example of nonfunctional requirement, “how fast does the website load?” Failing to meet non-functional requirements can result in systems that fail  to  satisfy  user  needs.  Non-  functional  Requirements  allows  you to  impose constraints  or  restrictions  on  the  design  of  the  system  across  the  various  agile backlogs.  Example,  the  site  should  load  in  3  seconds  when  the  number  of simultaneous users are > 10000. Description of non-functional requirements is just as critical as a functional requirement. 

- Usability requirement 
- Serviceability requirement 
- Manageability requirement 
- Recoverability requirement 
- Security requirement 
- Data Integrity requirement 
- Capacity requirement 
- Availability requirement 
- Scalability requirement 
- Interoperability requirement 
- Reliability requirement 
- Maintainability requirement 
- Regulatory requirement 
- Environmental requirement 

1. **Examples Of Non-Functional Requirements** 

Here, are some examples of non-functional requirement: 

1. Users must upload dataset 
2. The software should be portable. So moving from one OS to other OS does not create any problem. 
3. Privacy  of  information,  the  export  of  restricted  technologies, intellectual property rights, etc. should be audited. 


2. **Advantages Of Non-Functional Requirement** 

Benefits/pros of Non-functional testing are: 

- The nonfunctional requirements ensure the software system follow legal and compliance rules. 
- They  ensure  the  reliability,  availability,  and  performance  of  the software system 
- They  ensure  good  user  experience  and  ease  of  operating  the software. 
- They help in formulating security policy of the software system.

3. **Disadvantages Of Non-Functional Requirement** 

   Cons/drawbacks of Non-function requirement are: 

- None  functional  requirement  may  affect  the  various  high-level software subsystem 
- They  require  special  consideration  during  the  software architecture/high-level design phase which increases costs. 
- Their implementation does not usually map to the specific software sub-system, 
- It is tough to modify non-functional once you pass the architecture phase.

2. **LITERATURE SURVEY** 

This  seems  to  be  a  classic  example  of  supervised  learning.  We  have  been provided with a fixed number of features for each data point, and our aim will be to train a variety of Supervised Learning algorithms on this data, so that , when a new data point arises, our best performing classifier can be used to categorize the data point as a positive example or negative. Exact details of the number and types of algorithms  used  for  training  is  included  in  the  'Algorithms  and  Techniques' sub-section of the 'Analysis' part. 

3. **PROBLEM STATEMENT** 

The problem statement is formally defined as:  

Given  a  dataset  containing  various  attributes  of  584  Indian  patients,  use  the features available in the dataset and define a supervised classification algorithm which can identify whether a person is suffering from liver disease or not. This data set contains 416 liver patient records and 167 non- liver patient records.The data set was collected from north east of Andhra Pradesh, India. This data set contains 441 male patient records and 142 female patient records. Any patient whose age exceeded 89 is listed as being of age "90". 

 STRATEGY :- 

This seems to be a classic example of supervised learning. We have been provided with a fixed number of features for each data point, and our aim will be to train a variety of Supervised Learning algorithms on this data, so that , when a new data point arises, our best performing classifier can be used to categorize the data point as a positive example or negative. Exact details of the number and types of algorithms used for training is included in the 'Algorithms and Techniques' sub-section of the 'Analysis' part. 

**METRICS :-

In  problems  of  disease  classification  like  this  one,  simply  comparing  the accuracy, that is, the ratio of correct predictions to total predictions is not enough. This is because depending on the context like severity of disease, sometimes it is more important that an algorithm does not wrongly predict a disease as a non-disease, while predicting a healthy person as diseased will attract a comparatively less severe penalty.  

Thus, here we will use F-1 score as a performance metric, which is basically the weighted harmonic mean of precision and recall. Precision and Recall are defined as:  

Precision=TP/ (TP+FP), Recall=TP/ (TP+FN), where  

TP=True Positive  

FP=False Positive  

FN=False Negative  


3. **PROBLEM ANALYSIS** 

EXISTING APPROACH:- 

Existing methods using support vector machine and K-nearest neighbour. 

 Drawbacks:-

Classification is slower and costlier with respect to time and memory 

ROPOSED SYSTEM ;-

By using machine learning the liver disease can detected and prevented. Sklearn, numpy,  pandas  these  are  the  some  of  the  packages  for  understanding  purpose  of machine  learning.  Liver  disease  have  been  continuously  increasing  because  of excessive consumption of alcohol, inhale of harmful gases, intake of contaminated food, pickles and drugs 

Advantages:-
- Fast, 
- less time  

SOFTWARE AND HARDWARE REQUIREMENTS:

Software Requirements:-

The functional requirements or the overall description documents include the product perspective and features, operating system and operating environment, graphics requirements, design constraints and user documentation.
The appropriation of requirements and implementation constraints gives the general overview of the project in regards to what the areas of strength and deficit are and how to tackle them.
•	Python IDE 3.7 version   (or)
•	Anaconda 3.7   ( or)
•	Jupiter   (or)
•	Google colab

 Hardware Requirements ;-
Minimum hardware requirements are very dependent on the particular software being developed by a given Enthought Python / Canopy / VS Code user. Applications that need to store large arrays/objects in memory will require more RAM, whereas applications that need to perform numerous calculations or tasks more quickly will require a faster processor.
•	Operating system		: windows, Linux
•	Processor			: minimum Intel i3
•	Ram				:  minimum 4 GB
•	Hard disk 			: minimum 250GB


![]( ReadmeImages/Aspose.Words.e4bfd82e-acc5-43da-8479-c6d62d68f870.003.jng)

Fig 3.1 Dataset 

**Columns:** 

- Age of the patient 
- Gender of the patient 
- Total Bilirubin 
- Direct Bilirubin 
- Alkaline Phosphotase 
- Alamine Aminotransferase 
- Aspartate Aminotransferase 
- Total Protiens 
- Albumin 
- Albumin and Globulin Ratio 
- Data set: field used to split the data into two sets (patient with liver disease, or no disease) 



**EXPLORATORY DATA ANALYSIS** 

COUNT PLOT OF LIVER PATIENTS DIAGNOISED Number of patients diagnosed with liver disease: 416 
Number of patients not diagnosed with liver disease:   167 

![]( ReadmeImages/Aspose.Words.e4bfd82e-acc5-43da-8479-c6d62d68f870.004.png)

Fig 3.2 EDA1 

COUNT PLOT OF MALE & FEMALE PATIENTS Number of patients that are male:  441 
Number of patients that are female:  142 

![]( ReadmeImages/Aspose.Words.e4bfd82e-acc5-43da-8479-c6d62d68f870.005.png)

Fig 3.3 EDA2 

LGORITHMS**  

Decision trees
logistic regression
Naive Bayes
random forests
linear and SVMs
Neural Networks

4.**DESIGN**

4.1 UML DIAGRAMS:

The  System  Design  Document  describes  the  system  requirements,  operating environment,  system  and  subsystem  architecture,  files  and  database  design,  input formats, output layouts, human-machine interfaces, detailed design, processing logic, and external interfaces. 

Global Use Case Diagrams:

Identification of actors: 

Actor: Actor represents the role a user plays with respect to the system. An actor interacts with, but has no control over the use cases. 

Graphical representation: 

![]( ReadmeImages/Aspose.Words.e4bfd82e-acc5-43da-8479-c6d62d68f870.006.png)  ![]( ReadmeImages/Aspose.Words.e4bfd82e-acc5-43da-8479-c6d62d68f870.007.png)
![]( ReadmeImages/Aspose.Words.e4bfd82e-acc5-43da-8479-c6d62d68f870.008.png)

Actor
An actor is someone or something that:Interacts with or uses the system. Provides input to and receives information from the system. 
Is external to the system and has no control over the use cases.  

Actors are discovered by examining: 

- Who directly uses the system? 
- Who is responsible for maintaining the system? 
- External hardware used by the system. 
- Other systems that need to interact with the system. Questions to identify actors: 

Who is using the system? Or, who is affected by the system? Or, which groups need help from the system to perform a task? 

Who  affects  the  system?  Or,  which  user  groups  are  needed  by  the  system  to perform its functions? These functions can be both main functions and secondary functions such as administration. 

Which external hardware or systems (if any) use the system to perform tasks? 

What problems does this application solve (that is, for whom)? 

And, finally, how do users use the system (use case)? What are they doing with the system? 

The actors identified in this system are: 

- System Administrator 
- Customer 
- Customer Care

 Identification of usecases: 

Usecase:  A use case can be described as a specific way of using the system from a user’s (actor’s) perspective. 

 Graphical representation: 

![]( ReadmeImages/Aspose.Words.e4bfd82e-acc5-43da-8479-c6d62d68f870.009.png)

A more detailed description might characterize a use case as: 

- Pattern of behavior the system exhibits 
- A sequence of related transactions performed by an actor and the 

system 

- Delivering  something  of  value  to  the  actor  Use  cases  provide  a 

means to: 

- capture system requirements 
- communicate with the end users and domain experts 
- test the system 

Use cases are best discovered by examining the actors and defining what the actor will be able to do with the system. 

Guide lines for identifying use cases: 

- For each actor, find the tasks and functions that the actor should be able to perform or that the system needs the actor to perform. The use case should represent a course of events that leads to clear goal 

- Name the use cases. 
- Describe the use cases briefly by applying terms with which the user is familiar. This makes the description less ambiguous 

Questions to identify use cases: 

- What are the tasks of each actor? 
- Will any actor create, store, change, remove or read information in the system? 

- What use case will store, change, remove or read this information? 
- Will  any  actor  need  to  inform  the  system  about  sudden  external changes? 
- Does  any  actor  need  to  inform  about certain occurrences in the system? 
- What usecases will support and maintains the system? 

Flow of Events

A flow of events is a sequence of transactions (or events) performed by the system. They typically contain very detailed information, written in terms of what the system should do, not how the system accomplishes the task. Flow of events are created as separate files or documents in your favorite text editor and then attached or linked to a use case using the Files tab of a model element. 

A flow of events should include: 

- When and how the use case starts and ends 
- Use case/actor interactions 
- Data needed by the use case 
- Normal sequence of events for the use case 
- Alternate or exceptional flows Construction of Usecase diagrams: 

Use-case  diagrams  graphically  depict  system  behavior  (use  cases). These diagrams present a high level view of how the system is used as viewed from an outsider’s (actor’s) perspective. A use-case diagram may depict all or some of the use cases of a system. 

A use-case diagram can contain: 

- actors ("things" outside the system) 
- use cases (system boundaries identifying what the system should do) 
- Interactions  or  relationships  between  actors  and  use  cases  in  the 

system including the associations, dependencies, and generalizations. 

Relationships in use cases: 

4.1.3.1 Communication:

The communication relationship of an actor in a usecase is shown by connecting the actor symbol to the usecase symbol with a solid path. The actor is said to communicate with the usecase. 

4.1.3.2 Uses: 

A Uses relationship between the usecases is shown by generalization arrow from the usecase. 

4.1.3.3 Extends:

The  extend  relationship  is  used  when  we  have  one  usecase  that  is similar  to  another  usecase  but  does  a  bit  more.  In  essence  it  is  like subclass. 

4. SEQUENCE DIAGRAMS

A sequence diagram is a graphical view of a scenario that shows object interaction in a time- based sequence what happens first, what happens next. Sequence diagrams establish the roles of objects and help provide essential information to determine class responsibilities and interfaces. There are two main differences between sequence and collaboration diagrams: sequence diagrams show time-based object interaction while collaboration  diagrams  show  how  objects  associate  with  each  other.  A  sequence diagram  has  two  dimensions:  typically,  vertical  placement  represents  time  and horizontal placement represents different objects. 

Object: 

An object has state, behavior, and identity. The structure and behavior of similar objects are defined in their common class. Each object in a diagram indicates some instance of a class. An object that is not named is referred to as a class instance. 

The object icon is similar to a class icon except that the name is underlined: An object's concurrency is defined by the concurrency of its class. 

Message: 

A message is the communication carried between two objects that trigger an event. A message carries information from the source focus of control to the destination focus of control. The synchronization  of  a  message can be  modified  through

the  message specification. Synchronization means a message where the sending object pauses to wait for results. 

Link: 

A link should exist between two objects, including class utilities, only if there is a relationship  between  their  corresponding  classes.  The  existence  of  a  relationship between two classes symbolizes a path of communication between instances of the classes: one object may send messages to another. The link is depicted as a straight line between objects or objects and class instances in a collaboration diagram. If an object links to itself, use the loop version of the icon. 

5. CLASS DIAGRAM: Identification of analysis classes: 

A class is a set of objects that share a common structure and common behavior (the same attributes, operations, relationships and semantics). A class is an abstraction of real-world items. There are 4 approaches for identifying classes: 

1. Noun phrase approach: 
2. Common class pattern approach. 
2. Use case Driven Sequence or Collaboration approach. 
2. Classes , Responsibilities and collaborators Approach 

Noun Phrase Approach: 

The guidelines for identifying the classes: 

- Look for nouns and noun phrases in the usecases. 
- Some classes are implicit or taken from general knowledge. 
- All  classes  must  make  sense  in  the  application  domain;  Avoid computer implementation classes – defer them to the design stage. 
- Carefully choose and define the class names After identifying theclasses we have to eliminate the following types of classes: 
- Adjective classes. Common class pattern approach: 

The following are the patterns for finding the candidate classes: 

- Concept class. 
- Events class. 
- Organization class 
- Peoples class 
- Places class 
- Tangible things and devices class. 

Use case driven approach: 

We have to draw the sequence diagram or collaboration diagram. If there is need for some classes to represent some functionality then add new classes which perform those functionalities. 

CRC approach: 

The process consists of the following steps: 

- Identify classes’ responsibilities ( and identify the classes ) 
- Assign the responsibilities 
- Identify the collaborators. Identification of responsibilities of each 

class: 

The questions that should be answered to identify the attributes and methods of a class respectively are: 

1. What information about an object should we keep track of? 
1. What services must a class provide? Identification of relationships among the classes: 

Three types of relationships among the objects are: Association: How objects are associated? 

Super-sub structure: How are objects organized into super classes and sub classes? Aggregation: What is the composition of the complex classes? 

Association: 

The questions that will help us to identify the associations are: 

1. Is the class capable of fulfilling the required task by itself? 
1. If not, what does it need? 
1. From what other classes can it acquire what it needs? Guidelines for 

identifying the tentative associations: 

- A dependency between two or more classes may be an association. Association often corresponds to a verb or prepositional phrase. 
- A  reference  from  one  class  to  another  is  an  association.  Some associations are implicit or taken from general knowledge. 

Some common association patterns are: 

Location  association  like  part  of,  next  to,  contained  in….. Communication association like talk to, order to …… 

We  have  to  eliminate  the  unnecessary  association  like  implementation associations, ternary or n-ary associations and derived associations. 

Super-sub class relationships: 

Super-sub class hierarchy is a relationship between classes where one class is the parent class of another class (derived class).This is based on inheritance. 

Guidelines for identifying the super-sub relationship, a generalization are

 **Top-down*: 
Look for noun phrases composed of various adjectives in a class name. Avoid excessive refinement. Specialize only when the sub classes have significant behavior. 

**Bottom-up*:

Look for classes with similar attributes or methods. Group them by moving the common  attributes  and  methods  to  an  abstract  class.  You  may  have  to  alter  the definitions a bit. 

Re-usability*:

Move the attributes and methods as high as possible in the hierarchy.

 Multiple inheritances:

Avoid  excessive  use  of  multiple  inheritances.  One  way  of  
