🏆 Silent Auction Program (Python)

This project is a simple Silent Auction program written in Python.
Multiple bidders can enter their names and bid amounts, and the program automatically determines the highest bidder at the end.

This project is inspired by Dr. Angela Yu’s Python Bootcamp.

📌 Features

Allows multiple bidders to enter bids

Clears the screen between each bidder

Stores all bids in a dictionary

Determines the highest bidder using a custom function

Clean and beginner-friendly Python code

📁 Project Structure
silent-auction/
│
├── main.py        # Main auction program
├── logo.py        # Contains ASCII art for display
└── README.md      # Project documentation

🧠 How It Works

The program:

Displays an ASCII art logo

Repeatedly asks for:

Bidder name

Bid amount

Clears the screen after each entry

When there are no more bidders, it:

Iterates through all bids

Identifies the highest bid

Prints the winner

The winner is determined using:

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    return winner

▶️ Running the Program

Make sure you have Python installed.

Run the script using:

python main.py

🖥️ Example Output
Enter your name: Mohit
Enter your bid amount: $300
Are there any other bidders? Type 'yes' or 'no': yes

Enter your name: Aman
Enter your bid amount: $450
Are there any other bidders? Type 'yes' or 'no': no

The winner is Aman with a bid of $450

💡 Optional Improvement

You can replace the custom function with Python’s built-in max():

highest_bidder = max(bidders, key=bidders.get)

📜 License

This project is free to use for learning and practice.