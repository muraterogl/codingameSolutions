using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Collections;
using System.Collections.Generic;


class Solution
{
    static Dictionary<string, int> resistors = new Dictionary<string, int>();
    
    static List<string> findElements(string resString)
    {
        List<string> elements = new List<string>();
        List<char> paranthesis = new List<char>();
        string hold = "";

        foreach(char character in resString)
        {
            hold += character;

            if(character.Equals(' '))
            {
                //If paranthesis' are matched, add hold without last space to elements
                if(paranthesis.Count == 0)
                {
                    elements.Add(hold[0..^1]);
                    hold = "";
                }
            }

            else if(character.Equals('(') || character.Equals('['))
            {
                paranthesis.Add(character);
            }

            else if(character.Equals(')') || character.Equals(']'))
            {
                paranthesis.RemoveAt(paranthesis.Count-1);
            }
        }
        if(!hold.Equals(""))
        {
            elements.Add(hold);
        }
        return elements;
    }

    static double findRes(string resString)
    {

        if(resistors.ContainsKey(resString))
        {
            return resistors[resString];
        }
        else
        {
            List<string> elements = findElements(resString[2..^2]);

            //Series Connection
            if(resString[0].Equals('('))
            {
                return elements.Select(element => findRes(element)).Sum();
            }

            //Parallel Connection
            else
            {
                return 1/elements.Select(element => 1/findRes(element)).Sum();
            }
        }
    }
    static void Main(string[] args)
    {
        int N = int.Parse(Console.ReadLine());
        

        for (int i = 0; i < N; i++)
        {
            string[] inputs = Console.ReadLine().Split(' ');
            string name = inputs[0];
            int R = int.Parse(inputs[1]);
            resistors.Add(name, R);
        }

        string circuit = Console.ReadLine();

        Console.WriteLine(findRes(circuit).ToString("N1"));
    }
} 
