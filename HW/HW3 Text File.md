HW3 Text File:

Agile: 
As a vanilla git power-user that has never seen GiggleGit before, I want to easily transfer my knowledge of git to GiggleGit

As a team lead onboarding an experienced GiggleGit user, I want (to) GiggleGit to work with a multitude of software/hardware, 
especially with the current company’s software/hardware

As a professor teaching version control system to my students, I want to clearly understand the step-by-step process 
behind GiggleGit commands and outputs

    Task: Introduce traceability to GiggleGit commands and outputs

        Ticket 1: Create and document traceable models of GiggleGit commands and outputs
            We want the users to understand the “black box” function of GiggleGit commands and outputs. This can be accomplish 
            through creating and documenting traceable, step-by-step models of these commands and outputs. 

        Ticket 2: Display in-progress, computer executions between GiggleGit commands 
            While the processor is executing a GiggleGit command, the terminal should display the in-progress, behind-the-scene 
            computer executions (i.e. Merging = “Compiling branch”, “Pushing branch to main”, etc.)

“As a user I want to be able to authenticate on a new machine” is too vague as a user story. It does not provide details on the 
customer’s viewpoint/“class” (ex. a day-to-day consumer will have different security requirements than admins). The customer’s 
intention/problem is not clearly conveyed in this user story (for all we know, the customer may want a bicycle but the developers 
accidentally build a car).

Formal Requirements:
Goal: Using the GiggleGit interface, the user can easily manage merge requests using memes and sync requests using snickers
Non-Goal: The interface efficiently processes merge and sync requests, generating corresponding meme and snicker outputs
    Non-functional Requirements:

        Reliability
            1. Merges/Sync functions saves files locally 
            2. Copies of merges/sync files are sent to main branch 

        Portability
            1. Meme outputs (i.e. pictures, quotes, videos, etc.) should be portable with different environments (i.e. hardware, 
            OS, etc.)
            2. Create/test different versions of GiggleGit for different environments