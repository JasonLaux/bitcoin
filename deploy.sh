#!/bin/sh
scp -i ~/.ssh/awsFreeTier.pem -r ~/project/bitcoin/deployment ec2-user@ec2-54-221-46-119.compute-1.amazonaws.com:.
