PROJECT TITLE: FARMER REGISTRY SYSTEM

PURPOSE: The purpose of the project is to maintain the farmer data and help the business person manage the amount and resourses given to the farmer.

OBJECTIVE: 1)objective of this project is to make the flask app for entering farmer personal details and display the amount he has to pay to the business person.
           2)reduce the workload on the business person.
           3)To learn about the new technologies like flask, SQL-Alchemy, Docker, kubernetes.
           
HIGH LEVEL DESIGN[HLD]:

  ARCHITECTURE DIAGRAM:
  
            ![image](https://user-images.githubusercontent.com/59594811/210315617-6e3782e5-a75a-409a-ac4e-72ab902362b2.png)
            
            
LOW LEVEL DESIGN[LLD]:

    BACKEND:
    
           1) We used Flask as webserver.
           2) using POST and GET methods we post the data to database using Forms and get the data from database using SQLAlchemy.
           3)we will update the database using sessions.
           
           
    FROUNT END:
   
           1) For frountend we used HTML and CSS.
  
    DATABASE:
       
       SERVER:
           1)We used MYSQL Server for data base services and MYSQLDB to connect to database.
           2)We used pymysql as connector to the mysql database.
           3)From MYSQLDB module we used engine and server submodules to connect to server.
           4)We import declarative_base for creating Base class which will create schema tables for our models.
           5) We use inherit that Base class to our models for creating schema.
           
           
       MIGRATIONS:
           1) We will use Migrate and Manager for making migrations for our database.
           2) so that we can revertback to previous versions or update to existing versions.
     

    ENTITIES or MODELS:
   
        1)FARMER:
            Has the properties farmer_id,farmer_name,mobile_number,village_name,address.
       
        2)Fertilizer:
            Has the properties product_id, product_name,unit_cost, supplier,quantity,bags,total_cost.
        
        3)Pestisides:
            Has the properties unit_cost, product_name, toatl_cost, supplier, unit_cost, cottons.
        
        4)Users:
            Has the properties user_id,email,password.
        
        5)Amount:
            Has the properties farmer_id, Amount and date.
            
    Docker:
   
        1) We use Docker to test our app in differnt environment with only necessary resources and anyone can Impliment our app.
        1) We used Docker to containarise our app and MySQL server.
        2) We used Port Binding to Bind both containers.
        
    Kubernetes:
   
        1) We use Kubernetes to deploy our app.
        
   

FUTURE IMPLIMENTATION:

        1) We can integrate our app for Frountend with ReactJS.
        






           



