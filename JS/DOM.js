
// DOM - Document Object Model

// Dom makes communication with the html document

// Event Listners

// Mouse Events:- 
// 1. click     - single click event in html document
// 2. dblclick  - double click event in html document
// 3. mouseover - when mouse pointer is over the element
// 4. mouseout  - when mouse pointer is out of the element
// 5. mousedown - when mouse pointer is down on the element
// 6. mouseup   - when mouse pointer is up on the element
// 7. mousemove - when mouse pointer is moving on the element
// 8. mouseenter - when mouse pointer is entering the element
// 9. mouseleave - when mouse pointer is leaving the element
// 10. contextmenu - when right click is performed on the element
// 11. wheel - when mouse wheel is scrolled on the element


// Window Events:-
// 1. PageHide - when page is hidden
// 2. PageShow - when page is shown
// 3. Load - when page is loaded
// 4. Unload - when page is unloaded
// 5. BeforeUnload - when page is about to unload
// 6. Error - when error is occurred
// 7. Online - when page is online
// 8. Offline - when page is offline
// 9. AfterPrint - when page is printed
// 10. BeforePrint - when page is about to print


// form Events:-
// 1. Submit - when form is submitted
// 2. Reset - when form is reset
// 3. Change - when form is changed
// 4. Focus - when form is focused
// 5. Blur - when form is blurred
// 6. Input - when form is inputted
// 7. Invalid - when form is invalid 

// Different DOM Methods:-
// 1. getElementById() - returns the element with the specified id
    // example:-
    var x = document.getElementById("demo");

// 2. getElementsByClassName() - returns the elements with the specified class name
    // example:-
    var x = document.getElementsByClassName("demo");

// 3. getElementsByTagName() - returns the elements with the specified tag name
    // example:-
    var x = document.getElementsByTagName("input");

// 4. getElementsByName() - returns the elements with the specified name
    // example:-
    var x = document.getElementsByName("demo");
       //  <input type="text" name="demo">

// 5. createElement() - creates an element
    // example:-
    var x = document.createElement("p");

// 6. createTextNode() - creates a text node
    // example:-
    var x = document.createTextNode("Hello World");

// 7. appendChild() - adds a node as the last child of a specified node
    // example:-
    var x = document.getElementById("demo");
    var y = document.createElement("p");
    x.appendChild(y);

// 8. remove() - removes a node
    // example:-
    var x = document.getElementById("demo");
    x.remove();

// 9. replaceChild() - replaces a child node with another node
    // example:-
    var x = document.getElementById("demo");
    var y = document.createElement("p");
    x.replaceChild(y, x.firstChild);