#! /bin/bash

echo "------------------------------------------------------------------"
echo "||                          start                               ||"
echo "------------------------------------------------------------------"
if [ -z $1 ]
then
    echo "------------------------------------------------------------------"
    echo "||                        填写注释                              ||"
    echo "------------------------------------------------------------------"
else
    git add .
    git commit -m $1
    git push origin master

    echo "------------------------------------------------------------------"
    echo "||                           end                                ||"
    echo "------------------------------------------------------------------"
fi