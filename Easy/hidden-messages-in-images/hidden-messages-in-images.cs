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
        string[] inputs;
        inputs = Console.ReadLine().Split(' ');
        int w = int.Parse(inputs[0]);
        int h = int.Parse(inputs[1]);
        string extracted = "";
        for (int i = 0; i < h; i++)
        {
            
            inputs = Console.ReadLine().Split(' ');
            for (int j = 0; j < w; j++)
            {
                int pixel = int.Parse(inputs[j]);
                extracted += Convert.ToString(pixel, 2)[^1];
            }
        }
        while (extracted.Count() % 8 != 0) extracted = "0" + extracted;

        byte[] bytes = Enumerable.Range(0, extracted.Count()/8)
                                       .Select(i => Convert.ToByte(extracted.Substring(8 * i, 8), 2))
                                       .ToArray();

        Console.WriteLine(Encoding.ASCII.GetString(bytes));
    }
}