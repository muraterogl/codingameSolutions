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
        List<long> a = Console.ReadLine().Split().Select(n => long.Parse(n)).ToList();
        List<long> b = Console.ReadLine().Split().Select(n => long.Parse(n)).ToList();
        long result = 0;
        while(a.Count > 0)
        {
            long factor = Math.Min(a[0], b[0]);
            result += factor * a[1] * b[1];
            a[0] -= factor;
            b[0] -= factor;
            if (a[0] == 0) a = a.Skip(2).ToList();
            if (b[0] == 0) b = b.Skip(2).ToList();
        }
        Console.WriteLine(result);
    }
}