using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Collections;
using System.Collections.Generic;
using System.Text.RegularExpressions;

class Solution
{
    static void Main(string[] args)
    {
        string b = Console.ReadLine();

        int maxCount = 0;

        for (int i = 0; i < b.Count(); i++)
        {
            string newBits = b[0..i] + "1" + b[(i+1)..];

            int localMax = new Regex("1+").Matches(newBits).ToList().Select(match => match.Value.Count()).Max();

            if (localMax > maxCount) maxCount = localMax;
                
        }

        Console.WriteLine(maxCount);
    }
} 
