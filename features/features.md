# Features

## Making an appliation

### Personas
John Sportssecretary

### Feature: Applying for spaces for activities

* John wants to arrange football for their senior and 12 year old members in Helsinki's spaces in 2021
    * Given that there is an application period open for 2021 that have
    Metsälän kenttä and Oulunkylän urheilupuisto suitable for football
    * And there is Oulunkylän tekojäärata suitable for skating
    * John selects application period that offers spaces for football and the applications are open for year 2021
    * John selects Oulunkylä as an area they operate in 
    * John sees that Metsälän kenttä and Oulunkylän urheilupuisto are
     in the area and are suitable for football
        * John selects Metsälän kenttä and Oulunkylän urheilupuisto as a places 
        he wants to football in
            * John would prefer to arrange activities in urheilupuisto
    * John sees that there are free times in Metsälän kenttä and Oulunkylän urheilupuisto
    on tuesdays from 10.00 to 20.00 and on thursdays from 14.00 to 19.00
        * John would prefer to have their 12 year old members to practice on 
        tuesdays between 10.00 and 14.00 for 1 hour
            * If that can not be arranged then John would like them to practice on 
            thursdays from 14.00-17.00
            * John describes that the 12 years will play some football and 
            run around wildly during these football activities
        * John would prefer to have their senior members to practice
        on tuesdays from 16.00 to 20.00 for 1.5 hours
            * If that can not be arranged then John would like them to practice on 
            thursdays between 17.00-19.00 for 1 hour
            * John describes that these senior members will play some football
            and talk bout weather during this activity 
    * John fills in ### organisation information for oulunkylän pallo
    * John sends the application
    * Then he sees that their application for activities for their 12 years old
     and their seniors is due to being processed in two weeks
        
### Feature: Managing organisation information
* John wants to set the organisation for their application
    * John fills Oulynkylän Pallo as their organisation name
    * John 1234-123 as their Y tunnus
    * John fills in Address information for Oulunkylän pallo
    * John adds Teppo Tukihenkilö as contact persons
    * The he sees that Oulunkylän pallo has (*) and Teppo as contact person

### Feature: Address information

* John wants to fill in address information for Oulynkylän Pallo
    * John fills in Käskynhaltijantie 11 as street address, 00640 as postal code and Helsinki as city
    * John saves the information
    * Then he sees that Oulunkylän pallo has address (*) 


## Models

### Application (hakemus)
|Field   |Mandatory   |Rules|Model|
|---|---|---|---|
|Application period   |true   |   |ApplicationPeriod|
|Organisation   |true   |   |Organisation|
|Spaces   |true   |   |1..* Space|
|Events   |   |   |0..* ApplicationEvent|

### ApplicationEvent (vuoro)
|Field   |Mandatory   |Rules|Model|
|---|---|---|---|
|Number of persons   |false   |   ||
|Area   |false   |   |District|
|Age group   |false   |   |AgeGroup|
|Ability group   |false   |   |AbilityGroup|
|Ability group   |false   |   |AbilityGroup|
|Application   |true   |   |Application|
|Times   |true   ||1..* Recurrence|
|Number of persons   |true   |||
|Duration   |true   |||

### Recurrence (vuoron aika)
|Field   |Mandatory   |Rules|Model|
|---|---|---|---|
|Application event   |true   |   |ApplicationEvent|
|Starting   |true   |Must be between the start and end of the Application period reservation period|date|
|Ending   |true   |Must be between the start and end of the Application period reservation period|date|
|Date of week   |true   |   ||
|start time   |true   |   |time|
|end time   |true   |   |time|
|priority   |false   |default medium||

### Organisation (hakija)
|Field   |Mandatory   |Rules|Model  |
|---|---|---|---|
|Y tunnus   |true   |||
|Name|true   |  |   |
|Year established|false   |  |   |
|Address|true   |  |Address|
|Contact person|true   |    |Person|
