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
        Dictionary<string, string> d = new Dictionary<string, string>();
        for (int i = 0; i < n; i++)
        {
            string[] inputs = Console.ReadLine().Split(' ');
            string b = inputs[0];
            int c = int.Parse(inputs[1]);
            d.Add(b, ((char)c).ToString());
        }
        string s = Console.ReadLine();  

        string result="";
        int index=0;
        while(s.Length>0)
        {
            int l = s.Length;
            foreach(KeyValuePair<string, string> entry in d)
            {
                if(s.StartsWith(entry.Key))
                {
                    result+=entry.Value;
                    s=s.Substring(entry.Key.Length);
                }
            }
            if(l==s.Length)
            {
                Console.WriteLine($"DECODE FAIL AT INDEX {index}");
                return;
            }
            index += l-s.Length;
        }
        Console.WriteLine(result);
    }
} 
