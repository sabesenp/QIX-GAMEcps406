========
QIX GAME 
========

Group 49: p9_mQix_Game 
Hello! This is a simple recreation of the classic arcade game Qix, developed and published by Taito America. 
This Qix is being developed in Python using the Pygame library. This project is for CPS406 at TMU

Qix is a simple game where you control a character and attempt to capture a field. As you capture, 
new boundaries get drawn. Enemies will attempt to collide into you, reducing HP. You are vulnerable 
whether you are resting on the edge or pushing out to capture!

~~ The Team ~~
Carissa Larocque - Team Leader, Lead Programmer
Muran Ganesan  
Sabesen Pathmanathan
Ryan Aleixo

============================
Various References and Docs: 
============================
UML Charts: https://lucid.app/lucidchart/c3363d6f-15bd-482f-bf43-4e4118a9243d/edit?viewport_loc=222%2C-1416%2C2783%2C1629%2C1Uol60Xt.ZZj&invitationId=inv_9cbecb7d-0ae9-4989-8b5f-4f0a3463677f
Pygame Docs: https://www.pygame.org/docs/

========================================================
As you can see, there is not much here yet but plans. So, let's outline a few plans:

The main control scheme is the arrow keys and the spacebar. However, there are plans to allow for key binding in the options menu!

Class Descriptions:
ACTOR CLASS: Defines characters and sprites. Used for inheriting movement, colour, etc.

MENU CLASS: Defines menu drawing, affects program state. Note that the UI class, which controls score and game loop state,
will be an instance of or implement menu.

FIELD CLASS: A special class used in the main game loop. Interacts with the UI for score and affects game state. 
An edge or boundary of the field is defined as just a limited section of the field

PLAYER: Subclass of ACTOR. It implements movement using the player input as parameters

ENEMY: Subclass of ACTOR. It has a negative HP to denote damage output. It's movement is made by the program and randomized. Every
child of the enemy class must specify a 'habitat' attribute. habitat determines where an enemy is allowed to move and affect other entities

QIX: Subclass of ENEMY. It's habitat is field

SPARC: Subclass of ENEMY. It's habitat is edge

All of the above is subject to change as this is a living document. For example, it is not currently clear whether menus will have subclasses
or be a instance of a class.

