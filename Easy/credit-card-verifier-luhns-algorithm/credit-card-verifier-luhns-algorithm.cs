using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Collections;
using System.Collections.Generic;


class Solution
{
    static void Main(string[] args)
    {
        int n = int.Parse(Console.ReadLine());
        for (int i = 0; i < n; i++)
        {
            string card = Console.ReadLine();
            Verifier(card);
        }
    }

    static void Verifier(string card)
    {
        card = card.Replace(" ", "");
        int secondStep = 0;
        for (int i = 0; i < card.Length; i += 2)
        {
            int factor = ((int) card[i]-48) * 2;
            secondStep += factor < 10 ? factor : factor - 9;
        }
        int thirdStep = 0;
        for (int i = 1; i < card.Length; i += 2)
        {
            thirdStep += (int) card[i]-48;
        }
        int fourthStep = secondStep + thirdStep;
        Console.WriteLine(fourthStep % 10 == 0 ? "YES" : "NO");
    }
}