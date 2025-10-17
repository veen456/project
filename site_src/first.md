---
title: Interactive Functions
author: Vihaan Budhraja
date: October 16, 2025
tags: [jupyter, notebook, frontmatter]
permalink: /functions/interactive/
---

**Interactive functions**

Farenheit to Celcius:


```python
Farenheit = float(input("Your temperature: "))
def F_C():
    Celsius = (Farenheit - 32) * 5/9
    string_farenheit = str(Farenheit)
    string_celsius = str(Celsius)
    print(string_farenheit + " degrees in Farenheit is " + string_celsius + " degrees in Celcius")

F_C()

```

    32.0 degrees in Farenheit is 0.0 degrees in Celcius


Celsius to Farenheit:


```python
Celsius = float(input("Your temperature: "))
def C_F():
    Farenheit = (Celsius - 32) * 5/9
    string_farenheit = str(Farenheit)
    string_celsius = str(Celsius)
    print(string_celsius + " degrees in Celsius is " + string_farenheit + " degrees in Farenheit")

C_F()
```
