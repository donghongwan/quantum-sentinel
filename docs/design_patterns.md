# Design Patterns Used in the Project

## Overview
This document outlines the design patterns implemented in the Quantum Sentinel framework to promote code reusability, maintainability, and scalability.

## 1. Singleton Pattern
**Description**: Ensures that a class has only one instance and provides a global point of access to it.

**Usage**: Used for managing configuration settings and logging instances.

## 2. Factory Pattern
**Description**: Provides an interface for creating objects in a superclass but allows subclasses to alter the type of created objects.

**Usage**: Used in the encryption module to create different types of encryption algorithms based on user input.

## 3. Observer Pattern
**Description**: Defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified.

**Usage**: Used in the logging module to notify various components of log events.

## 4. Strategy Pattern
**Description**: Enables selecting an algorithm's behavior at runtime.

**Usage**: Used in the AI module to switch between different anomaly detection algorithms based on the context.

## 5. Command Pattern
**Description**: Encapsulates a request as an object, thereby allowing for parameterization of clients with queues, requests, and operations.

**Usage**: Used in the CLI module to handle user commands and execute them dynamically.

## Conclusion
These design patterns help maintain a clean architecture and facilitate future enhancements to the Quantum Sentinel framework.
