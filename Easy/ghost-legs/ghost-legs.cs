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
        string[] inputs = Console.ReadLine().Split(' ');
        int W = int.Parse(inputs[0]);
        int H = int.Parse(inputs[1]);
        List<string> lines = new List<string>();
        for (int i = 0; i < H; i++)
        {
            lines.Add(Console.ReadLine());
        }
        List<string> alps = lines[0].Split("  ").ToList();
        List<string> ends = lines.Last().Split("  ").ToList();

        alps.ForEach(a=>{
            int cIndex = alps.IndexOf(a);
            for(int i=1; i<lines.Count-1; i++)
            {
                List<string> cr = lines[i].Split("|")[1..^1].ToList();
                if(cIndex==0)
                {
                    if(cr[0]=="--")
                    {
                        cIndex++;
                    }
                }
                else if(cIndex==alps.Count-1)
                {
                    if(cr[cr.Count-1]=="--")
                    {
                        cIndex--;
                    }
                }
                else{
                    if(cr[cIndex-1]=="--")
                    {
                        cIndex--;
                    }
                    else if(cr[cIndex]=="--")
                    {
                        cIndex++;
                    }
                }
            }
            Console.WriteLine(a+ends[cIndex]);
        });
    }
} 
