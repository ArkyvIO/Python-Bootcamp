# Day 9: Silent Auction Program - Dictionaries and Nesting Concepts

## Project Description

The Day 9 project involves the creation of a silent auction program in Python, showcasing the use of dictionaries and demonstrating nesting concepts. This project highlights nested conditional statements and loops, illustrating their application within the context of managing participant bids and determining the auction winner.

## Key Concepts Applied

- **Dictionaries in Python:** Utilizing dictionaries to organize and store information related to auction participants and their bids.
- **Nesting Concepts - Conditional Statements and Loops:** Implementing nested conditional statements within loops to manage auction-related logic and decision-making processes.
- **Silent Auction Implementation:** Creating a program that facilitates a silent auction, managing participant details and bids in an organized manner using dictionaries and nested control structures.

## Project Progress

- [x] Define the structure and objectives of the silent auction program
- [x] Implement dictionary structures to manage participant information and bids
- [x] Develop program functionalities for bid submission and winner determination
- [x] Complete the silent auction program showcasing nested conditional statements and loops

## Code Snippet - Silent Auction Program (Nesting Conditional Statements and Loops)

```python
for key in bidder_Info:
    if float(bidder_Info[key]) > winnerBid:
        winnerBid = float(bidder_Info[key])
        winnerName = key

