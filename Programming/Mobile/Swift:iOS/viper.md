# VIPER Architecture

## Overview
VIPER is a shorthand for **View, Interactor, Presenter, Entity, and Router**. The architecture based on Single Responsibility Principle, which states that every module or class should have responsibility over a single part of the functionality provided by the software, and that responsibility should be entirely encapsulated by the class.

**View**
- Responsible for sending user actions to the Presenter and showing whatever the Presenter tells it.

**Interactor**
- Contains the business logic.

**Presenter**
- Responsible for getting the data from the Interactor on user actions.
- Responsible for sending the data received from the Interactor to the View for a display. 

**Entity**
- Contains basic model objects used by the Interactor.

**Router**
- Contains all navigation logic for describing which screens are to be shown when. Normally written as a wireframe.

## Advantages
- Decouples the code for reusability and testability.
- Divides the application components based on its role.
- Adding new features is easier.
- Easier to write automated tests since your UI logic is separated from the business logic.

## From:
- [Building iOS Apps with VIPER Architecture](https://blog.mindorks.com/building-ios-app-with-viper-architecture-8109acc72227)