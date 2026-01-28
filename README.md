# 🌲 Binomial Tree Visualization

A small application visualizing the effects of volatility on option prices under certain conditions. Does not accurately model option prices, but rather iteratively models the asset price evolution without considering option payoffs 

---

## 🍃 Features

### 1. Plotting interface to display details for each possibility 


https://github.com/user-attachments/assets/2602c9a1-a0b6-4336-af86-1d720afa499c

### 2. Scales to change properties of the options 


https://github.com/user-attachments/assets/0a39637f-cf1c-49cd-a9e9-a6e7f5acbdb4

---

## 📐 Theory

### 1. Time Step 

Splitting time expiration into steps to simulate the value of the option at a particular step

<h3 align="center">T = time until expiration</h3>
<h3 align="center">N = Number of Steps</h3>
<h1 align="center"> ∆T = $\frac{T}{N}$ </h1>

### 2. Exponential Growth/Decay 

<div>Continuous compounding prices to reflect potential market outcomes (Cox–Ross–Rubinstein model)</div>
<div>Vega (σ) is treated as an input parameter from the user (Uprate & Downrate sliders)</div>

<h1 align="center">U (up rate) = e<sup>σΔt</sup></h1>
<h1 align="center">D (down rate) = e<sup>-σΔt</sup></h1>

### 3. Iterative approach to price using nodes 
<div>Using a standard binomial function:</div>
<h1 align="center">S<sub> i,j </sub>​ = S0​ * u<sup> j</sup> * d<sup> i−j</sup></h1>
<div>Where i = time step and j = number of upward moves</div>​

## 🛠️ Tech Stack
* **Math** - Used to calculate prices
* **Matplotlib** - Interactive Graphing system
* **Numpy** - Condensing multi-dimentional arrays
* **Collections** - Storing possible option prices
* **Tkinter** - UI interface + Interactive link to matplotlib 
---
