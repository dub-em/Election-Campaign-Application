# Election-Campaign-Application

## Phase 1 (Citizens' Voice)
+ This Project was inspired by real problems and experiences of many people living in undeveloped countries with seemingly dormant government public office holders, but as a whole it simply aims to breech the gap betweeen the government and the people. This project is the first phase of an intended and much bigger idea, which is fundamentally based on raising awareness amongst the people on their rights and powers as the "people", helping them understand the government structure which presides over them, gradually removing the anonymity that exists between some lower level public office holdlers and the people, and also making it easier for public office holders who have genuine interest in listening to the people to be able to do that without a middle-man.
+ This phase of the project will tackle the last problem outlined in the last statement of the previous bullet, which is "making it easier for public office holders who have genuine interest in listening to the people to be able to do that without a middle-man". This basically means public office holders will have a quick one-stop access to the sentiments, views, values and frequent complaints of the people. This is why this phase of the project has been given the name "Citzens' Voice", in the hopes that the "incorruptible" part of the government can be influenced by the voice of the ctizens, through this project.  

### Problem Statement (Citizens' Voice)
+ There is a significant disconnect between public office holders and the sentiment/complaints of the citizens they preside over, even in cases where the said public office holder or leader is willing to pay attention. This issue has been largely tackled in developed countries, but still remain a major hinderance in undeveloped countries.
+ This problem also makes it difficult for people in power to lead a people-driven development, rather they end up executing policies and project they believe best with little influence from what the citizens think.
+ This problem also leads to generic campaigns, when in reality different states or districts may have different problems to address. A generic campaign might work more in underdeveloped countries, but as these countries start to develop, this generalized approach starts to have diminishing returns.
+ This is but to mention a few, and will be expanded upon as the project gets scaled up.

### Project Description
+ This phase of the project is split into 3 main parts, which all have their respective dedicated branches in the project repository. The phase was developed in a more decentarlized manner to reduce the vulnerability of the entire project to either of the separate branches.
+ The three main parts/branches are;
    - Election Database (branch name: election_database)
        - This part/branch of the phase 1 was focused on creating and deploying an AWS Postgres Instance.
        - Pulling a week's worth of data from Twitter API (one of many intended sources of data that will be exploited in the subsequent phases of the project), and storing it on the remote Postgres database, so as to make the project less dependent of on the response time of the Twitter API.
        - Hosting a Script to update the database on a daily basis, and delete any data older than a week, as the intended focus period is a week.
    - Research Questions API (branch name: research_questions_api)
        - Documentation Link: https://research-questions-api.herokuapp.com/docs#/ 
        - This application will enable end-users to answer essential campaign and governance related question, using extracted, wrangled and analyzed data from the social media platform (Twitter), which has already been stored in the AWS remote postgres instance. As this project is scaled up, more social platform will be included in the extraction source.
        - The research questions cover four main areas of focus, which is aimed at gaining an insight into the thought, complaints and sentiment of the citizens on certain areas of government or general topics, as well as their views and sentiments on various public office holders.
        - The four main areas are;
            - General Trends
            - Citizens' Sentiment
            - Complaint Areas
            - Politicians' Reputation
    - Election Campaign TPL (branch name: election_campaign_TPL)
        - Library Link: https://pypi.org/project/election-campaign/
        - This library serves as an extension of and for the election campaign API. It is intended to aid developers who decide to use the API in a python IDE for research work related to election campaign and governance.

### Further Description
+ Please refer to the various branches for further description and view of the source codes.

### Phase 1 Project Flow
![alt text](https://github.com/dub-em/Election-Campaign-Application-Phase2/blob/main/Project_Conclusion/ProjectFlow/Phase1_ProjectFlow.png?raw=true)

### Article
+ https://www.linkedin.com/pulse/citizens-voice-michael-igbomezie/

### Contribution
This Project is open to contribution and collaboration. Feel free to connect to join the project collaborators.

### Author(s)
+ Michael Dubem Igbomezie
    - Email: michaeligbomezie@gmail.com
    - Github: @dub-em
    - Pypi: https://pypi.org/user/Dubem/
+ George Michael Dagogo
    - Email: georgemichaeldagogo@gmail.com
    - Github: @George-Michael-Dagogo
