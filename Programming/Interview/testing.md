# Testing

## What Testing Tells About You

- Big Picture Understanding
	- Are you a person who understands what the software is really about?
- Knowing How the Pieces Fit Together
	- Do you understand how software works, and how it might fit into a greater system? 
	- ex. Do you understand how Google Spreadsheets fits into the rest of Google's ecosystem?
- Organization
	- Do you approach the problem in a structured manner?
- Practicality
	- Can you actually create reasonable testing plans?

## Testing a Real World Object / Testing a piece of Software
Testing a real world object and testing a piece of software are very similar. The major difference is that software testing generally places a greater emphasis on the details of performing testing. 

Software testing has two core aspects to it:

**Manual vs Automated Testing**
Both are an essential part of the testing process with different strengths. Whereas automated testing is generally used to identify issues a computer has been told to look for, manual testing is used to reveal new issues that are too qualitative for a computer to effectively examine. 

**Black Box Testing vs White Box Testing**
The distinction refers to the degree of access we have into the software. In black box testing, we are given the software as-is and need to test it (as a normal user would test the software). In white box testing, we have additional programmatic access to test individual functions (as a programmer would test the software).

### Steps Involved in Testing Real World Object / Software
1. Are we doing Black Box Testing or White Box Testing? (S/W)
2. Who will use it? And why?
3. What are the use cases?
4. What are the bounds of use?
No product is fail-proof, so analyzing failure conditions needs to be part of your testing. Think about when it is acceptable for the product to fail, and what failure should mean.
5. What are the stress conditions / failure conditions?
When the software fails, what should the failure look like?
6. What are the test cases? How would you perform the testing?

## Testing a Function

### Steps Involved in Testing Functions
1. Define the test cases
	- Normal case
	- Extreme cases
		- What happens when you pass in an empty array to sort? or an array with only one element?
	- Nulls and "illegal" input
		- What happens when you pass a negative number to a function that takes in a positive number?
	- Strange input
		- What happens if you pass an already sorted array as the input of a sorting function? 
2. Define the expected result
	- ex. Should `sort` return, a copy of the sorted array, or the array sorted in-place?
3. Write test code

## Troubleshooting

### Steps Involved in Troubleshooting Issues
1. Understand the Scenario
	- Ask questions to understand as much about the situation as possible
2. Break down the problem
	- Break down the problem into testable units
3. Create Specific, Manageable Tests

## From:
- Cracking the Coding Interview