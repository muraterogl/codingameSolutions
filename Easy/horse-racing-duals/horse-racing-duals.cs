using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Collections;
using System.Collections.Generic;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
class Solution
{
    static void Main(string[] args)
    {
        int N = int.Parse(Console.ReadLine());
        int result = 999999;
        List<int> pis = new List<int>();
        for (int i = 0; i < N; i++)
        {
            int pi = int.Parse(Console.ReadLine());  
            pis.Add(pi);
        }
        pis.Sort();
        for(int i = 1; i < pis.Count(); i++)
        {
            if(Math.Abs(pis[i]-pis[i-1]) < result) result = Math.Abs(pis[i]-pis[i-1]);
        }

        // Write an answer using Console.WriteLine()
        // To debug: Console.Error.WriteLine("Debug messages...");

        Console.WriteLine(result);
    }
} 
