pragma solidity ^0.5.0;

contract Crowdfunding {
    address payable owner;
    uint max_block;
    uint goal;

    mapping(address => uint) backers;
    bool funded = false;

    constructor() public {
        owner = address(0x10000);
        max_block = 4600000;
        goal = 1000000;
    }

    function Donate() public payable {
        if(max_block <= block.number) {
            revert();
        }
        else {
            if(backers[msg.sender] == 0) {
                backers[msg.sender] = msg.value;
            }
            else {
                revert();
            }
        }
    }

    function GetFunds() public {
        if(max_block < block.number && msg.sender == owner) {
            if(goal <= address(this).balance) {
                funded = true;
                owner.transfer(address(this).balance);
            }
            else {
                revert();
            }
        }
        else {
            revert();
        }
    }

    function Claim() public {
        if(block.number <= max_block) {
            revert();
        }
        else {
            if(backers[msg.sender] == 0 || funded || goal <= address(this).balance) {
                revert();
            }
            else {
                uint val = backers[msg.sender];
                backers[msg.sender] = 0;
                msg.sender.transfer(val);
            }
        }
    }
}
