# Algoran Certificate Creation

In this project, the client is 10 Academy; the client would like to solve the challenge of ensuring that certificates are available to all trainees in a secure way, and (if possible) that certificate holders can benefit from smart contract actions now and in the future.  At present, certificates are distributed as simple PDF files, without the ability to verify their authenticity nor can 10 Academy undertake smart actions with the trainees/their contracts.

10 Academy has partnered with Algorand to use the Algorand Blockchain as the foundational element of the NFT, and this must now be implemented.  In this project you will build end-to-end Web3 dapps on the Algorand Blockchain that will help 10 Academy generate and distribute Non-Fungible Tokens (NFTs) as certificates that will represent the

## Tech Stack
I have used the following techstacks for making this dApp
- React
- Python Algo SDK
- Algorand Sandbox
- MySQL : this should be deprecated for future work
___

git clone https://github.com/fanuelabebe/Algorand_Certificate_Creation.git

cd Algorand_Certificate_Creation
## Installation

# start api
cd ../Frontend/api
uvicorn app:app --reload

# start react frontend
# go to the react folder first 
# from the api folder . . . .
cd ../Frontend/algorand-react
npm run start
