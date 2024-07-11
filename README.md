# Punto-Singular-Challenge
This was a challenge carried out by Punto Singular Academy in order to assess technical programming skills.

## Challenge description
### Instructions

**Console Project:**
This should be a console-based project.

**Functions:**
When the application starts, it should display the following options:
1. **Create account:** Generate a random 10-digit number as a unique account identifier, and request and store the following data:
   i. Account holder's name
   ii. CURP
2. **Show account balance:** To perform this action, the account number must be entered to display the balance of the associated account. Additionally, a reward based on the balance and the duration the account has been with the bank will be shown. There will be 6 different rewards, one for each range established by yourself (you should simulate a way to use different dates to verify this functionality, and it should work by default with the account creation date if a simulated date is not provided).
3. **Deposit money to account**
4. **Withdraw money from account**
5. **Show all accounts:** Only display:
   i. Account holder's name
   ii. Account number
6. **Show transaction history of an account:** Enter the account number for which information is to be queried, and the data to be displayed about the transactions are:
   i. Amount
   ii. Date
   iii. Description
7. Perform the necessary validations to avoid application errors, for example, avoid entering non-numeric characters in the amount field for deposits.

**Notes:**
- For options 3 and 4, the following data should be requested:
  - Account number
  - Amount
  - Date and time
  - Description
- For options 5 and 6, an access password must be requested.

**Test Cases:**
- Create 4 bank accounts with the following data:
  - Pedro Fernández, PD201819HASRTR07
  - Juan Pérez, JP201819HASRTR06
  - Pepito Limón, PL211819HASRTR06
  - María Gamesa, MG211811MASRTR05
- Make a deposit of:
  - $1,500 to Pedro's account
  - $750 to Juan's account
  - $1,110 to Pepito's account
  - $500 to María's account
- Make a withdrawal of:
  - $750 from Pedro's account
  - $200 from Juan's account
  - $520 from Pepito's account
  - $300 from María's account
- Show balance of the accounts of:
  - Pedro
  - María
- Show all accounts created so far
- Show transaction history of the accounts of:
  - Juan
  - Pepito
