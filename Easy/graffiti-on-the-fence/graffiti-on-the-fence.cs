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
        int L = int.Parse(Console.ReadLine());
        int N = int.Parse(Console.ReadLine());

        List<List<int>> results = new List<List<int>>{new List<int>{0,L}};

        for (int i = 0; i < N; i++)
        {
            string[] inputs = Console.ReadLine().Split(' ');
            int st = int.Parse(inputs[0]);
            int ed = int.Parse(inputs[1]);
            List<List<int>> newResults = new List<List<int>>();
            
            results.ForEach((result) => {
                if (ed <= result[0] || st >= result[1])
                {
                    newResults.Add(result);
                }
                else if (st <= result[0] && ed >= result[0] && ed < result[1])
                {
                    newResults.Add(new List<int>{ed, result[1]});
                }
                else if (st > result[0] && ed < result[1])
                {
                    newResults.Add(new List<int>{result[0], st});
                    newResults.Add(new List<int>{ed, result[1]});
                }
                else if (st > result[0] && st < result[1] && ed >= result[1])
                {
                    newResults.Add(new List<int>{result[0], st});
                }
            });

            results = newResults;
        }

        results.ForEach((result) => Console.WriteLine($"{result[0]} {result[1]}"));

        if (results.Count == 0) Console.WriteLine("All painted");
    }
} 
